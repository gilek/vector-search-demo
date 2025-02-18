import React from "react";
import SearchItem from "./SearchItem";
import {
  Button,
  Card,
  CardActions,
  CardContent,
  CardMedia,
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
