#!/bin/bash
VYRAZ="0"
while read NUM
do
	VYRAZ="$VYRAZ+$NUM"
done
echo "$VYRAZ" | bc

