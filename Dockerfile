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
    chown sheep:sheep -R /opt/mindustry/config && \
    wget https://github.com/Anuken/Mindustry/releases/download/${tag_name}/server-release.jar -O /opt/mindustry/server-release.jar


COPY docker-entrypoint.sh /

VOLUME /opt/mindustry/config

EXPOSE 6567
EXPOSE 6859

ENTRYPOINT ["/docker-entrypoint.sh"]