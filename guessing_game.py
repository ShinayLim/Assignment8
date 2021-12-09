# Import modules
import random

# Intro
print("Welcome to Dan's number guessing game!\n")

# Define variables
number = random.randint(0, 100)
u_guess = int(input("Have a guess: "))

# Main program loop
while u_guess != number:
    if u_guess == number:
        print("Well done, you win!")
    if u_guess > number:
        print("Your guess was too high.")
        print("Please try again.")
    if u_guess < number:
        print("Your guess was too low.")
        print("Please try again.")
    u_guess = int(input("Have a guess: "))
print("Well done, you win!")
