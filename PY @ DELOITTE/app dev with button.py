import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main application window
app = tk.Tk()
app.title("Simple Python App")

# Create a label widget
label = tk.Label(app, text="Welcome to Python App")

# Create a button widget
button = tk.Button(app, text="Click me!", command=on_button_click)

# Pack the widgets into the window
label.pack(pady=10)
button.pack(pady=10)

# Run the application
app.mainloop()
