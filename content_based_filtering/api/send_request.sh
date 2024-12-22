#!/bin/bash

url="http://127.0.0.1:8000/recommend_tracks"
data='{"user_id": 0}'

response=$(curl -s -X POST "$url" -H "Content-Type: application/json" -d "$data")

echo "response from server: $response"
