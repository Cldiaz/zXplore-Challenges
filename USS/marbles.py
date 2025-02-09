#!/usr/bin/env python3

marbles = 10  #You start out with 10 marbles
marble_dots = "**********" #Pretend these are ten marbles

while (marbles > 0):
   
   #This prints out how many marbles you have left.
   # We have to say str(marbles) because marbles is a number
   # and we want to use it in a string (letters and other characters)
   print(marble_dots[:marbles])
   print("You have " + str(marbles) + " marbles left.")
   
   if (marbles <= 3):
    print("Warning: You are running low on marbles!!")
   
   #This is another way of saying "Subtract 1 from the marbles variable"
   # It is logically the same as writing "marbles = marbles - 1", just shorter
   marbles -= 1 
   
   # Make a newline, so there's an empty line before the next time we run this loop
   print("")

#This is *NOT* indented, and is therefore not part of the above loop.
#Just sayin'
print("You are all out of marbles")