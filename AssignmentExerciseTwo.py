# Simple Inventory Management Program

# Initial inventory (item: quantity)
inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Oranges": 20
}

while True:
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity} in stock")

    print("\nOptions:")
    print("1. Update item stock")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        item_name = input("Enter the item name: ").title()
        if item_name in inventory:
            new_quantity = int(input(f"Enter new quantity for {item_name}: "))
            inventory[item_name] = new_quantity
            print(f"{item_name} stock updated.")
        else:
            print("Item not found in inventory.")
    elif choice == "2":
        print("Exiting Inventory Management.")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")
