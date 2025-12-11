#!/usr/bin/env bash

infile="$1"
outfile="${2:-$1}"

inside=false
> "$outfile"

while IFS= read -r line; do
    if [[ $line == *'<textarea id="source">'* ]]; then
        echo "<!--" >> "$outfile"
        inside=true
    fi

    echo "$line" >> "$outfile"

    if [[ $line == *'</textarea>'* ]]; then
        echo "-->" >> "$outfile"
        inside=false
    fi
done < "$infile"
