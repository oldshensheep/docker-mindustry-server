import subprocess
import requests

realeases = requests.get(
    'https://api.github.com/repos/Anuken/Mindustry/releases').json()
for index, realease in enumerate(realeases[::-1]):
    tag_name = realease["tag_name"]
    ext_tag = ''
    if index == 0:
        ext_tag = "-t oldshensheep/mindustry-server:latest \\"
    if realease['prerelease'] == False:
        ext_tag += "-t oldshensheep/mindustry-server:stable \\"
    subprocess.call(f'''
    docker buildx build \\
    --push \\
    --platform linux/arm,linux/arm64,linux/amd64 \\
    -t oldshensheep/mindustry-server:{tag_name} \\
    {ext_tag} \\
    --build-arg "tag_name"="{tag_name}" .
    ''')
