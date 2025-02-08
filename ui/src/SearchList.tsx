import React, { Fragment } from "react";
import SearchItem from "./SearchItem";
import { Grid2 as Grid } from "@mui/material";
import SearchListItem from "./SearchListItem";

interface SearchListProps {
  items: SearchItem[];
  onSimilarSearch: (id: string) => void;
}

export default function SearchList({
  items,
  onSimilarSearch,
}: SearchListProps) {
  return (
    <Grid container spacing={2}>
      {items &&
        items.map((item) => (
          <Grid size={3}>
            <Fragment key={item.id}>
              <SearchListItem onSimilarSearch={onSimilarSearch} item={item} />
            </Fragment>
          </Grid>
        ))}
    </Grid>
  );
}
