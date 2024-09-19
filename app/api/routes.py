from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from recommender.engine import RecommenderEngine

router = APIRouter()

class Query(BaseModel):
    user_id: str
    query: str

recommender = RecommenderEngine()

@router.post("/recommend")
async def get_recommendations(query: Query):
    try:
        recommendations = await recommender.get_recommendations(query.user_id, query.query)
        
        # Update conversation history and state
        await recommender.history_manager.add_to_history(query.user_id, query.query, str(recommendations))
        current_state = await recommender.state_tracker.get_state(query.user_id)
        new_state = {**current_state, "last_query": query.query}
        await recommender.state_tracker.update_state(query.user_id, new_state)
        
        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))