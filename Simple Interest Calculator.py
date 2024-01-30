#This program calculates simple interest and uses the Graphics User Interface

import tkinter as tk
from tkinter import messagebox

# Function to calculate simple interest
def calculate_simple_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        interest = (principal * rate * time) / 100

        result_label.config(text=f"{interest:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

def reset():
    try:
        principal_entry.delete(0, "end")
        rate_entry.delete(0, "end")
        time_entry.delete(0, "end")
        result_label.config(text="0")
        principal_entry.focus()


    except Exception:
        messagebox.showerror("Error")

def close():
    win.destroy()


# Create the main application window
win = tk.Tk()
win.title("Simple Interest Calculator")
win.geometry("350x250")

# Labels and entry fields
principal_label = tk.Label(win, text="Principal (Naira):")
principal_label.grid(row=1, column=1, sticky="W")
principal_entry = tk.Entry(win)
principal_entry.grid(row=1, column=2)

rate_label = tk.Label(win, text="Rate (%):")
rate_label.grid(row=2, column=1, sticky="W")
rate_entry = tk.Entry(win)
rate_entry.grid(row=2, column=2)

time_label = tk.Label(win, text="Time (Years):")
time_label.grid(row=3, column=1, sticky="W")
time_entry = tk.Entry(win)
time_entry.grid(row=3, column=2)

space = tk.Label(win, text="")
space.grid(row=4, column=1, sticky="W")

interest_label = result_label = tk.Label(win, text="Interest: ")
result_label.grid(row=5, column=1)

# Label to display the result
result_label = tk.Label(win, text="0")
result_label.grid(row=5, column=2, sticky="W")

# Close button
close = tk.Button(win,  width=7, text="Close", command=close, bg="red", fg="white")
close.grid(row=6, column=1)

# Reset button
reset = tk.Button(win, width=7, text="Reset", command=reset)
reset.grid(row=6, column=2)

# Calculate button
calculate_button = tk.Button(win, width=8, text="Compute", command=calculate_simple_interest)
calculate_button.grid(row=6, column=3)

# Start the tkinter main loop
win.mainloop()

