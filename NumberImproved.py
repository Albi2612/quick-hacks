import random

def get_user_guess(lowest, highest):
    while True:
        try:
            guess = int(input(f"Guess a number between {lowest} and {highest}: "))
            if lowest <= guess <= highest:
                return guess
            else:
                print(f"Out of range! Please enter a number between {lowest} and {highest}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def play_game(lowest_number, highest_number):
    answer = random.randint(lowest_number, highest_number)
    guesses = 0

    while True:
        user_guess = get_user_guess(lowest_number, highest_number)
        guesses += 1

        if user_guess < answer:
            print("Too low! Try again.")
        elif user_guess > answer:
            print("Too high! Try again.")
        else:
            print(f"Correct! 🎉 The number was {answer}.")
            print(f"You guessed it in {guesses} tries.")
            break

def main():
    print("🎮 Welcome to the Python Number Guessing Game!")
    lowest_number = 1
    highest_number = 10

    while True:
        play_game(lowest_number, highest_number)
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == '__main__':
    main()
