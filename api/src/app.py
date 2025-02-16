from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .es_client import EsClient
from .search import Search
from .vector_generator import VectorGenerator

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/search/lexical/blip")
def search_lexical_blip(query: str):
    return Search().lexical(["description_blip"], query)


@app.get("/api/search/vector/blip-minilm")
def search_vector_blip(query: str):
    return Search().vector(
        "description_blip_vector",
        VectorGenerator().gen_minimilm(query),
    )


@app.get("/api/search/vector/clip")
def search_vector_clip(query: str):
    return Search().vector(
        "image_vector",
        VectorGenerator().gen_clip(query),
    )


@app.get("/api/search/similar/{doc_id}")
def search_similar(doc_id: str):
    doc = EsClient().get(doc_id)

    return Search().vector("image_vector", doc["_source"]["image_vector"])


@app.get("/api/search/hybrid/blip")
def search_hybrid_blip(query: str):
    return Search().hybrid(
        lexical_field="description_blip",
        lexical_query=query,
        vector_field="description_blip_vector",
        vector_vector=VectorGenerator().gen_minimilm(query),
    )


@app.get("/api/search/all")
def search_all():
    return Search().all()
