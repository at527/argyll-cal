#!/bin/bash

# DATE=$(date +%m-%d_%T)
DATE=$(date +%m-%d_%H:%M)

# -t l : LCD
# -v : verbose
# -H : high resolution mode
# -o 2012_2 : observer
# -P 0.5,0.5,2.0 : position, sizey


ccxxmake -t l -v -H -P 0.5,0.5,2.0 dpt94-$DATE.ccmx
