import tkinter as tk
from tkinter import messagebox

# Function to validate login credentials
def validate_login():
    username = entry_username.get()  # Get username from input field
    password = entry_password.get()  # Get password from input field

    # Sample credentials for validation
    if username == "admin" and password == "password123":
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")  # Display welcome message
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")  # Show error message

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create and place labels and entry fields for username and password
label_username = tk.Label(root, text="Username")
label_username.pack(pady=5)  # Add some vertical space

entry_username = tk.Entry(root)
entry_username.pack(pady=5)  # Add some vertical space

label_password = tk.Label(root, text="Password")
label_password.pack(pady=5)  # Add some vertical space

entry_password = tk.Entry(root, show='*')  # Hide password input
entry_password.pack(pady=5)  # Add some vertical space

# Create and place the login button
button_login = tk.Button(root, text="Login", command=validate_login)
button_login.pack(pady=20)  # Add some vertical space