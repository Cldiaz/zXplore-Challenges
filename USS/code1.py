#!/usr/bin/env python3

# Here, we're importing a few modules. 
# We're using datetime so we can tell what time it is.
# We're using time so we can use "sleep" 
# We're using getpass to get your userid
from datetime import datetime
import time
import getpass

#This is a typical print message
#Wherever we put \n, there will be an extra newline, which
#can be helpful for formatting and making things look nice.
print("Welcome to the CODE challenge!\n")

#Set "my_number" to 5
my_number = 5

#Keep doing everything indented below as long as "my_number" is greater than 0
while (my_number > 0):
   
   #set the variable "now" to the current time
   now = datetime.now()
   
   #format the variable "the_time" so it shows the hour, minute, and seconds of the current time
   the_time = now.strftime("%H:%M:%S")
   
   #print out the current time in the format of "the_time"
   #Notice how we combined literal text ("The current time is") with "the_time"
   #by sticking a plus sign between them like that. 
   print("The current time is " + the_time)
   
   #subtract 1 from "my_number"
   my_number = my_number - 1
   
   #Take a 1-second nap
   time.sleep(1)

#We stopped indenting because what happens here is outside of
#the "while" loop above. Anything here and below will only happen
#AFTER the loop is done looping five times. 

#This line of code sets the variable "your_userid" to your userid
your_userid = getpass.getuser()

#This prints a special message to you, using your userid
print("We hope you have fun in this challenge, " + your_userid)

#Setting another new variable to zero for reasons we'll see in a little bit.
total_number = 0  #Comments can also go AFTER code, btw

#This is a different type of loop. It says "do this for every something in something else"
#In this case, it says "For every character in the userid, do the following"
for char in your_userid: 
  if (char.isnumeric()): #If the character is a number
    total_number = total_number + int(char) #treat it like a number, and add it to total_number

#... and then print out a nice message letting you know the sum of all the numbers in your userid. 
print("By the way, if you add up all the numbers in your userid, you get " + str(total_number) + "\nThat's pretty neat, right?")
