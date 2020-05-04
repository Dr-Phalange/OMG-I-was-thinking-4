import string
import random
import re

print("Hi, what is your name?")
name = input()
if name == "":
    print("Okay Nameless, I am thinking of a letter")
else:
    print("Well " + name + " I am thinking of a letter")
    
secretLetter = random.choice(string.ascii_letters).lower()

for guessesTaken in range(1, 6):
  print("Take a guess!")
  guess = input().lower()
  
  if not re.match("^[a-z]*$", guess):
    print ("ONLY LETTERS ALLOWED! Please enter a letter.")
  elif guess == "":
    print ("Please enter a letter to continue.")
  elif guess < secretLetter:
    print("Your guess is too low.")
  elif guess > secretLetter:
      print("Your guess is too high.")
  else:
        break
   
if guess == secretLetter:
    print("Good job, " + name + "! You guessed my letter in " + str(guessesTaken) + " guesses")
else:
    print("Nope. The number I was thinking of was " + secretLetter)
