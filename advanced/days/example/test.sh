#!/bin/bash

> ./leaderboard.txt

for solution in solutions/*/*.py; do
	filename=$(basename -- "$solution")
	extension="${filename##*.}"
	filename="${filename%.*}"
	python3 $solution > $solution.output

	if [[ -n $(diff $solution.output ./answer.txt) ]]; then
		echo ❌ - $filename >> ./leaderboard.txt
	else
		echo ✅ - $filename >> ./leaderboard.txt
	fi
done
