#! bin/zsh

# set -e
# set -u
# set -x

#compile the file
gpp test_*.cpp


# take all the input tests iterate through them
for i in *.in
do
  # Take the filename without the extension
  filename="${i%.*}"

  # Differ the output expected with the output of the program.
  diff -u $i.out <(./a.out < $i.in)
done
