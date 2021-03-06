import subprocess
import requests

realeases = requests.get(
    'https://api.github.com/repos/Anuken/Mindustry/releases').json()

realease = realeases[0]
tag_name = realease["tag_name"]
ext_tag = ''

if realease['prerelease'] == False:
    ext_tag = "-t oldshensheep/mindustry-server:stable"
call_str = f'''
docker buildx build \\
--push \\
--platform linux/arm,linux/arm64,linux/amd64 \\
-t oldshensheep/mindustry-server:{tag_name} \\
-t oldshensheep/mindustry-server:latest \\
-t ghcr.io/oldshensheep/mindustry-server:{tag_name} \\
-t ghcr.io/oldshensheep/mindustry-server:latest \\
{ext_tag} \\
--build-arg "tag_name"="{tag_name}" .
'''
print(call_str)
subprocess.call(call_str, shell=True)
