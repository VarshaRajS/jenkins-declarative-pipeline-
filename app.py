import tkinter as tk
import random

# List of compliments
compliments = [
    "You look awesome today!",
    "You're a coding genius!",
    "You have a brilliant mind!",
    "You're so creative!",
    "You're unstoppable!",
    "You light up the room!"
]

# Function to show a random compliment
def show_compliment():
    compliment = random.choice(compliments)
    label.config(text=compliment)

# Create the main application window
root = tk.Tk()
root.title("Fun Compliment App")

# Set the size of the window
root.geometry("300x200")

# Create a label to display the compliment
label = tk.Label(root, text="Click the button for a compliment!", font=("Helvetica", 12), wraplength=250)
label.pack(pady=20)

# Create a button to generate a compliment
button = tk.Button(root, text="Get Compliment", command=show_compliment, font=("Helvetica", 12), bg="lightblue")
button.pack(pady=10)

# Run the app
root.mainloop()
