from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from collaborative_filtering.src.services import recommend_songs

app = FastAPI()


class RecommendationRequest(BaseModel):
    target_user_id: int


class RecommendationResponse(BaseModel):
    recommended_songs: List[int]


@app.post("/recommend_songs/", response_model=RecommendationResponse)
async def recommend_songs_endpoint(request: RecommendationRequest):
    try:
        recommended_songs = recommend_songs(request.target_user_id)
        return RecommendationResponse(recommended_songs=recommended_songs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"an error occurred: {str(e)}")
