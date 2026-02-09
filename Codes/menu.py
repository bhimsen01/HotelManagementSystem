import os

data_folder = "data"
menu_file = os.path.join(data_folder, "menu.txt")

def add_menu_item(name,price):
    with open(menu_file, "a") as file:
        file.write(f"{name},,{price}\n")
    print("Menu item added successfully!")

def view_menu():
    if not os.path.exists(menu_file) or os.stat(menu_file).st_size == 0:
        print("No menu items found.")
        return

    print("\nName\t\tPrice ($)")
    print("-" * 40)

    with open(menu_file, "r") as file:
        for line in file:
            name,price = line.strip().split(",")
            print(f"{name}\t${price}")

def update_menu_item(old_name, new_name, new_price):
    if not os.path.exists(menu_file):
        print("No menu items found.")
        return
    
    lines = []
    with open(menu_file, "r") as file:
        for line in file:
            name,price = line.strip().split(",")
            if name == old_name:
                name,price = new_name,new_price
            lines.append(f"{name},{price}")
    
    with open(menu_file, "w") as file:
        file.write("\n".join(lines) + "\n")
    
    print("Menu item updated successfully!")

def delete_menu_item(name):
    if not os.path.exists(menu_file):
        print("No menu items found.")
        return
    
    lines = []
    with open(menu_file, "r") as file:
        for line in file:
            if not line.startswith(name + ","):
                lines.append(line.strip())
    
    with open(menu_file, "w") as file:
        file.write("\n".join(lines) + "\n")
    
    print("Menu item deleted successfully!")
