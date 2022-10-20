for day in days/*; do
	for solution in $day/*/*/*.py; do
		python3 $solution > $solution.output

		if [[ -n $(diff $solution.output $day/answer.txt) ]]; then
			echo FAIL - $solution
		else
			echo SUCCESS - $solution
		fi
	done
done
