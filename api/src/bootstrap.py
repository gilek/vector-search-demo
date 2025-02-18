from os import getenv

from kink import di
from sentence_transformers import SentenceTransformer

from .rrf import RRF


def bootstrap_di():
    model = SentenceTransformer(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )
    di["es_api"] = getenv("ES_API")
    di["es_index"] = getenv("ES_INDEX")
    di["model_mini_lm"] = model
    # di["model_clip"] = SentenceTransformer("clip-ViT-B-32-multilingual-v1")
    di["model_clip"] = model # TODO tmp
    di[RRF] = lambda di: RRF()
