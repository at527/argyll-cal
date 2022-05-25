#!/bin/bash

DATE=$(date +%m-%d_%H:%M)

# -t l : LCD
# -v : verbose
# -H : high resolution mode
# -Q 2012_2 : observer

dispcal -v -w 0.3127,0.3290 -Ibw -H -P 0.5,0.5,2.0 -o xps15-spec-$DATE