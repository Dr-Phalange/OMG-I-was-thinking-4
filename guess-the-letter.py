import string
import random

print("Hi, what is your name?")
name = input()

print("Well " + name + " I am thinking of a letter")
secretLetter = random.choice(string.ascii_letters)

for guessesTaken in range(1, 6):
  print("Take a guess!")
  guess = input()
  
  if guess < secretLetter:
    print("Your guess is too low.")
  elif guess > secretLetter:
      print("Your guess is too high.")
  else:
        break
   
if guess == secretLetter:
    print("Good job, " + name + "! You guessed my letter in " + str(guessesTaken) + " guesses")
else:
    print("Nope. The number I was thinking of was " + secretLetter)
