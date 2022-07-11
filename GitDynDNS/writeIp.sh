#!/bin/bash

script_directory="FILL IN CORRECT DIR HERE"

date=$(date +"%Y%m%d%H%M%S%3N")

cd ${script_directory}

curl https://ipinfo.io/ip > ip
git add ip
git commit -m "updated ip: ${date}"
git push
