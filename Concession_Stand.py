#In this program we are going to create a concession stand

menu = {"Biryani" : 100,
        "Fried Rice" : 80,
        "Coke" : 25,
        "Water" : 20}

cart = []

total = 0

print(f"{'*'*7}MENU{'*'*7}")
for i, (key, value) in enumerate(menu.items(),start=1):
    print(f"{i}.{key:12}: ₹{value}")
print(f"{'*'*7}MENU{'*'*7}")

while True:
    food = input("Enter the item you want to choose\n"
                 "(Press 'Q' to quit):").capitalize()

    if food == 'Q':
        print("Thank you for shopping with us!")
        break
    elif food in menu:
        cart.append(food)
        total += menu[food]
        print(f"You have added {food}.")
    else:
        print("Choose an item from the menu.")


print(f"{'*'*7}YOUR ORDER{'*'*7}")
for i, item in enumerate(cart, start=1):
    print(f"{i}. {item}: ₹{menu[item]}")

print(f"TOTAL BILL = ₹{total}")

print("Enjoy your meal!!😋")