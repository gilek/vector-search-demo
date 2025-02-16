from typing import List

from kink import inject
from sentence_transformers import SentenceTransformer


@inject
class VectorGenerator:
    def __init__(
        self, model_mini_lm: SentenceTransformer, model_clip: SentenceTransformer
    ):
        self.model_mini_lm = model_mini_lm
        self.model_clip = model_clip

    def minimilm(self, text: str) -> List[float]:
        return self.model_mini_lm.encode(text).tolist()

    def clip(self, text: str) -> List[float]:
        return self.model_clip.encode(
            text, convert_to_tensor=True, show_progress_bar=False
        ).tolist()
