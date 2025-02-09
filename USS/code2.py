#!/usr/bin/env python3

#Here is where we are setting our variables.
#Remember in algebra class how you might say x = 5?
#It's just like that.
the_letter = "z"
the_word = "pumplin"

#This could have been written as   if "z" in "racecar" but
# by using variables, it makes it so we don't have to change
# the actual code below when we want to try out different
# letters and words.
if the_letter in the_word:
  print("Yes! The letter " + the_letter + " is in the word " + the_word)
else:
  print("Nope. The letter " + the_letter + " is NOT in the word " + the_word)
