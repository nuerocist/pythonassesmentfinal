store_items = {
    "apple": 1.50,
    "banana": 0.90,
    "bread": 2.50
}
cart = {}

# Main shopping loop
while True:
    start = input("Do you want to start shopping? (yes/no): ").lower()
    if start != 'yes':
        print("Goodbye!")
        break

    if not cart:
        print("Your cart is currently empty.")
    else:
        print("Your Cart:")
        for item, qty in cart.items():
            print(f"- {item.title()} x{qty}")
    # Show available items
    print("\nAvailable items:")
    for item, price in store_items.items():
        print(f"- {item.title()} (${price:.2f})")

    buy = input("Would you like to buy an item? (yes/no): ").lower()
    if buy != 'yes':
        print("Thank you for visiting!")
        break
        
    while True:
        item = input("Enter item name to buy (or 'no' to stop): ").lower()
        if item == 'no':
            break
        if item not in store_items:
            print("Item not found.")
            continue
        qty = input("Enter quantity: ")
        if not qty.isdigit() or int(qty) <= 0:
            print("Invalid quantity.")
            continue
        qty = int(qty)
        cart[item] = cart.get(item, 0) + qty
        print(f"Added {qty} {item}(s) to cart.")
        more = input("Buy more items? (yes/no): ").lower()
        if more != 'yes':
            break

    if not cart:
        print("Your cart is empty. Goodbye!")
        break
        # Calculate subtotal and show cart summary
    print("\nYour Cart:")
    subtotal = 0
    for item, qty in cart.items():
        price = store_items[item] * qty
        subtotal += price
        print(f"- {item.title()} x{qty}: ${price:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")

    cont = input("\nWould you like to continue shopping? (yes/no): ").lower()
    if cont != 'yes':
        print("Thank you for shopping! Goodbye!")
        break
