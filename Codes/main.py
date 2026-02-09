import auth
import admin
import manager
import chef
import customer

def main():
    try:
        print("\n=================================================")
        print(" 🍽️  Delicious Restaurant Management System  🍽️ ")
        print("=================================================\n")

        # Attempt user login
        user = auth.login()

        if user:
            role = user['role'].lower()
            username = user['username']  # Get the username

            print("=" * 50)
            print()

            if role == "admin":
                admin.admin_menu(username)  
            elif role == "manager":
                manager.manager_menu(username)
            elif role == "chef":
                chef.chef_menu(username)
            elif role == "customer":
                customer.customer_menu(username)
            else:
                print("⚠️ Invalid user role.")
        else:
            print("⚠️ Login failed!")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred during execution: {e}")
