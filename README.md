# Songs recommendation system

## Overview

In this project, we implement two methods for recommending songs to users: collaborative filtering and content-based filtering. Collaborative filtering relies on `nearest neighbors`, using user ratings of songs to identify similar tracks based on preferences. In contrast, content-based filtering leverages `FAISS (Facebook AI Similarity Search)` to recommend songs based on their intrinsic characteristics, such as audio features and genre information, which are transformed into `TF-IDF embeddings`. By analyzing song features and user ratings, we aim to provide personalized song recommendations. The datasets used are available at :`https://www.kaggle.com/datasets/rymnikski/dataset-for-collaborative-filters` and `https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset` 

## Usage
Run the chosen API server in its directory with `uvicorn app:app --reload` , and test it by executing `./send_request.sh` to send a user ID and receive recommended track IDs.


