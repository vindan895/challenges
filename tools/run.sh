#!/bin/bash

for day in advanced/days/*; do
    cd $day && ./test.sh && echo $day
done
