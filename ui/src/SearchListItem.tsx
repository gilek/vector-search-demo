import React from "react";
import SearchItem from "./SearchItem";
import {
  Box,
  Button,
  Card,
  CardActions,
  CardContent,
  CardHeader,
  CardMedia,
  Divider,
  Typography,
} from "@mui/material";

interface SearchListItemProps {
  item: SearchItem;
  onSimilarSearch: (id: string) => void;
}

export default function SearchListItem({
  item,
  onSimilarSearch,
}: SearchListItemProps) {
  return (
    <Card>
      <CardMedia component="img" image={`images/${item.image}`} />
      <CardContent>
        <Typography variant="body1" sx={{ marginBottom: "10px" }}>
          {item.description}
        </Typography>
        <Typography variant="body2">BLIP: {item.description_blip}</Typography>
      </CardContent>

      <CardActions>
        <Button size="small" onClick={() => onSimilarSearch(item.id)}>
          Similar (CLIP)
        </Button>
      </CardActions>
    </Card>
  );
}
