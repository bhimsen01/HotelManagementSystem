import os

# File paths
data_folder = "data"
menu_file = os.path.join(data_folder, "menu.txt")
users_file = os.path.join(data_folder, "users.txt")
ingredient_requests_file = os.path.join(data_folder, "ingredient_requests.txt")

# Ensure the data folder exists
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Ensure essential files exist
for file_path in [menu_file, users_file, ingredient_requests_file]:
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("")


def manager_menu(username):
    while True:
        print("\n--------------------------------------------------")
        print(f"     Manager Menu (Logged in as {username})   ")
        print("--------------------------------------------------")
        print("1. Manage Customers (Add/Edit/Delete)")
        print("2. Manage Menu (Add/Edit/Delete)")
        print("3. View Ingredient Requests")
        print("4. Update Profile")
        print("5. Logout")
        print("-" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":
            manage_customers()
        elif choice == "2":
            manage_menu()
        elif choice == "3":
            view_ingredient_requests()
        elif choice == "4":
            update_profile(username)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Please try again.")

def manage_menu():
    while True:
        print("\n----- Manage Menu -----")
        print("1. Add Menu Item")
        print("2. Edit Menu Item")
        print("3. Delete Menu Item")
        print("4. View Menu")
        print("5. Back to Manager Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_menu_item()
        elif choice == "2":
            edit_menu_item()
        elif choice == "3":
            delete_menu_item()
        elif choice == "4":
            view_menu()
        elif choice == "5":
            print("Returning to Manager Menu...")
            break
        else:
            print("Invalid choice! Please try again.")


def add_menu_item():
    item_name = input("Enter item name: ")
    price = input("Enter price: ")

    with open(menu_file, "a") as file:
        file.write(f"\n{item_name},{price}")

    print(f"Item '{item_name}' added successfully.")


def view_menu():
    if os.stat(menu_file).st_size == 0:
        print("The menu is empty.")
        return

    with open(menu_file, "r") as file:
        print("\n--- Menu ---")
        for line in file:
            item_name, price = line.strip().split(",")
            print(f"{item_name} - ${price}")


def edit_menu_item():
    view_menu()
    item_name = input("Enter the name of the item to edit: ")

    menu_list = []
    found = False

    with open(menu_file, "r") as file:
        for line in file:
            name, price = line.strip().split(",")
            if name == item_name:
                new_name = input(f"Enter new name for {name} (or press Enter to keep current name): ") or name
                new_price = input(f"Enter new price for {name} (or press Enter to keep current price): ") or price
                menu_list.append(f"{new_name},{new_price}\n")
                found = True
            else:
                menu_list.append(line)

    if found:
        with open(menu_file, "w") as file:
            file.writelines(menu_list)
        print(f"Item '{item_name}' updated successfully.")
    else:
        print(f"Item '{item_name}' not found.")


def delete_menu_item():
    view_menu()
    item_name = input("Enter the name of the item to delete: ")

    menu_list = []
    found = False

    with open(menu_file, "r") as file:
        for line in file:
            name, price = line.strip().split(",")
            if name != item_name:
                menu_list.append(line)
            else:
                found = True

    if found:
        with open(menu_file, "w") as file:
            file.writelines(menu_list)
        print(f"Item '{item_name}' deleted successfully.")
    else:
        print(f"Item '{item_name}' not found.")


def manage_customers():
    while True:
        print("\n----- Manage Customers -----")
        print("1. Add Customer")
        print("2. Edit Customer")
        print("3. Delete Customer")
        print("4. View Customers")
        print("5. Back to Manager Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            edit_customer()
        elif choice == "3":
            delete_customer()
        elif choice == "4":
            view_customers()
        elif choice == "5":
            print("Returning to Manager Menu...")
            break
        else:
            print("Invalid choice! Please try again.")


def add_customer():
    username = input("Enter customer username: ")
    password = input("Enter customer password: ")

    with open(users_file, "a") as file:
        file.write(f"\n{username},{password},Customer")

    print(f"Customer '{username}' added successfully.")


def view_customers():
    print("\n----- Customers -----")
    with open(users_file, "r") as file:
        for line in file:
            user, password, role = line.strip().split(",")
            if role == "Customer":
                print(f"Username: {user}")


def edit_customer():
    view_customers()
    username = input("Enter the username of the customer to edit: ")

    users = []
    found = False

    with open(users_file, "r") as file:
        for line in file:
            user, password, role = line.strip().split(",")
            if user == username and role == "Customer":
                new_username = input("Enter new username (or press Enter to keep current): ") or user
                new_password = input("Enter new password (or press Enter to keep current): ") or password
                users.append(f"{new_username},{new_password},Customer\n")
                found = True
            else:
                users.append(line)

    if found:
        with open(users_file, "w") as file:
            file.writelines(users)
        print(f"Customer '{username}' updated successfully.")
    else:
        print(f"Customer '{username}' not found.")


def delete_customer():
    view_customers()
    username = input("Enter the username of the customer to delete: ")

    users = []
    found = False

    with open(users_file, "r") as file:
        for line in file:
            user, password, role = line.strip().split(",")
            if user != username:
                users.append(line)
            else:
                found = True

    if found:
        with open(users_file, "w") as file:
            file.writelines(users)
        print(f"Customer '{username}' deleted successfully.")
    else:
        print(f"Customer '{username}' not found.")

def view_ingredient_requests():
    print("\n----- Ingredient Requests -----")
    if os.stat(ingredient_requests_file).st_size == 0:
        print("No ingredient requests found.")
        return

    with open(ingredient_requests_file, "r") as file:
        for line in file:
            ingredient, quantity = line.strip().split(",")
            print(f"{ingredient} - {quantity}")

def update_profile(username):
    print("\n----- Update Profile -----")
    
    users = []
    found = False

    with open(users_file, "r") as file:
        for line in file:
            user, password, role = line.strip().split(",")
            if user == username and role == "Manager":
                new_username = input("Enter new username (or press Enter to keep current): ") or user
                new_password = input("Enter new password (or press Enter to keep current): ") or password
                users.append(f"{new_username},{new_password},Manager\n")
                found = True
            else:
                users.append(line)

    if found:
        with open(users_file, "w") as file:
            file.writelines(users)
        print("Profile updated successfully!")
    else:
        print("Error: Manager profile not found.")

