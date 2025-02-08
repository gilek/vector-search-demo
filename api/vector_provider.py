from typing import List

from kink import inject
from sentence_transformers import SentenceTransformer


@inject
class VectorProvider:
    def __init__(
        self, model_mini_lm: SentenceTransformer, model_clip: SentenceTransformer
    ):
        self.model_mini_lm = model_mini_lm
        self.model_clip = model_clip

    def gen_minimilm(self, text: str) -> List[float]:
        return self.model_mini_lm.encode(text).tolist()

    def gen_clip(self, text: str) -> List[float]:
        return self.model_clip.encode(
            text, convert_to_tensor=True, show_progress_bar=False
        ).tolist()
