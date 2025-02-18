# Elasticsearch hybrid search demo

![Screenshot](https://github.com/user-attachments/assets/6c0808dd-cf16-407a-a63d-23a650afd59c)


A demo of hybrid search done in Elasticsearch. The project was never meant to be published, but over time, I thought some part of it might be useful to someone.

The goal of the project was to allow users to search through a collection of photos of people wearing t-shirts. The input was just image files, without descriptions, brand names, colors, etc. The images were taken from the [Kaggle Fashon dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset), except that they have been downsized to 640px. Dataset, along with some of the original date is available at [Hugging face](https://huggingface.co/datasets/gilek19/tshirts)

The idea was to test two options:
- use the [BLIP](https://huggingface.co/docs/transformers/model_doc/blip) model to generate image descriptions and then through some [SBERT](https://sbert.net/docs/sentence_transformer/pretrained_models.html) models convert them to their vector representations. BLIP generates data only in English, to provide support for multiple languages, choose the [paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) model,
- use the [CLIP](https://github.com/openai/CLIP) model that combines the above approaches, but does it in one step. Both the text and the image are in the same space, so an additional model is not needed.

Lexical search is based on data generated by the BLIP model.

When it comes to hybrid search, Elasticsearch provides an [RRF](https://www.elastic.co/guide/en/elasticsearch/reference/current/rrf.html) scorer, but unfortunately it is paid, so I used my own naive [implementation](https://github.com/gilek/vector-search-demo/blob/master/api/src/rrf.py).

# How to set it up

1. `make run` builds and runs the API, UI and Elasticsearch containers,
1. `make images` imports a set of images from the Hugging Face dataset,
1. `make import` imports the output data from the [prepare-data.py](https://github.com/gilek/vector-search-demo/blob/master/data/prepare-data.py) script into elasticsearch.
