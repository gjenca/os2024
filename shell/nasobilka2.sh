#!/bin/bash
for N in $(seq 10)
do
	VYSLEDOK=$(echo "$N*5" | bc)
	echo "$N*5=$VYSLEDOK"
done
