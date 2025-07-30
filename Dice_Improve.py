import random

# ASCII art representation of dice faces
DICE_FACES = {
    1: [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ],
    2: [
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ],
    3: [
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ],
    4: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    5: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    6: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    ]
}


def display_dice_side_by_side(dice_results):
    """Display multiple dice horizontally (side by side)."""
    # For each line of the dice (0 to 4), print all dice on that line
    for line_index in range(5):
        line = ""
        for dice_value in dice_results:
            line += DICE_FACES[dice_value][line_index] + "  "  # Add spacing
        print(line.rstrip())  # Remove trailing spaces
    print()  # Add empty line for better formatting


def get_dice_count():
    """Get valid number of dice from user input."""
    while True:
        try:
            num_dice = int(input("Enter the number of dice you want to roll (1-8): "))
            if num_dice < 1:
                print("Please enter a positive number!")
                continue
            if num_dice > 8:
                print("Maximum 8 dice allowed for better display!")
                continue
            return num_dice
        except ValueError:
            print("Please enter a valid number!")


def main():
    """Main program function."""
    print("🎲 Welcome to Python Dice Roller Program 🎲")
    print("=" * 45)

    try:
        # Get number of dice from user
        num_dice = get_dice_count()

        # Roll the dice and store results
        dice_results = []
        for i in range(num_dice):
            dice_results.append(random.randint(1, 6))

        # Display results
        print(f"\nRolling {num_dice} dice...\n")
        display_dice_side_by_side(dice_results)

        # Show individual results and total
        individual_results = ", ".join(str(die) for die in dice_results)
        total = sum(dice_results)

        print(f"Individual results: [{individual_results}]")
        print(f"Total: {total}")

    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye! 👋")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()