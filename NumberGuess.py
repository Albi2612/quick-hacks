print("Welcome to Python Number Guessing Game!")

import random

def game(lowest_number, highest_number):
    answer = random.randint(lowest_number, highest_number)
    guesses = 0
    is_running = True

    while is_running:
        try:
            user_input = int(input(f"Guess a random number between {lowest_number} and {highest_number}=\n"))

            if user_input>highest_number or user_input<lowest_number:
                print("Invalid input(Input out of range)\n"
                        f"Guess a random number between {lowest_number} and {highest_number}")
            elif user_input>answer:
                print("Greater than...")
                guesses+=1
            elif user_input<answer:
                print("Less than...")
                guesses+=1
            elif user_input==answer:
                guesses+=1
                print("Correct!🎉")
                print(f"Number of guesses = {guesses}")
                is_running = False
            else:
                print("Error!!")
        except:
            print("Enter a valid number!")

def main():
     #We are defining the range of the number
     lowest_number = 1
     highest_number = 10
     game(lowest_number, highest_number)

if __name__=='__main__':
    main()