
menu = {
    'pizza': 99,
    'Pasta': 40,
    'Burger': 81,
    'salad': 70,
    'coffee': 80,
}

print("Welcome to Restaurant")
print("pizza: 99 Rs\nPasta: 40 Rs\nBurger: 81 Rs\nsalad: 70 Rs\ncoffee: 80 Rs")

order_total = 0

while True:
    item = input("Enter the item you want to order: ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order")
    else:
        print("Sorry, we don't have that item on the menu")

    another_order = input("Do you want to add another item? (yes/no): ")
    if another_order.lower() != 'yes':
        break

print(f"The total amount to pay is {order_total} Rs")