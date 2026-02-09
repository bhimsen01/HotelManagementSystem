import os

data_folder = "data"
users_file = os.path.join(data_folder, "users.txt")

def authenticate_user(username, password):
    if not os.path.exists(users_file):
        print("User database not found.")
        return None
    
    with open(users_file, "r") as file:
        for line in file:
            stored_username, stored_password, role = line.strip().split(",")
            if stored_username == username and stored_password == password:
                return {"username": stored_username, "role": role}
    
    return None

def register_user(username, password, role):
    with open(users_file, "a") as file:
        file.write(f"{username},{password},{role}\n")
    print("User registered successfully.")

def list_users():
    if not os.path.exists(users_file):
        print("No users found.")
        return
    
    with open(users_file, "r") as file:
        print("\nRegistered Users:")
        for line in file:
            username, _, role = line.strip().split(",")
            print(f"Username: {username}, Role: {role}")
