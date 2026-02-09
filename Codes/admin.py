import os

# File paths
data_folder = "data"
staff_file = os.path.join(data_folder, "staff.txt")
sales_report_file = os.path.join(data_folder, "sales_report.txt")
feedback_file = os.path.join(data_folder, "feedback.txt")
users_file = os.path.join(data_folder, "users.txt")

# Ensure "data" folder exists
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Ensure essential files exist
for file in [staff_file, sales_report_file, feedback_file, users_file]:
    if not os.path.exists(file):
        with open(file, "w") as f:
            f.write("")

def print_header(title):
    print("\n" + "=" * 40)
    print(f"       {title} ")
    print("=" * 40)

def admin_menu(username):
    while True:
        print("\n--------------------------------------------------")
        print(f"      ADMIN DASHBOARD (Logged in as {username})  ")
        print("--------------------------------------------------")
        print(" 1. Manage Staff ")
        print(" 2. View Sales Report ")
        print(" 3. View Customer Feedback ")
        print(" 4. Update Profile ")
        print(" 5. Logout ")
        print("--------------------------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            manage_staff()
        elif choice == "2":
            view_sales_report()
        elif choice == "3":
            view_feedback()
        elif choice == "4":
            update_profile(username)
        elif choice == "5":
            print(" Logging out...\n")
            return
        else:
            print(" Invalid choice! Please try again.")


def manage_staff():
    while True:
        print("\n----- STAFF MANAGEMENT -----")
        print(" 1. Add Staff")
        print(" 2. Edit Staff")
        print(" 3. Delete Staff")
        print(" 4. View Staff List")
        print(" 5. Back to Admin Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_staff()
        elif choice == "2":
            edit_staff()
        elif choice == "3":
            delete_staff()
        elif choice == "4":
            view_staff()
        elif choice == "5":
            print(" Returning to Admin Menu...\n")
            return
        else:
            print(" Invalid choice! Please try again.")


def add_staff():
    print("\n----- ADD STAFF -----")
    name = input("Enter staff name: ")
    role = input("Enter staff role: ")

    with open(staff_file, "a") as file:
        file.write(f"{name},{role}\n")

    print(f" Staff '{name}' added successfully!")


def view_staff():
    print("\n----- STAFF LIST -----")
    if os.stat(staff_file).st_size == 0:
        print(" No staff members found.")
        return

    print(" Name\t\t Role")
    print("-" * 40)

    with open(staff_file, "r") as file:
        for line in file:
            name, role = line.strip().split(",")
            print(f"{name}\t\t{role}")

    print("-" * 40)


def edit_staff():
    print("\n----- EDIT STAFF -----")
    view_staff()
    staff_name = input("Enter the name of the staff member to edit: ")

    staff_list = []
    found = False

    with open(staff_file, "r") as file:
        for line in file:
            name, role = line.strip().split(",")
            if name == staff_name:
                new_name = input(f"Enter new name for {name} (or press Enter to keep current name): ") or name
                new_role = input(f"Enter new role for {name} (or press Enter to keep current role): ") or role
                staff_list.append(f"{new_name},{new_role}\n")
                found = True
            else:
                staff_list.append(line)
    if found:
        with open(staff_file, "w") as file:
            file.writelines(staff_list)
        print(f" Staff '{staff_name}' updated successfully!")
    else:
        print(f" Staff '{staff_name}' not found.")

def delete_staff():
    print("\n----- DELETE STAFF -----")
    view_staff()
    staff_name = input("Enter the name of the staff member to delete: ")
    staff_list = []
    found = False
    with open(staff_file, "r") as file:
        for line in file:
            name, role = line.strip().split(",")
            if name != staff_name:
                staff_list.append(line)
            else:
                found = True
    if found:
        with open(staff_file, "w") as file:
            file.writelines(staff_list)
        print(f" Staff '{staff_name}' deleted successfully!")
    else:
        print(f" Staff '{staff_name}' not found.")

def view_sales_report():
    try:
        with open(sales_report_file, "r") as file:
            content = file.read()
        if content:
            print("\n----- Sales Report -----\n")
            print(content)
        else:
            print("\nNo sales report available.\n")    
    except Exception as e:
        print(f"Error reading the sales report: {e}")


def view_feedback():
    try:
        with open(feedback_file, "r") as file:
            content = file.read()

        if content:
            print("\n----- Customer Feedback -----\n")
            print(content)
        else:
            print("\nNo customer feedback available.\n")
    
    except Exception as e:
        print(f"Error reading the customer feedback: {e}")


def update_profile(username):
    print_header("\n----- UPDATE PROFILE -----")
    user_list = []
    found = False

    # Ask for new username and password
    new_username = input(f" Enter new username (current username is '{username}'): ") or username
    new_password = input(" Enter new password: ")

    try:
        # Open the users file to find the user to update
        with open(users_file, "r") as file:
            for line in file:
                stored_username, stored_password, role = line.strip().split(",")
                if stored_username == username:
                    # Update username and password if found
                    user_list.append(f"{new_username},{new_password},{role}\n")
                    found = True
                else:
                    user_list.append(line)

        if found:
            # Write the updated user list back to the file
            with open(users_file, "w") as file:
                file.writelines(user_list)
            print(f" Profile updated successfully! New username: {new_username}")
        else:
            print(f" User '{username}' not found.")
    except IOError as e:
        print(f"Error updating profile: {e}")


