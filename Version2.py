import easygui

store_items = {
    "apple": 1.50,
    "banana": 0.90,
    "bread": 2.50
}
cart = {}

while True:
    # Start shopping prompt
    start = easygui.buttonbox("Do you want to start shopping?", "Welcome", choices=["Yes", "No"])
    if start != "Yes":
        easygui.msgbox("Goodbye!", "Exit")
        break

    # Show cart
    if not cart:
        easygui.msgbox("Your cart is currently empty.", "Cart")
    else:
        cart_text = "\n".join([f"- {item.title()} x{qty}" for item, qty in cart.items()])
        easygui.msgbox(f"Your Cart:\n{cart_text}", "Cart")

    # Buy prompt
    buy = easygui.buttonbox("Would you like to buy an item?", "Buy", choices=["Yes", "No"])
    if buy != "Yes":
        easygui.msgbox("Thank you for visiting!", "Exit")
        break

    # Item buying loop
    while True:
        items_text = "\n".join([f"- {item.title()} (${price:.2f})" for item, price in store_items.items()])
        item = easygui.enterbox(
            f"Available items:\n{items_text}\n\nType the item name to buy (or type 'no' to stop):",
            "Buy Item"
        )
        if not item or item.lower() == "no":
            break
        item = item.lower()
        if item not in store_items:
            easygui.msgbox("Item not found. Please type the name exactly as shown.", "Error")
            continue

        qty = easygui.integerbox(f"Enter quantity for {item.title()}:", "Quantity", lowerbound=1)
        if qty is None:
            continue

        cart[item] = cart.get(item, 0) + qty
        easygui.msgbox(f"Added {qty} {item}(s) to cart.", "Added")

        more = easygui.buttonbox("Buy more items?", "Continue", choices=["Yes", "No"])
        if more != "Yes":
            break

    # If cart is empty after shopping loop
    if not cart:
        easygui.msgbox("Your cart is empty. Goodbye!", "Exit")
        break

    # Show cart and subtotal
    subtotal = 0
    cart_summary = ""
    for item, qty in cart.items():
        price = store_items[item] * qty
        subtotal += price
        cart_summary += f"- {item.title()} x{qty}: ${price:.2f}\n"
    cart_summary += f"\nSubtotal: ${subtotal:.2f}"
    easygui.msgbox(f"Your Cart:\n{cart_summary}", "Cart Summary")

    # Continue shopping prompt
    cont = easygui.buttonbox("Would you like to continue shopping?", "Continue", choices=["Yes", "No"])
    if cont != "Yes":
        easygui.msgbox("Thank you for shopping! Goodbye!", "Exit")
        break
