from os import getenv

from kink import di
from sentence_transformers import SentenceTransformer
from api.rrf import RRF


def bootstrap_di():
    model = SentenceTransformer(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )
    di["es_host"] = getenv("ES_API")
    di["model_mini_lm"] = model
    # di["model_clip"] = SentenceTransformer("clip-ViT-B-32-multilingual-v1")
    di["model_clip"] = model # TODO tmp
    di[RRF] = lambda di: RRF()
