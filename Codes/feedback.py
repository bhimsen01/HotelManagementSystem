import os

data_folder = "data"
feedback_file = os.path.join(data_folder, "feedback.txt")

def submit_feedback(username, message):
    with open(feedback_file, "a") as file:
        file.write(f"{username},{message}\n")
    print("Feedback submitted successfully!")

def view_feedback():
    if not os.path.exists(feedback_file):
        print("No feedback found.")
        return
    
    with open(feedback_file, "r") as file:
        print("\nCustomer Feedback:")
        for line in file:
            username, message = line.strip().split(",", 1)
            print(f"User: {username}, Feedback: {message}")
