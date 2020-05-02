import random

print("Hi, what is your name?")
name = input()

print("Well " + name + " I am thinking of a number between 1 and 100")
secretNumber = random.randint(1, 100)

for guessesTaken in range(1, 6):
  print("Take a guess!")
  guess = int(input()) #changes input to an integer
  
  if guess < secretNumber:
    print("Your guess is too low.")
  elif guess > secretNumber:
      print("Your guess is too high.")
  else:
        break
   
if guess == secretNumber:
    print("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " guesses")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
