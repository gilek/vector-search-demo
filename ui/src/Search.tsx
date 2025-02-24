import React, { useState } from "react";
import { Container } from "@mui/material";
import SearchForm from "./SearchForm";
import SearchFilters from "./SearchFilters";
import SearchItem from "./SearchItem";
import SearchList from "./SearchList";
import { useSnackbar } from "notistack";
import { SearchFilterMode } from "./SearchFilterMode";

export default function Search() {
  const { enqueueSnackbar } = useSnackbar();
  const [items, setItems] = useState<SearchItem[]>([]);
  const [loading, setLoading] = useState<symbol>(false);

  const fetchProducts = (uri: string) => {
    setLoading(true);
    fetch(`${process.env.API}${uri}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Not found");
        }
        return response.json();
      })
      .then((data) => setItems(data))
      .catch(() =>
        enqueueSnackbar("Unable to search products", { variant: "error" }),
      )
      .finally(() => setLoading(false));
  };

  const resolveUri = ({ mode, query }: SearchFilters): string | null => {
    switch (mode) {
      case SearchFilterMode.LEXICAL_BLIP:
        return `/api/search/lexical/blip?query=${query}`;

      case SearchFilterMode.VECTOR_BLIP_MINILM:
        return `/api/search/vector/blip-minilm?query=${query}`;

      case SearchFilterMode.VECTOR_CLIP:
        return `/api/search/vector/clip?query=${query}`;

      case SearchFilterMode.HYBRID_BLIP:
        return `/api/search/hybrid/blip?query=${query}`;

      default:
        return null;
    }
  };

  const handleSearch = (filters: SearchFilters) => {
    const uri = resolveUri(filters);
    if (uri === null) {
      enqueueSnackbar("Mode is not supported", { variant: "error" });
      return;
    }
    fetchProducts(uri);
  };

  const handleSearchAll = () => {
    fetchProducts("/api/search/all");
  };

  const handleSimilarSearch = (id: string) => {
    fetchProducts(`/api/search/similar/${id}`);
  };

  return (
    <Container style={{ paddingTop: "30px" }}>
      <SearchForm
        onSearch={handleSearch}
        onSearchAll={handleSearchAll}
        loading={loading}
      />
      <SearchList items={items} onSimilarSearch={handleSimilarSearch} />
    </Container>
  );
}
