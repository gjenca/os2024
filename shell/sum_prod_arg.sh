#!/bin/bash
VYRAZ="0"
OPER="+"
while true
do
	if test "$1" = "-m"
	then
		OPER="*"
		VYRAZ="1"
		shift
	else
		break
	fi
done
while [ "$#" != 0 ]
do
	VYRAZ="$VYRAZ$OPER$1"
	shift
done
echo "$VYRAZ" | bc

