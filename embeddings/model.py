from sentence_transformers import SentenceTransformer
from app.config import settings

class EmbeddingModel:
    def __init__(self):
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)

    def encode(self, text):
        return self.model.encode(text)

    def encode_batch(self, texts):
        return self.model.encode(texts)