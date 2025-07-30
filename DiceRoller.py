print("Welcome to Python dice roller program")

import random

dice_faces = {
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

dice = []
total = 0

try:
    user_input = int(input("Enter the number of dice you want to roll:"))

    for die in range(user_input):
        dice.append(random.randint(1, 6))

    for die in dice:
        for line in dice_faces[die]:
            print(line)

    for die in dice:
        total+=die

    print(f"Total = {total}")

except ValueError:
    print("Please enter in number format!")

