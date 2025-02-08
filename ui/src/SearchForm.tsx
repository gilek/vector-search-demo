import React from "react";
import {
  Box,
  Button,
  FormControlLabel,
  Radio,
  RadioGroup,
  TextField,
} from "@mui/material";
import SearchFilters from "./SearchFilters";
import { SearchFilterMode } from "./SearchFilterMode";

interface SearchFormProps {
  loading: boolean;
  onSearch: (filters: SearchFilters) => void;
  onSearchAll: (filters: SearchFilters) => void;
}

export default function SearchForm({
  onSearch,
  onSearchAll,
  loading,
}: SearchFormProps) {
  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();

    onSearch({
      query: event.target.query.value,
      mode: event.target.mode.value,
    });
  };

  return (
    <Box
      component="form"
      onSubmit={handleSubmit}
      sx={{ display: "flex", flexDirection: "column" }}
    >
      <Box sx={{ display: "inline-flex", gap: "6px" }}>
        <TextField
          name="query"
          label="Query"
          sx={{
            input: {
              background: "white",
            },
          }}
          slotProps={{
            inputLabel: {
              shrink: true,
            },
          }}
          fullWidth
        />
        <Button type="submit" variant="contained" loading={loading}>
          Search
        </Button>
        <Button type="button" onClick={onSearchAll} loading={loading}>
          Random
        </Button>
      </Box>

      <RadioGroup row defaultValue="lexical_blip" name="mode">
        <FormControlLabel
          value={SearchFilterMode.LEXICAL_BLIP}
          control={<Radio />}
          label="Lexical BLIP"
        />

        <FormControlLabel
          value={SearchFilterMode.VECTOR_BLIP_MINILM}
          control={<Radio />}
          label="Vector MiniLM (BLIP)"
        />

        {/*<FormControlLabel*/}
        {/*  value={SearchFilterMode.VECTOR_CLIP}*/}
        {/*  control={<Radio />}*/}
        {/*  label="Vector CLIP"*/}
        {/*/>*/}

        <FormControlLabel
          value={SearchFilterMode.HYBRID_BLIP}
          control={<Radio />}
          label="Hybrid BLIP"
        />
      </RadioGroup>
    </Box>
  );
}
