import subprocess
import requests

releases = requests.get(
    'https://api.github.com/repos/Anuken/Mindustry/releases').json()
for index, realease in enumerate(releases[::-1]):
    tag_name = realease["tag_name"]
    ext_tag = ''
    if index == len(releases) - 1:
        ext_tag += "-t oldshensheep/mindustry-server:latest -t ghcr.io/oldshensheep/mindustry-server:latest \\"
    if realease['prerelease'] == False:
        ext_tag += "-t oldshensheep/mindustry-server:stable -t ghcr.io/oldshensheep/mindustry-server:stable \\"
    call_str = f'''
    docker buildx build \\
    --push \\
    --platform linux/arm,linux/arm64,linux/amd64 \\
    -t oldshensheep/mindustry-server:{tag_name} \\
    -t ghcr.io/oldshensheep/mindustry-server:{tag_name} \\
    {ext_tag} \\
    --build-arg "tag_name"="{tag_name}" .
    '''
    print(call_str)
    subprocess.call(call_str, shell=True)
