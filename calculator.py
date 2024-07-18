import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    result_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='#e0f7fa')  # Set background color of the window

# Create and place the widgets
entry1 = tk.Entry(root, bg='#ffffff', fg='#000000')
entry1.grid(row=0, column=1, padx=10, pady=5)

entry2 = tk.Entry(root, bg='#ffffff', fg='#000000')
entry2.grid(row=1, column=1, padx=10, pady=5)

operation_var = tk.StringVar(root)
operation_var.set("Add")  # default value

operation_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")
operation_menu.config(bg='#4db6ac', fg='#ffffff')
operation_menu.grid(row=2, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate, bg='#00796b', fg='#ffffff')
calculate_button.grid(row=3, column=1, padx=10, pady=5)

result_label = tk.Label(root, text="Result: ", bg='#e0f7fa', fg='#00796b')
result_label.grid(row=4, column=1, padx=10, pady=5)

# Create and place the labels
tk.Label(root, text="Enter first number:", bg='#e0f7fa', fg='#00796b').grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Enter second number:", bg='#e0f7fa', fg='#00796b').grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Select operation:", bg='#e0f7fa', fg='#00796b').grid(row=2, column=0, padx=10, pady=5)

# Run the main event loop
root.mainloop()
