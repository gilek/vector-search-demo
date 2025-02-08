from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.es_client import EsClient
from api.search_service import SearchService
from api.vector_provider import VectorProvider

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search/lexical/blip")
def search_lexical_blip(query: str):
    return SearchService().lexical(["description_blip"], query)


@app.get("/search/vector/blip-minilm")
def search_vector_blip(query: str):
    return SearchService().vector(
        "description_blip_vector",
        VectorProvider().gen_minimilm(query),
    )


@app.get("/search/vector/clip")
def search_vector_clip(query: str):
    return SearchService().vector(
        "image_vector",
        VectorProvider().gen_clip(query),
    )


@app.get("/search/similar/{doc_id}")
def search_similar(doc_id: str):
    doc = EsClient().get(doc_id)

    return SearchService().vector("image_vector", doc["_source"]["image_vector"])


@app.get("/search/hybrid/blip")
def search_hybrid_blip(query: str):
    return SearchService().hybrid(
        lexical_field="description_blip",
        lexical_query=query,
        vector_field="description_blip_vector",
        vector_vector=VectorProvider().gen_minimilm(query),
    )


@app.get("/search/all")
def search_all():
    return SearchService().all()
