# Docker image for mindustry server 
Docker hub https://hub.docker.com/repository/docker/oldshensheep/mindustry-server  
you can see all realeases there.  
What is Mindustry?  
A sandbox tower defense game. see https://github.com/Anuken/Mindustry
## How to run
First you need install docker and open terminal input the flowing.  
You can modify the `/path/to/config` that you need as it used for save data and config.
```bash
sudo docker run  -it \
            -p 6567 -p 6567/udp \
            -v /path/to/config:/opt/mindustry/config \
            --name mindustry-server \
            --detach \
            oldshensheep/mindustry-server:latest
```
### I want specific verion
You can replace `oldshensheep/mindustry-server:latest` with `oldshensheep/mindustry-server:v130.1` etc.  
where dose the `v130.1` come from? https://github.com/Anuken/Mindustry/tags  
the `latest` is always the latest as anuken's Mindustry version. `stable` is stable version.
