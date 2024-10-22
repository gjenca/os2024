#!/usr/bin/env bash
N=100
for K in $(seq 2 "$N")
do
	POLOVICA=$(echo "$K/2" | bc)
	JEPRVOCISLO="ano"
	for D in $(seq 2 "$POLOVICA")
	do
		if [ $(echo "$K%$D" | bc) = 0 ]
		then
			# echo "$K" nie je prvocislo
			JEPRVOCISLO="nie"
			break
		fi
	done
	if test "$JEPRVOCISLO" = "ano"
	then
		echo "$K" je prvocislo
	fi
done

