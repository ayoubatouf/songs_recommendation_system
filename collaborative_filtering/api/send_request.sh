#!/bin/bash


URL="http://127.0.0.1:8000/recommend_songs/"

PAYLOAD='{
  "target_user_id": 0
}'

curl -X 'POST' \
  "$URL" \
  -H 'Content-Type: application/json' \
  -d "$PAYLOAD"
