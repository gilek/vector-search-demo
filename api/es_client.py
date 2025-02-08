import typing as t

from elastic_transport import ObjectApiResponse
from elasticsearch import Elasticsearch
from kink import inject


@inject
class EsClient:
    INDEX = "tshirts"  # TODO dependency

    def __init__(self, es_host: str):
        self.client = Elasticsearch(hosts=[es_host])

    def search(self, body: t.Dict[str, any]) -> ObjectApiResponse[t.Any]:
        return self.client.search(index=self.INDEX, body=body)

    def get(self, id: str) -> ObjectApiResponse[t.Any]:
        return self.client.get(index=self.INDEX, id=id)
