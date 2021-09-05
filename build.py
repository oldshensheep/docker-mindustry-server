import os

import requests

realeases = requests.get(
    'https://api.github.com/repos/Anuken/Mindustry/releases').json()
for index, realease in enumerate(realeases):
    tag_name = realease["tag_name"]
    latest = ''
    if index == 0:
        latest = "-t oldshensheep/mindustry-server:latest"
    os.system(f'''
    docker buildx build \\
    --push \\
    --platform linux/arm,linux/arm64,linux/amd64 \\
    -t oldshensheep/mindustry-server:{tag_name} \\
    {latest} \\
    --build-arg "tag_name"="{tag_name}" .
    ''')
