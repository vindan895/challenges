#!/usr/bin/env bash

START="$1"

END=$(($(date +%s%N)/1000000))

echo "$(expr $END - $START)"
