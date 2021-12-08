import random

number = random.randint(0, 100)
tries = 0

user_name = (input("Enter your name: "))
user_name = user_name.strip()

print(f"Hello!" + user_name)
print("Would you like to continue to the game?")
print("1.) Yes")
print("2.) No")

option = input("Select your option: ")
option = int(option)

if option ==1:
    print("You have to guess the number that is between 0 to 100")
    print("You only have three(3) tries")