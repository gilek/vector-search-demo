import typing as t
from collections import defaultdict

from kink import inject


@inject
class RRF:
    K = 60

    def compute(self, rankings: t.List[t.List[str]]) -> t.List[t.Tuple[str, float]]:
        scores = defaultdict(float)

        for ranking in rankings:
            for rank, doc_id in enumerate(ranking, start=1):
                scores[doc_id] += 1 / (self.K + rank)

        return sorted(scores.items(), key=lambda x: x[1], reverse=True)

