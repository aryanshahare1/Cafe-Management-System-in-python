# Define the menu of the restaurant
menu = {
    "pizza": 150,
    "burger": 100,
    "pasta": 120,
    "salad": 90,
    "french fries": 90,
    "maggie": 60,
    "nachos": 80,
    "sandwich": 100,
    "coffee": 80,
    "chocolate shake": 100,
    "mohito": 120,
    "cold coffee": 120,
    "tea": 50
}

# Greet the customer
print("WELCOME TO PYTHON RESTAURANT")
print("\nHere's our menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: {price} Rs")

order_total = 0
ordered_items = []

# Ordering process
while True:
    item = input("\nEnter the name of the item you want to order: ").lower()  # Convert input to lowercase
    if item in menu:
        try:
            quantity = int(input(f"How many {item.capitalize()} would you like to order? "))
            if quantity <= 0:
                print("Quantity must be greater than zero!")
                continue
        except ValueError:
            print("Please enter a valid number for quantity!")
            continue

        order_total += menu[item] * quantity
        ordered_items.append((item, quantity))
        print(f"{quantity} x {item.capitalize()} has been added to your order.")
    else:
        print(f"Sorry, {item.capitalize()} is not available.")
    
    another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if another_order != 'yes':
        break

# Option to remove an item
remove_item = input("Do you want to remove an item from your order? (Yes/No): ").strip().lower()
if remove_item == 'yes':
    item_to_remove = input("Enter the item to remove: ").lower()
    for ordered_item, quantity in ordered_items:
        if item_to_remove == ordered_item:
            ordered_items.remove((ordered_item, quantity))
            order_total -= menu[ordered_item] * quantity
            print(f"{ordered_item.capitalize()} has been removed from your order.")
            break
    else:
        print(f"{item_to_remove.capitalize()} is not in your order.")

# Apply discount if applicable
if order_total > 500:
    discount = order_total * 0.10
    print(f"Congratulations! You've received a 10% discount of {discount} Rs.")
    order_total -= discount

# Final order summary
if ordered_items:
    print("\n--- Bill Summary ---")
    for ordered_item, quantity in ordered_items:
        print(f"{quantity} x {ordered_item.capitalize()}: {menu[ordered_item] * quantity} Rs")
    print(f"\nTotal Amount: {order_total} Rs")

    # Payment method
    payment_method = input("\nHow would you like to pay? (Cash/Card/Online): ").strip().lower()
    print(f"\nPayment received via {payment_method.capitalize()}. Thank you!")
else:
    print("\nYou haven't ordered anything.")

# Save the order to a file
with open("order_receipt.txt", "w") as file:
    file.write("--- Bill Summary ---\n")
    for ordered_item, quantity in ordered_items:
        file.write(f"{quantity} x {ordered_item.capitalize()}: {menu[ordered_item] * quantity} Rs\n")
    file.write(f"\nTotal Amount: {order_total} Rs\n")
    file.write(f"Payment method: {payment_method.capitalize()}\n")
    file.write("Thank you for dining with us!")
