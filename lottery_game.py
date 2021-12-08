import random

def main_game():
    winning_number1 = False 
    winning_number2 = False
    winning_number3 = False

    lotto_number1 = random.randint(0,9) 
    lotto_number2 = random.randint(0,9)
    lotto_number3 = random.randint(0,9)

    number1 = int(input("First lucky number between 0 to 9: "))
    number2 = int(input("Second lucky number between 0 to 9: "))
    number3 = int(input("Third lucky number between 0 to 9: "))

    if number1 == lotto_number1 or number1 == lotto_number2 or number1 == lotto_number3:
        winning_number1 = True 
    if number2 == lotto_number1 or number2 == lotto_number2 or number2 == lotto_number3:
        winning_number2 = True 
    if number3 == lotto_number1 or number3 == lotto_number2 or number3 == lotto_number3:
        winning_number3 = True 
    if winning_number1 == True and winning_number2 == True and winning_number3 == True:
        print("Winner!")
    else:
        print("You loss.")
        
    print("Your numbers are: ", number1, number2, number3)
    print("The lottery numbers are: ", lotto_number1, lotto_number2, lotto_number3)

def again():
    if input("Try again?(y/n) ") == 'y':
        main_game()
    else:
        exit

main_game()
again()
