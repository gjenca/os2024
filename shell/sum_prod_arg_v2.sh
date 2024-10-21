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
for ARG in "$@"
do
	VYRAZ="$VYRAZ$OPER$ARG"
done
echo "$VYRAZ" | bc

