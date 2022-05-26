#!/bin/bash

DATE=$(date +%m-%d_%H:%M)
#MONITOR="xps15"
MONITOR="vert"
NUMBER=2

# -t l : LCD
# -v : verbose
# -H : high resolution mode
# -Q 2012_2 : observer

COMMAND="dispcal -d $NUMBER -v -w 0.3127,0.3290 -Ibw -H -P 0.5,0.5,2.0 -o ${MONITOR}-spec-${DATE}"

echo $COMMAND
echo "good?"
read
$COMMAND