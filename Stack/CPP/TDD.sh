#!/bin/bash


set -e # exit on the first error with an error
# set -eo pipefail # exit on the first error even in a pipeline
# set -u
# set -x

#compile the file
g++ test_*.cpp -std=c++0x -Wpedantic


# take all the input tests iterate through them
for i in *.in
do
  # Take the filename without the extension
  filename="${i%.*}"

  # Differ the output expected with the output of the program.
  diff -u $filename.out <(./a.out < $filename.in)
done
