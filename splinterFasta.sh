#!/bin/bash

# Splinter a fasta file into an individual fasta file for each sequence that it contains

# ./splinterFasta.sh -f <fasta>

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -f|--fasta) fasta="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

cat $fasta | awk '{
        if (substr($0, 1, 1)==">") {filename=(substr($0,2) ".fa")}
        print $0 > filename
}'
