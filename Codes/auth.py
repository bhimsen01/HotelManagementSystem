import getpass
import data_handler

def login():
    attempts = 3
    
    while attempts > 0:
        username = input("Enter Username: ")
        password = getpass.getpass("Enter Password: ")
        
        user = data_handler.authenticate_user(username, password)
        
        if user:
            print(f"\nLogin successful! Welcome, {user['role']} {user['username']}.")
            return user  # Return user details for further processing
        else:
            attempts -= 1
            print(f"Incorrect username or password. Attempts left: {attempts}\n")
    
    print("Too many failed attempts. Exiting system.")
    return None
