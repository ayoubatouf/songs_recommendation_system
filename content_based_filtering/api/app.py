from fastapi import FastAPI, HTTPException
from collaborative_filtering.config.paths import USERS_TRACKS_DATASET_PATH
from content_based_filtering.data.data_loader import CSVDataLoader
from content_based_filtering.data.feature_extractor import TrackFeatureExtractor
from content_based_filtering.src.models import UserRequest
from content_based_filtering.src.services import RecommendationService
from content_based_filtering.src.similarity_search import FaissSimilaritySearch


app = FastAPI()


@app.on_event("startup")
def initialize():
    global recommendation_service

    data_loader = CSVDataLoader(USERS_TRACKS_DATASET_PATH)
    df_original = data_loader.load_data()

    df = df_original.copy()  # working dataset for feature extraction and indexing

    feature_extractor = TrackFeatureExtractor()
    combined_features = feature_extractor.extract_features(df)

    similarity_search = FaissSimilaritySearch(df, combined_features)

    recommendation_service = RecommendationService(df_original, similarity_search)


@app.post("/recommend_tracks")
def recommend_tracks(request: UserRequest):
    try:

        recommendations = recommendation_service.recommend_for_user(request.user_id)

        track_ids = recommendations["track_id"].tolist()[:5]  # limit result on 5 recs

        return {"recommended_track_ids": track_ids}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


@app.get("/")
def root():
    return {"message": "welcome to the music recommendation API!"}
