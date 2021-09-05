#!/bin/bash
latest_tag_name=$(curl -s https://api.github.com/repos/Anuken/Mindustry/releases)
echo $latest_tag_name