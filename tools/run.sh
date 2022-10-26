#!/bin/bash

home="$PWD"

for day in advanced/days/*/; do
    cd $day && ./test.sh && echo "Finished leaderboard: $day" && cd $home
done
