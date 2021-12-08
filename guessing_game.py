import random

number = random.randint(0, 100)

user_name = (input("Enter your name: "))
user_name = user_name.strip()

print(f"Hello!" + user_name)
print("Would you like to continue to the game?")
print("1.) Yes")
print("2.) No")

option = input("Select your option: ")
option = int(option)

if option ==1:
    print("You have to guess the number that is between 0 to 100 correctly.")

    guess = input("Enter your guessed number [0-100]: ")
    guess = int(guess)

    if guess > number:
        print("Guess greater than that number...")
    if guess < number:
        print("Guess lower than that number...")

    if guess == number:
        print("You won!")

elif option == 2:
    print("Thank you!")