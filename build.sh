#!/bin/bash
latest_tag_name=$(curl -s https://api.github.com/repos/Anuken/Mindustry/releases | jq -r .[0].tag_name)
echo $latest_tag_name

docker buildx build \
    --push \
    --platform linux/arm/v7,linux/arm64/v8,linux/amd64 \
    -t oldshensheep/mindustry-server:$latest_tag_name \
    -t oldshensheep/mindustry-server:latest \
    --build-arg "tag_name"="$latest_tag_name" .
