import React from "react";
import ReactDOM from "react-dom/client";
import Search from "./Search";
import { SnackbarProvider } from "notistack";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <SnackbarProvider>
    <Search />
  </SnackbarProvider>,
);
