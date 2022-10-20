#!/bin/bash

for solution in solutions/*/*.py; do
	python3 $solution > $solution.output

	if [[ -n $(diff $solution.output ./answer.txt) ]]; then
		echo FAIL - $solution
	else
		echo SUCCESS - $solution
	fi
done

