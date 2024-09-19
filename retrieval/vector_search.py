import numpy as np
from sentence_transformers import SentenceTransformer
from utils.dummy_data import LOCATION_DATA
from app.config import settings

class VectorSearch:
    def __init__(self):
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)
        self.loc_embeddings = self._preprocess_locations()

    def _preprocess_locations(self):
        loc_texts = []
        
        for loc in LOCATION_DATA:
            text_parts = [f"DisplayName: {loc.get('displayName', 'N/A')}"]
            
            if loc.get('types'):
                types_str = '; '.join(loc['types'])
                text_parts.append(f"Types: {types_str}")
            
            if loc.get('reviews'):
                review_texts = [review.get('text', '') for review in loc['reviews'] if review.get('text')]
                if review_texts:
                    reviews_str = '; '.join(review_texts)
                    text_parts.append(f"Reviews: {reviews_str}")
            
            if loc.get('rating') is not None:
                text_parts.append(f"Rating: {loc['rating']}")
            
            loc_text = '. '.join(text_parts)
            loc_texts.append(loc_text)
        
        return self.model.encode(loc_texts)

    async def search(self, query_embedding, top_k=5):
        similarities = np.dot(self.loc_embeddings, query_embedding)
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        return [LOCATION_DATA[i]['id'] for i in top_indices]