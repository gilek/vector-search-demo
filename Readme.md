# Elasticsearch hybrid search demo

[Presentation](https://docs.google.com/presentation/d/1_UtZA1_vgfahuqO-dSebo2z3_G75rVUMUwSxA0vOikY/edit?usp=sharing)

![Screenshot from 2025-02-18 20-17-36](https://github.com/user-attachments/assets/190ad91a-7062-4584-aa42-722dcf6b1849)

A demo of hybrid search done in Elasticsearch. The project was never meant to be published, but over time, I thought some part of it might be useful to someone.

The goal of the project was to allow users to search through a collection of t-shirt photos. The input was just image files, without descriptions, brand names, colors, etc. The images were taken from the [Kaggle Fashon dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset), except that they have been downsized to 640px. Dataset, along with some of the original data is available at [Hugging face](https://huggingface.co/datasets/gilek19/tshirts)

The idea was to test two options:
- use the [BLIP](https://huggingface.co/docs/transformers/model_doc/blip) model to generate image descriptions and then through some [SBERT](https://sbert.net/docs/sentence_transformer/pretrained_models.html) models convert them to their vector representations. BLIP generates data only in English, to provide support for multiple languages, choose the [paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) model,
- use the [CLIP](https://github.com/openai/CLIP) model that combines the above approaches, but does it in one step. Both the text and the image are in the same space, so an additional model is not needed.

Lexical search is based on data generated by the BLIP model.

When it comes to hybrid search, Elasticsearch provides an [RRF](https://www.elastic.co/guide/en/elasticsearch/reference/current/rrf.html) scorer, but unfortunately it is paid, so I used my own naive [implementation](https://github.com/gilek/vector-search-demo/blob/master/api/src/rrf.py).

# How to set it up

1. `make run` builds and runs the API, UI and Elasticsearch containers,
1. `make images` imports a set of images from the Hugging Face dataset,
1. `make import` imports the output data from the [prepare-data.py](https://github.com/gilek/vector-search-demo/blob/master/data/prepare-data.py) script into elasticsearch.

The UI by default is available at [http://localhost:8080](http://localhost:8080)
