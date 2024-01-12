import tkinter as tk
from random import choice

def change_color():
    # List of colors
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
    # Change button color to a random color from the list
    button.config(bg=choice(colors))

# Create the main window
root = tk.Tk()
root.title("Color Changing Button")

# Create a button widget
button = tk.Button(root, text="Click me!", command=change_color)

# Place the button in the window
button.pack(pady=20, padx=20)

# Start the GUI event loop
root.mainloop()
