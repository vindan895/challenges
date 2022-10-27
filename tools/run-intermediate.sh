#!/bin/bash

home="$PWD"

for day in intermediate/days/*/; do
    cd $day && ./test.sh && echo "Finished leaderboard: $day" && cd $home
done
