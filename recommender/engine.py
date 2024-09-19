from embeddings.model import EmbeddingModel
from retrieval.vector_search import VectorSearch
from retrieval.context_retriever import ContextRetriever
from llm.model import LlamaModel
from llm.prompt_template import generate_prompt
from conversation.history_manager import HistoryManager
from conversation.state_tracker import StateTracker
from app.config import settings

class RecommenderEngine:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_search = VectorSearch()
        self.context_retriever = ContextRetriever()
        self.llm_model = LlamaModel()
        self.history_manager = HistoryManager()
        self.state_tracker = StateTracker()

    async def get_recommendations(self, user_id: str, query: str):
        # Process query
        query_embedding = self.embedding_model.encode(query)
        
        # Retrieve similar locations
        similar_loc_ids = await self.vector_search.search(query_embedding)
        loc_context = self.context_retriever.get_context(similar_loc_ids)
        
        # Get conversation context
        conversation_history = await self.history_manager.get_history(user_id)
        dialogue_state = await self.state_tracker.get_state(user_id)
        
        # Generate prompt
        prompt = generate_prompt(query, loc_context, conversation_history, dialogue_state)
        
        # Generate recommendations
        raw_recommendations = await self.llm_model.generate(prompt)
        
        # Process and return recommendations
        return self._process_recommendations(raw_recommendations)

    def _process_recommendations(self, raw_recommendations):
        # This is a placeholder implementation
        recommendations = raw_recommendations.split('\n')[:10]
        return [rec.strip() for rec in recommendations if rec.strip()]