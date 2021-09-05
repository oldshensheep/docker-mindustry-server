# Docker image for mindustry server 
What is Mindustry?  
A sandbox tower defense game. see https://github.com/Anuken/Mindustry
## How to Run
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
