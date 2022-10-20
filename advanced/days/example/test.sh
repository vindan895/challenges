#!/bin/bash

for solution in solutions/*/*.py; do
	filename=$(basename -- "$solution")
	extension="${filename##*.}"
	filename="${filename%.*}"
	python3 $solution > $solution.output

	if [[ -n $(diff $solution.output ./answer.txt) ]]; then
		echo FAIL - $filename >> ./leaderboard.txt
	else
		echo SUCCESS - $filename >> ./leaderboard.txt
	fi
done

