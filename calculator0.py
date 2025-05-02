import tkinter as tk
import math

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = [":", "×", "-", "+", "=", "÷"]
top_symbols = ["AC", "+/-", "%"]

# To arrange the design
row_count = len(button_values) #5
column_count = len(button_values[0]) # 4

# Color settings
color_tuscany = "#C79E9E"
color_black = "#1C1C1C"
color_falu_red = "#7E1D22"
color_smoky_topaz = "#914144"
color_white = "white"

# window setup
window = tk.Tk() # create window
window.title("Calculator")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text="0", font=("Arial", 45), background=color_black,
                foreground=color_white, anchor="e", width=column_count) # width to control the symbols existance

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tk.Button(frame, text=value, font=("Arial", 30),
                           width=column_count-1, height=1,
                           command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=color_white, background=color_falu_red)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_smoky_topaz)
        else:
            button.config(foreground=color_black, background=color_tuscany)

        button.grid(row=row+1, column=column)

frame.pack()

# A+B, A-B, A*B, A/B
A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)

                clear_all()

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
            
            operator = value


    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
    elif value == "√":
        result = math.sqrt(float(label["text"]))
        label["text"] = remove_zero_decimal(result)
    else: # digits or .
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0": #0
                label["text"] = value #replace 0
            else:
                label["text"] += value #append value


# center the window
window.update() # update window with the new size
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int(screen_width/2) - (window_width/2)
window_y = int(screen_height/2) - (window_height/2)

# format "{w}x{h}+{x}+{y}"
window.geometry(f"{int(window_width)}x{int(window_height)}+{int(window_x)}+{int(window_y)}")

window.mainloop()
