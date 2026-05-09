from tkinter import *

# Window
root = Tk()
root.title("Bisma Pro Calculator 💎")
root.geometry("320x500")
root.config(bg="#0b1437")
root.resizable(False, False)

# Display
equation = ""

display = Entry(
    root,
    font=("Arial", 28),
    bg="#0b1437",
    fg="white",
    bd=0,
    justify="right"
)
display.pack(fill="both", ipadx=8, ipady=25, padx=10, pady=20)

# Functions
def press(num):
    global equation
    equation += str(num)
    display.delete(0, END)
    display.insert(END, equation)

def equal():
    global equation
    try:
        result = str(eval(equation))
        display.delete(0, END)
        display.insert(END, result)
        equation = result
    except:
        display.delete(0, END)
        display.insert(END, "Error")
        equation = ""

def clear():
    global equation
    equation = ""
    display.delete(0, END)

# Button Style
btn_font = ("Arial", 16, "bold")

# Buttons Frame
frame = Frame(root, bg="#0b1437")
frame.pack()

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
]

for (text, row, col) in buttons:

    color = "#16213e"
    if text in ['/', '*', '-', '+']:
        color = "#fca311"
    elif text == 'C':
        color = "#ff4d4d"

    Button(
        frame,
        text=text,
        font=btn_font,
        fg="white",
        bg=color,
        activebackground=color,
        bd=0,
        width=5,
        height=2,
        command=lambda t=text:
            clear() if t == 'C' else press(t)
    ).grid(row=row, column=col, padx=10, pady=10)

# Equal Button
Button(
    root,
    text="=",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#2ecc71",
    activebackground="#2ecc71",
    bd=0,
    width=20,
    height=2,
    command=equal
).pack(pady=20)

root.mainloop()