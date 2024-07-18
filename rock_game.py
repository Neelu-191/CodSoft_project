import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!", bg='#ffeb3b')
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result_label.config(text="You win!", bg='#8bc34a')
    else:
        result_label.config(text="You lose!", bg='#f44336')

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.configure(bg='#e0f7fa')

# Create and place the widgets
tk.Label(root, text="Choose your move:", bg='#e0f7fa', fg='#00796b', font=('Arial', 14)).grid(row=0, column=0, columnspan=3, pady=10)

rock_button = tk.Button(root, text="Rock", width=15, command=lambda: determine_winner("rock"), bg='#cfd8dc')
rock_button.grid(row=1, column=0, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper", width=15, command=lambda: determine_winner("paper"), bg='#cfd8dc')
paper_button.grid(row=1, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: determine_winner("scissors"), bg='#cfd8dc')
scissors_button.grid(row=1, column=2, padx=10, pady=10)

user_label = tk.Label(root, text="", bg='#e0f7fa', fg='#00796b', font=('Arial', 12))
user_label.grid(row=2, column=0, columnspan=3, pady=5)

computer_label = tk.Label(root, text="", bg='#e0f7fa', fg='#00796b', font=('Arial', 12))
computer_label.grid(row=3, column=0, columnspan=3, pady=5)

result_label = tk.Label(root, text="", bg='#e0f7fa', fg='#00796b', font=('Arial', 14))
result_label.grid(row=4, column=0, columnspan=3, pady=20)

# Run the main event loop
root.mainloop()
