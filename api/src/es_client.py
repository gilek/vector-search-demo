import typing as t

from elastic_transport import ObjectApiResponse
from elasticsearch import Elasticsearch
from kink import inject


@inject
class EsClient:
    def __init__(self, es_api: str, es_index: str) -> None:
        self.client = Elasticsearch(hosts=[es_api])
        self.index_name = es_index

    def search(self, body: t.Dict[str, any]) -> ObjectApiResponse[t.Any]:
        return self.client.search(index=self.index_name, body=body)

    def get(self, id: str) -> ObjectApiResponse[t.Any]:
        return self.client.get(index=self.index_name, id=id)
