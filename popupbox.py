#in the terminal, pip install tkinter
#importing tkinter and random, and then from tkinter import messagebox
#tkinter is a graphical user interface(GUI) library in python
import tkinter as tk
import random
from tkinter import messagebox

def move_button(event=None):
    x = random.randint(0, window_width - button_width)
    y = random.randint(0, window_height - button_height)
    button.place(x=x, y=y)

#under def function, name the other box as yes, and write the message that you want to show
def on_yes_click():
    messagebox.showinfo(
        "💕",
        "YAYYYYYYY!!! 💖🥰\n\nI knew you'd say yes! ✨💕\n\nBest choice ever 😌"
    )

# Create the main window
#give it a title and width and height, and the geometry will be width x height
window = tk.Tk()
window.title("Pop-UP")
window_width = 500
window_height = 300
window.geometry(f"{window_width}x{window_height}")

# Background Color
window.configure(bg="#FFD6E8")  # Light pink

# Create the question label 
question_label = tk.Label(
    window, 
    text="do you love me?<3",
    font=("Comic Sans MS", 18, "bold"),
    bg="#FFD6E8",
    fg="#D63384"
)
question_label.pack(pady=30)

subtitle = tk.Label(
    window,
    text="Choose carefully 😌💕",
    font=("Arial", 12),
    bg="#FFD6E8",
    fg="#D63384"
)

subtitle.pack()
subtitle.place(x=170, y=70)

# Create the buttons
button_width = 78
button_height = 26
button = tk.Label(
    window,
    text="😭 No",
    bg="#FF69B4",
    fg="white",
    font=("Arial", 14, "bold"),
    padx=20,
    pady=10
)

button.place(x=150, y=150)
button.bind("<Enter>", lambda e: move_button())


button_yes = tk.Label(
    window,
    text="🫶🏻 Yes",
    bg="#D63384",
    fg="white",
    font=("Arial", 14, "bold"),
    padx=20,
    pady=10
)

button_yes.place(x=250, y=150)
button_yes.bind("<Button-1>", lambda e: on_yes_click())

# Start the main loop
window.mainloop()