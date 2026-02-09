import os

# File paths
data_folder = "data"
menu_file = os.path.join(data_folder, "menu.txt")
orders_file = os.path.join(data_folder, "orders.txt")
feedback_file = os.path.join(data_folder, "feedback.txt")
users_file = os.path.join(data_folder, "users.txt")
sales_report_file = os.path.join(data_folder, "sales_report.txt")

# Ensure data folder exists
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

def customer_menu(username):
    while True:
        print("\n--------------------------------------------------")
        print(f"      Customer Menu (Logged in as {username})    ")
        print("--------------------------------------------------")
        print("1. View & Order Food")
        print("2. View Order Status")
        print("3. Send Feedback")
        print("4. Update Profile")
        print("5. Logout")
        print("--------------------------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            order_food(username)
        elif choice == "2":
            view_order_status(username)
        elif choice == "3":
            send_feedback(username)
        elif choice == "4":
            update_profile(username)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Please try again.")

def order_food(username):
    if os.stat(menu_file).st_size == 0:
        print("The menu is empty.")
        return

    menu = load_menu()  # Get the loaded menu

    if not menu:
        print("No menu items found.")
        return

    view_menu(menu)  # Display the menu with numbers

    total_amount = 0
    while True:
        try:
            choice = input("\nEnter the number of the food item you want to order (or type 'done' to finish): ")

            if choice.lower() == 'done':  # Exit the order loop
                break

            item_number = int(choice)

            if 1 <= item_number <= len(menu):
                item_name, price = list(menu.items())[item_number - 1]
                quantity = int(input(f"Enter quantity for {item_name}: "))
                total_amount += price * quantity

                print(f"Added {quantity}x {item_name} to your order. Total so far: ${total_amount}")
            else:
                print(f"Invalid number. Please choose a number between 1 and {len(menu)}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    if total_amount > 0:
        record_sale(total_amount)
        print(f"\nYour total order amount is: ${total_amount}")
        print("Thank you for your order!")
    else:
        print("No items selected. Order was not placed.")

def view_menu(menu):
    print()
    print("*"*30)
    print("    Menu    ")
    print("*"*30)
    for idx, (item, price) in enumerate(menu.items(), start=1):
        print(f"{idx}. {item} - ${price}")
    print("*"*30)
    print()
def view_order_status(username):
    if not os.path.exists(orders_file) or os.stat(orders_file).st_size == 0:
        print("No orders found.")
        return

    print("\n----- Your Orders -----")
    with open(orders_file, "r") as file:
        for line in file:
            user, item, quantity = line.strip().split(",")
            if user == username:
                print(f"{quantity}x {item}")

    print("\n")

def send_feedback(username):
    feedback = input("Enter your feedback: ")
    with open(feedback_file, "a") as file:
        file.write(f"{username}: {feedback}\n")
    print("Thank you for your feedback!")

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

def load_menu():
    menu = {}
    try:
        with open(menu_file, "r") as file:
            for line in file:
                item, price = line.strip().split(",")
                menu[item] = float(price)
    except FileNotFoundError:
        print("Menu file not found!")
    return menu

def record_sale(amount):
    with open(sales_report_file, "a") as file:
        file.write(f"Sale of ${amount} recorded.\n")
    print(f"Sale of ${amount} recorded.")
