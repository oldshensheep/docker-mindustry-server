FROM alpine:latest

ARG tag_name

ENV \
    CONFIG=/opt/mindustry/config

RUN \
    apk add --no-cache openjdk8-jre shadow  && \
    mkdir -p /opt/mindustry && \
    mkdir -p /opt/mindustry/config && \
    useradd -u 999 -U -s /bin/false sheep && \
    groupmod -o -g 1000 sheep && \
    usermod -G sheep sheep && \
    chown sheep:sheep -R /opt/mindustry && \
    wget https://github.com/Anuken/Mindustry/releases/download/${tag_name}/server-release.jar -O /opt/mindustry/server-release.jar

VOLUME /opt/mindustry/config

EXPOSE 6567
EXPOSE 6859

CMD \
    cd /opt/mindustry && \
    su -s '/bin/sh' sheep -c "/usr/bin/java -jar /opt/mindustry/server-release.jar"

USER sheep:sheep
