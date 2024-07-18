import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg='light pink')  # Set background color of the window

# Create and place the widgets
tk.Label(root, text="Password Length:", bg='#f0f4c3', fg='#388e3c').grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(root, bg='#ffffff', fg='#000000')
length_entry.grid(row=0, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate", command=generate_password, bg='#388e3c', fg='#ffffff')
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

tk.Label(root, text="Generated Password:", bg='#f0f4c3', fg='#388e3c').grid(row=2, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, bg='#ffffff', fg='#000000')
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Run the main event loop
root.mainloop()
