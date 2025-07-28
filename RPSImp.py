import random
import time
import os


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_title():
    """Print the game title with style"""
    print("=" * 50)
    print("🎮 WELCOME TO ROCK, PAPER, SCISSORS! 🎮")
    print("=" * 50)
    print()


def get_choice_emoji(choice):
    """Return emoji representation of the choice"""
    emojis = {
        'rock': '🪨',
        'paper': '📄',
        'scissors': '✂️'
    }
    return emojis.get(choice, '❓')


def animate_countdown():
    """Animate a countdown before revealing choices"""
    print("Get ready...")
    time.sleep(0.8)

    for i in range(3, 0, -1):
        print(f"\n{i}...")
        time.sleep(0.8)

    print("\nSHOOT! 🎯")
    time.sleep(0.5)


def animate_reveal(computer_choice, user_choice):
    """Animate the reveal of both choices"""
    print("\n" + "=" * 30)
    print("REVEALING CHOICES...")
    print("=" * 30)

    # Show computer choice with animation
    print(f"\nComputer is thinking", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(f"\nComputer chose: {get_choice_emoji(computer_choice)} {computer_choice.upper()}")

    time.sleep(0.8)

    # Show user choice
    print(f"You chose: {get_choice_emoji(user_choice)} {user_choice.upper()}")

    time.sleep(1)


def determine_winner(computer, user):
    """Determine the winner and return result"""
    if computer == user:
        return "draw"
    elif (computer == 'rock' and user == 'paper') or \
            (computer == 'paper' and user == 'scissors') or \
            (computer == 'scissors' and user == 'rock'):
        return "user"
    else:
        return "computer"


def display_result(result):
    """Display the result with animation"""
    print("\n" + "=" * 30)

    if result == "draw":
        print("🤝 IT'S A DRAW! 🤝")
        print("Great minds think alike!")
    elif result == "user":
        print("🎉 YOU WIN! 🎉")
        print("Congratulations! You beat the computer!")
    else:
        print("💻 COMPUTER WINS! 💻")
        print("Better luck next time!")

    print("=" * 30)


def get_user_input():
    """Get and validate user input"""
    options = ("rock", "paper", "scissors")

    while True:
        print("\n🎯 Make your choice:")
        print("1. 🪨 Rock")
        print("2. 📄 Paper")
        print("3. ✂️  Scissors")

        choice = input("\nEnter your choice (rock/paper/scissors or 1/2/3): ").lower().strip()

        # Handle numeric input
        if choice == '1':
            choice = 'rock'
        elif choice == '2':
            choice = 'paper'
        elif choice == '3':
            choice = 'scissors'

        if choice in options:
            return choice
        else:
            print("❌ Invalid choice! Please try again.")
            time.sleep(1)


def play_again():
    """Ask if user wants to play again"""
    while True:
        choice = input("\n🔄 Do you want to play again? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")


def display_stats(wins, losses, draws):
    """Display game statistics"""
    total_games = wins + losses + draws
    if total_games > 0:
        print(f"\n📊 GAME STATISTICS 📊")
        print(f"Games played: {total_games}")
        print(f"Wins: {wins} ({wins / total_games * 100:.1f}%)")
        print(f"Losses: {losses} ({losses / total_games * 100:.1f}%)")
        print(f"Draws: {draws} ({draws / total_games * 100:.1f}%)")


def main():
    """Main game function"""
    options = ("rock", "paper", "scissors")
    wins = losses = draws = 0

    clear_screen()
    print_title()

    print("🎲 Rules:")
    print("• Rock crushes Scissors")
    print("• Paper covers Rock")
    print("• Scissors cuts Paper")
    print("\nLet's play! 🚀")

    while True:
        # Get user choice
        user_choice = get_user_input()

        # Computer makes choice
        computer_choice = random.choice(options)

        # Animate countdown
        animate_countdown()

        # Animate reveal
        animate_reveal(computer_choice, user_choice)

        # Determine winner
        result = determine_winner(computer_choice, user_choice)

        # Update statistics
        if result == "user":
            wins += 1
        elif result == "computer":
            losses += 1
        else:
            draws += 1

        # Display result
        display_result(result)

        # Show current stats
        display_stats(wins, losses, draws)

        # Ask to play again
        if not play_again():
            break

        clear_screen()
        print_title()

    # Final goodbye
    print("\n👋 Thanks for playing!")
    print("See you next time! 🎮")
    display_stats(wins, losses, draws)


if __name__ == "__main__":
    main()