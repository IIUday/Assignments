#!/bin/bash

# URL of the NAV data
url="https://www.amfiindia.com/spages/NAVAll.txt"

# Output file
output_file="nav_data.tsv"

# Download, filter, and extract fields
curl -s "$url" | awk -F ';' '
    BEGIN {
        print "Scheme Name\tNet Asset Value" > "'"$output_file"'"
    }
    /^[0-9]+;/ {
        print $4 "\t" $5 >> "'"$output_file"'"
    }
'

echo "Saved Scheme Name and NAV to $output_file"

