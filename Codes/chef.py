import os

# File paths
data_folder = "data"
orders_file = os.path.join(data_folder, "orders.txt")
ingredients_requests_file = os.path.join(data_folder, "ingredient_requests.txt")
users_file = os.path.join(data_folder, "users.txt")

# Ensure data folder exists
if not os.path.exists(data_folder):
    os.makedirs(data_folder)


def chef_menu(username):
    while True:
        print("\n--------------------------------------------------")
        print(f"    Chef Menu (Logged in as {username})    ")
        print("--------------------------------------------------")
        print("1. View Orders")
        print("2. Update Order Status")
        print("3. Request Ingredients")
        print("4. Update Profile")
        print("5. Logout")
        print("-" * 50)

        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_orders()
        elif choice == "2":
            update_order_status()
        elif choice == "3":
            request_ingredients()
        elif choice == "4":
            update_profile(username)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Please try again.")


def view_orders():
    if not os.path.exists(orders_file) or os.stat(orders_file).st_size == 0:
        print("No orders found.")
        return

    print("\n----- Current Orders -----")
    with open(orders_file, "r") as file:
        for line in file:
            user, item, quantity = line.strip().split(",")
            print(f"Order: {quantity}x {item} for {user}")
    print("\n")


def update_order_status():
    if not os.path.exists(orders_file) or os.stat(orders_file).st_size == 0:
        print("No orders found.")
        return

    order_id = input("Enter the order ID to update the status: ")
    
    try:
        order_id = int(order_id)
    except ValueError:
        print("Invalid Order ID.")
        return

    # Reading the orders file
    with open(orders_file, "r") as file:
        orders = file.readlines()

    if order_id <= 0 or order_id > len(orders):
        print("Invalid order ID.")
        return

    # Updating the order status
    print("Enter new order status (e.g., 'Preparing', 'Ready'):")
    status = input("New status: ")
    orders[order_id - 1] = orders[order_id - 1].strip() + f" | Status: {status}\n"
    
    with open(orders_file, "w") as file:
        file.writelines(orders)

    print("Order status updated successfully!")


def request_ingredients():
    ingredient = input("Enter the ingredient you want to request: ")
    quantity = input("Enter the quantity: ")

    # Save the request to a file
    with open(ingredients_requests_file, "a") as file:
        file.write(f"{ingredient},{quantity}\n")

    print(f"Ingredient request for {quantity}x {ingredient} has been submitted.")


def update_profile(username):
    print(f"Updating profile for {username}...")
    new_username = input("Enter new username (or press Enter to keep current): ") or username
    new_password = input("Enter new password (or press Enter to keep current): ")

    # Read the users file to update the details
    with open(users_file, "r") as file:
        lines = file.readlines()

    with open(users_file, "w") as file:
        for line in lines:
            user, password, role = line.strip().split(",")
            if user == username:
                if new_username != username:
                    line = f"{new_username},{new_password if new_password else password},{role}\n"
                else:
                    line = f"{username},{new_password if new_password else password},{role}\n"
            file.write(line)

    print("Profile updated successfully!")
