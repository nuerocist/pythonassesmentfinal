import easygui 
import matplotlib.pyplot as plt 

# Dictionary of store items with their prices
store_items = {
    "apple": 1.50,
    "banana": 0.90,
    "bread": 2.50,
    "milk": 3.00,
    "eggs": 2.20,
    "cheese": 4.50,
    "orange": 1.20,
    "chocolate": 2.80
}

cart = {} 

def plot_cart(cart):
    # Function to plot a bar chart of items and their quantities in the cart
    items = [item.title() for item in cart.keys()]  
    quantities = list(cart.values())  
    plt.figure(figsize=(10, 6))  
    plt.bar(items, quantities, color='skyblue')  # Create bar chart
    plt.xlabel('Items')  # Label x-axis
    plt.ylabel('Quantity')  # Label y-axis
    plt.title('Shopping Cart Items and Quantities')  # Chart title
    plt.grid(axis='y')  
    plt.tight_layout()  
    plt.show()  # Display the plot

shopping = True 
while shopping:
    # Prompt user to start shopping
    start = easygui.buttonbox("Do you want to start shopping?", "Welcome", choices=["Yes", "No"])
    if start != "Yes":
        easygui.msgbox("Goodbye!", "Exit")  
        shopping = False
        break

    # Show current cart contents or empty message
    if not cart:
        easygui.msgbox("Your cart is currently empty.", "Cart")
    else:
        cart_text = "\n".join([f"- {item.title()} x{qty}" for item, qty in cart.items()])
        easygui.msgbox(f"Your Cart:\n{cart_text}", "Cart")

    # Ask if user wants to buy an item
    buy = easygui.buttonbox("Would you like to buy an item?", "Buy", choices=["Yes", "No"])
    if buy != "Yes":
        easygui.msgbox("Thank you for visiting!", "Exit") 
        shopping = False
        break

    # Loop for buying items
    while True:
        # Show available items and prices
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

        # Get quantity from user
        qty = easygui.integerbox(f"Enter quantity for {item.title()}:", "Quantity", lowerbound=1)
        if qty is None:
            continue 

        # Add item and quantity to cart
        cart[item] = cart.get(item, 0) + qty
        easygui.msgbox(f"Added {qty} {item}(s) to cart.", "Added")

        # Ask if user wants to buy more items
        more = easygui.buttonbox("Buy more items?", "Continue", choices=["Yes", "No"])
        if more != "Yes":
            break

    # If cart is empty after buying loop, exit
    if not cart:
        easygui.msgbox("Your cart is empty. Goodbye!", "Exit")
        shopping = False
        break

    # Calculate subtotal and show cart summary
    subtotal = 0
    cart_summary = ""
    for item, qty in cart.items():
        price = store_items[item] * qty
        subtotal += price
        cart_summary += f"- {item.title()} x{qty}: ${price:.2f}\n"
    cart_summary += f"\nSubtotal: ${subtotal:.2f}"
    easygui.msgbox(f"Your Cart:\n{cart_summary}", "Cart Summary")

    # Ask if user wants to continue shopping
    cont = easygui.buttonbox("Would you like to continue shopping?", "Continue", choices=["Yes", "No"])
    if cont != "Yes":
        shopping = False

# Show the graph at the very end, if the cart is not empty
if cart:
    plot_cart(cart)
easygui.msgbox("Thank you for shopping! Goodbye!", "Exit")
