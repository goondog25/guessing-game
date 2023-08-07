#Importing the neccessary module to generate random numbers. Then storing in variable.
import random
random_number = random.randint(1, 100)

#Opening message with reusable prompt variable
print("Welcome to a generic python guessing game!")

prompt = "\nPlease enter a number between 1 and 100 to guess: "

#Setting counter at 0 to track the ammount of tries it takes to guess correctly.
counter = 0

#Empty string to allow while loop to start
guess = ""

#While loop to keep running until the number is guessed correctly. Displaying whether the guess was too high or too low.
while guess != random_number:
  guess = input(prompt)
  guess = int(guess)

  if guess < random_number:
    print("Sorry you guessed to low. Try again.")
  elif guess > random_number:
    print("Sorry you guessed to high. Try again.")

  #Counter that adds 1 for every incorrect guess.
  counter += 1

print(f"\nCongrats you guessed correctly! The correct number was {random_number}.")
print(f"\nIt took you {counter} tries to guess it!")
