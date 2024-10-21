#!/bin/bash
VYRAZ="0"
while [ "$#" != 0 ]
do
	VYRAZ="$VYRAZ+$1"
	shift
done
echo "$VYRAZ" | bc

