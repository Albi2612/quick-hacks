#!/usr/bin/env python3
"""
Concession Stand Management System
A simple command-line program for ordering food items from a concession stand.

Features:
- Display menu with items and prices
- Add items to cart
- Calculate total bill
- Show order summary

Author: [Your Name]
Date: [Current Date]
Version: 2.0
"""


class ConcessionStand:
    """A simple concession stand ordering system."""

    def __init__(self):
        """Initialize the concession stand with menu items and empty cart."""
        self.menu = {
            "Biryani": 100,
            "Fried Rice": 80,
            "Coke": 25,
            "Water": 20
        }
        self.cart = []
        self.total = 0

    def display_menu(self):
        """Display the menu in a formatted way."""
        print(f"\n{'=' * 20}")
        print(f"{'MENU':^20}")
        print(f"{'=' * 20}")

        for i, (item, price) in enumerate(self.menu.items(), start=1):
            print(f"{i}. {item:<12}: ₹{price}")

        print(f"{'=' * 20}\n")

    def add_item_to_cart(self, item_name):
        """
        Add an item to the cart if it exists in the menu.

        Args:
            item_name (str): Name of the item to add

        Returns:
            bool: True if item was added successfully, False otherwise
        """
        if item_name in self.menu:
            self.cart.append(item_name)
            self.total += self.menu[item_name]
            print(f"✓ Added {item_name} to your cart (₹{self.menu[item_name]})")
            return True
        else:
            print("❌ Item not found. Please choose from the menu.")
            return False

    def display_cart(self):
        """Display the current cart contents and total."""
        if not self.cart:
            print("Your cart is empty.")
            return

        print(f"\n{'=' * 25}")
        print(f"{'YOUR ORDER':^25}")
        print(f"{'=' * 25}")

        for i, item in enumerate(self.cart, start=1):
            print(f"{i}. {item:<12}: ₹{self.menu[item]}")

        print(f"{'=' * 25}")
        print(f"{'TOTAL BILL':<12}: ₹{self.total}")
        print(f"{'=' * 25}")

    def get_user_input(self):
        """
        Get user input for item selection.

        Returns:
            str: User's choice (capitalized) or 'Q' to quit
        """
        choice = input("\nEnter the item name you want to order\n"
                       "(or press 'Q' to checkout): ").strip().title()
        return choice

    def run(self):
        """Main program loop."""
        print("🍽️  Welcome to the Concession Stand! 🍽️")
        self.display_menu()  # Display menu only once at the start

        while True:
            choice = self.get_user_input()

            if choice.upper() == 'Q':
                break
            elif choice in self.menu:
                self.add_item_to_cart(choice)
            else:
                print("❌ Please choose a valid item from the menu.")

        # Display final order and checkout
        print("\n🛒 Checkout Summary:")
        self.display_cart()

        if self.cart:
            print("\n🎉 Thank you for your order!")
            print("Enjoy your meal! 😋")
        else:
            print("\n👋 Thank you for visiting!")


def main():
    """Main function to run the concession stand program."""
    try:
        stand = ConcessionStand()
        stand.run()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try again.")


if __name__ == "__main__":
    main()