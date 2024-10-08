#!/bin/bash
for N in $(seq 10)
do
echo "$N*5" | bc
done
