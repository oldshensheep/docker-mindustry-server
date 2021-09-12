#!/bin/sh
chown -R sheep:sheep /opt/mindustry/config
cd /opt/mindustry
su -s '/bin/sh' sheep -c "/usr/bin/java -jar /opt/mindustry/server-release.jar"
