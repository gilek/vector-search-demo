import os

from elasticsearch import Elasticsearch
import pandas as pd
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()
index = os.getenv("ES_INDEX")
es = Elasticsearch(os.getenv("ES_API"))

es.options(ignore_status=404).indices.delete(index=index)
create_body = {
    "settings": {
        "number_of_shards": 1,
        "analysis": {
            "filter": {
                "english_stop": {
                    "type": "stop",
                    "stopwords": "_english_"
                },
                "english_stemmer": {
                    "type": "stemmer",
                    "language": "english"
                },
                "english_possessive_stemmer": {
                    "type": "stemmer",
                    "language": "possessive_english"
                }
            },
            "analyzer": {
                "text_en": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": [
                        "english_possessive_stemmer",
                        "lowercase",
                        "english_stop",
                        "english_stemmer"
                    ]
                }
            }
        },
        "index": {
            "similarity": {
                "custom_bm25": {
                    "type": "BM25",
                    "b": 0.75,
                    "k1": 0
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "image": {
                "type": "keyword"
            },
            "gender": {
                "type": "text",
                "analyzer": "text_en",
            },
            "color": {
                "type": "text",
                "analyzer": "text_en",
            },
            "season": {
                "type": "text",
                "analyzer": "text_en",
            },
            "description": {
                "type": "text",
                "analyzer": "text_en",
            },
            "description_blip": {
                "type": "text",
                "analyzer": "text_en",
                "similarity": "custom_bm25"
            },
            "description_vector": {
                "type": "dense_vector",
                "dims": 384
            },
            "image_vector": {
                "type": "dense_vector",
                "dims": 512
            }
        }
    }
}
es.indices.create(index=index, body=create_body)

df = pd.read_json("tshirts.json")

for _, row in tqdm(df.iterrows(), total=df.shape[0]):
    body = {
        "image": f'{row["id"]}.jpg',
        "gender": row["gender"],
        "color": row["color"],
        "season": row["season"],
        "description": row["description"],
        "description_blip": row["description_blip"],
        "description_blip_vector": row["description_vector"],
        "image_vector": row["image_vector"],
    }
    es.index(index=index, body=body)
