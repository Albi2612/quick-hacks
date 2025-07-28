#Rock paper and scissor in python
import random

print("Welcome to rock, paper and scissors.")

option=("rock","paper","scissor")

computer=random.choice(option)

user=input("Enter rock or paper or scissor: ").lower()

while user not in option:
    print("Invalid input")
    user = input("Enter rock or paper or scissor: ").lower()

print(f"Computer={computer}")
print(f"User={user}")

if computer=="rock" and user=="scissor":
    print("You lose")
elif computer=="paper" and user=="rock":
    print("You lose!")
elif computer=="scissor" and user=="paper":
    print("You Lose!")
elif computer==user:
    print("Draw!")
else:
    print("You win! Hurray!")
