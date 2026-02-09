import os

data_folder = "data"
orders_file = os.path.join(data_folder, "orders.txt")

def place_order(username, items):
    order_id = get_next_order_id()
    with open(orders_file, "a") as file:
        file.write(f"{order_id},{username},{items},Pending\n")
    print("Order placed successfully!")

def get_next_order_id():
    if not os.path.exists(orders_file):
        return 1
    
    with open(orders_file, "r") as file:
        lines = file.readlines()
        if not lines:
            return 1
        last_order_id = int(lines[-1].split(",")[0])
        return last_order_id + 1

def view_orders(username=None):
    if not os.path.exists(orders_file):
        print("No orders found.")
        return
    
    with open(orders_file, "r") as file:
        orders = [line.strip().split(",") for line in file]
    
    if not orders:
        print("No orders found.")
        return
    
    print("\nOrders:")
    print("+---------+------------+----------------+----------+----------+")
    print("| OrderID | Username   | Items          | Quantity | Price    |")
    print("+---------+------------+----------------+----------+----------+")
    
    for order in orders:
        order_id, user, items, status = order
        item_list = items.split(";")  # Assuming items are stored as 'item1-qty-price;item2-qty-price'
        for item in item_list:
            name, quantity, price = item.split("-")
            if username is None or username == user:
                print(f"| {order_id:<7} | {user:<10} | {name:<14} | {quantity:<8} | RM{price:<7} |")
    
    print("+---------+------------+----------------+----------+----------+")

def update_order_status(order_id, new_status):
    if not os.path.exists(orders_file):
        print("No orders found.")
        return
    
    lines = []
    with open(orders_file, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == str(order_id):
                data[3] = new_status
            lines.append(",".join(data))
    
    with open(orders_file, "w") as file:
        file.write("\n".join(lines) + "\n")
    
    print("Order status updated successfully!")
