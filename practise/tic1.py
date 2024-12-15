import tkinter as tk
from tkinter import messagebox

# Function to check for a winner
def check_winner():
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combos:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for i in combo:
                buttons[i].config(bg="lightgreen")  # Highlight winning combo
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

# Function to handle button clicks
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index].config(text=current_player, fg="white", bg="blue" if current_player == "X" else "orange")
        check_winner()
        toggle_player()

# Toggle the current player
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Initialize the game window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="black")  # Background color for the window

# Create the buttons for the grid
buttons = [
    tk.Button(
        root, text="", font=("Helvetica", 20), width=5, height=2,
        bg="white", command=lambda i=i: button_click(i)
    ) for i in range(9)
]

# Arrange the buttons in a 3x3 grid
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)

# Initialize game state
current_player = "X"
winner = False

# Add a label to display the current player's turn
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Helvetica", 16), bg="black", fg="white")
label.grid(row=3, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
