import typing as t

from elastic_transport import ObjectApiResponse
from kink import inject

from api.es_client import EsClient
from api.product import Product
from api.rrf import RRF


@inject
class SearchService:
    def __init__(self, es_client: EsClient, rrf: RRF):
        self.es_client = es_client
        self.rrf = rrf

        self.__SIZE = 20
        self.__COMMON = {
            "fields": [
                "image",
                "gender",
                "color",
                "season",
                "description",
                "description_blip",
            ],
            "size": self.__SIZE,
            "_source": False,
        }

    def lexical(self, fields: t.List[str], query: str) -> t.List[Product]:
        response = self.es_client.search(
            {
                "query": self.__prepare_query(fields, query),
                **self.__COMMON,
            }
        )

        return self.__to_products(response)

    def vector(self, field: str, vector: t.List[float]) -> t.List[Product]:
        response = self.es_client.search(
            {
                "knn": [self.__prepare_knn(field, vector)],
                **self.__COMMON,
            }
        )

        return self.__to_products(response)

    def all(self) -> t.List[Product]:
        response = self.es_client.search(
            {
                "query": {
                    "function_score": {
                        "query": {"match_all": {}},
                        "random_score": {},
                    },
                },
                **self.__COMMON,
                "size": 100,
            }
        )

        return self.__to_products(response)

    def hybrid(
        self,
        lexical_field: str,
        lexical_query: str,
        vector_field: str,
        vector_vector: t.List[float],
    ) -> t.List[Product]:
        # RRF is a paid feature. We could use it as the following:
        # response = self.es_client.search({
        #     "query": self.__prepare_query([lexical_field], lexical_query),
        #     "knn": self.__prepare_knn(vector_field, vector_vector),
        #     "rank": {
        #         "rrf": {
        #             "rank_window_size": self.__SIZE,
        #         },
        #     },
        #     **self.__COMMON,
        # })
        #
        # return self.__to_products(response)

        # TODO more efficient would be to use mquery
        lexical_res = self.lexical([lexical_field], lexical_query)
        vector_res = self.vector(vector_field, vector_vector)

        all_products = {}
        rankings = []
        for products in [lexical_res, vector_res]:
            ranking = []
            for product in products:
                ranking.append(product.id)
                all_products[product.id] = product
            rankings.append(ranking)

        return [all_products[score[0]] for score in self.rrf.compute(rankings)]

    def __prepare_knn(self, field: str, vector: t.List[float]) -> t.Dict[str, t.Any]:
        return {
            "field": field,
            "k": 20,
            "num_candidates": 1000,
            "query_vector": vector,
        }

    def __prepare_query(self, fields: t.List[str], query: str) -> t.Dict[str, t.Any]:
        return {
            "multi_match": {
                "query": query,
                "fields": fields,
                "type": "best_fields",
                "tie_breaker": 0.3,
            }
        }

    def __to_products(self, response: ObjectApiResponse[t.Any]) -> t.List[Product]:
        return [
            Product(**hit["fields"], id=hit["_id"]) for hit in response["hits"]["hits"]
        ]
