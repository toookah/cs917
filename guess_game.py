"""
This program is a simple guessing game
"""
#Import the random integer function
from random import randint

#Setup a random number
random_number=randint(1,5)
#get the first guess
print("I'm thinking of a number,can you guess what it is?")
first_guess=int(input())
if first_guess==random_number:
  print("Well done. The number is "+str(first_guess))
elif first_guess<random_number:
  print("Too Low! Guess again.")
else:
  print("Too High! Guess again.")
#Loop while the guess is not the same as the matching number
flag=True
while flag:
  guess=int(input())
  if guess==random_number:
    print("Well done. The number is "+str(first_guess))
    flag=False
  elif guess<random_number:
    print("Too Low! Guess again.")
  else:
    print("Too High! Guess again.")




#print "Well done. The number was " + str(random_number)