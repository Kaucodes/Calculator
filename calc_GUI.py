# have libraries
import tkinter as tk
from tkinter import messagebox
import math

# make a window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

#make Entry to the numbers
num1_entry = tk.Entry(window)
num1_entry.pack(pady=5)

num2_entry = tk.Entry(window)
num2_entry.pack(pady=5)

# definition to show the result
def show_result(result):
    messagebox.showinfo("Result", f"The result is: {result}")

# operators definition
# addition
def add_numbers():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 + num2
        show_result(result)
    except ValueError:
        messagebox.showerror("Error", "Invalid number entered.")

# subtraction 
def substract_numbers():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 - num2
        show_result(result)
    except ValueError:
        messagebox.showerror("Error", "Invalid number entered.")

# multiplication
def multiply_numbers():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 * num2
        show_result(result)
    except ValueError:
        messagebox.showerror("Error", "Invalid number entered.")

# division
def divide_numbers():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 / num2
        show_result(result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")

# Button for every operation
tk.Button(window, text="Add", command=add_numbers).pack(pady=5)
tk.Button(window, text="Subtract", command=substract_numbers).pack(pady=5)
tk.Button(window, text="Multiply", command=multiply_numbers).pack(pady=5)
tk.Button(window, text="Divide", command=divide_numbers).pack(pady=5)

# Square Root definition
def sqrt_number():
    try:
        num = float(num1_entry.get())
        result = math.sqrt(num)
        show_result(result)
    except ValueError:
        messagebox.showerror("Error", "Invalid number entered.")

# Button for square root
tk.Button(window, text="Square Root", command=sqrt_number).pack(pady=5)


window.mainloop()
