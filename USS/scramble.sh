input="$1"
count="$2"

if [ $# -ne 2 ]
  then
    printf "Usage Example: ./scramble.sh file.txt 13\n\n"
    printf "This program takes the input from a file (first argument)\n"
    printf "and rotates the letters by a number of positions (second argument)\n"
    printf "If only works for lowercase characters.\n"
    printf "The first argument needs to be a file.\n"
    printf "\nYour task is to figure out the correct number of rotations needed\n"
    printf "to decode the secret message in /z/public/secret.txt. Good luck!\n"
    exit 1
fi
if test -f "$input"; then
    echo "$input exists."
    content=$(cat $input)
else
    echo "File $input does not exist, or is not a file"
    exit 1
fi

content=$(echo $content | tr '[:upper:]' '[:lower:]')
scrambled=$content

abc1="abcdefghijklmnopqrstuvwxyz"
abc2="bcdefghijklmnopqrstuvwxyza"

echo -n "Processing"
for (( c=1; c<=$count; c++ ))
do
    echo -n "."
    scrambled=$(echo $scrambled | tr "$abc1" "$abc2")
done
printf "Done!\n\nOutput:\n"
echo $scrambled
