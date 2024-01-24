import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_name = entry.get()
    messagebox.showinfo("Hello", f"Hello, {user_name}!")

# Create the main application window
app = tk.Tk()
app.title("Simple Python GUI App")

# Create a label widget
label = tk.Label(app, text="Enter your name:")

# Create an entry widget
entry = tk.Entry(app)

# Create a button widget
button = tk.Button(app, text="Say Hello", command=on_button_click)

# Pack the widgets into the window
label.pack(pady=10)
entry.pack(pady=10)
button.pack(pady=10)

# Run the application
app.mainloop()
