#!/usr/bin/env bash

java -jar selenium-server-standalone-2.43.1.jar \
    -role node \
    -hub http://localhost:4444/grid/register \
    -browser browserName=firefox,maxInstances=1
