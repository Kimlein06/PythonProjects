import tkinter as tk

root = tk.Tk()
root.title("Kimlein's Calculator")

# entry display (readonly)
display = tk.Entry(root, width=25, borderwidth=5, font=('Arial', 16), justify="right", state="readonly")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# global state
last_was_equal = False

# helper function to update display safely
def update_display(value):
    display.config(state="normal")
    display.delete(0, tk.END)
    display.insert(0, value)
    display.config(state="readonly")

# function to handle button clicks
def button_click(value):
    global last_was_equal

    if value == "AC":
        update_display("")
        last_was_equal = False

    elif value == "🔙":
        current = display.get()
        update_display(current[:-1])
        last_was_equal = False

    elif value == "+/-":
        current = display.get()
        if current.startswith("-"):
            update_display(current[1:])
        else:
            update_display("-" + current)
        last_was_equal = False

    elif value == "%":
        try:
            current = float(display.get())
            result = current / 100
            update_display(str(result))
        except:
            update_display("Error")
        last_was_equal = False

    elif value == "=":
        try:
            result = str(eval(display.get()))
            update_display(result)
            last_was_equal = True   # mark that equals was pressed
        except:
            update_display("Error")
            last_was_equal = True

    else:  # numbers and operators
        current = display.get()

        if last_was_equal:
            if value.isdigit():  # start fresh if a number is pressed
                update_display(str(value))
            else:  # continue calculation if operator
                update_display(current + str(value))
            last_was_equal = False
        else:
            update_display(current + str(value))

# buttons
def make_button(root, text, row, col):
    btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14),
                    command=lambda: button_click(text))
    btn.grid(row=row, column=col)

# first row
make_button(root, "AC", 1, 0)
make_button(root, "+/-", 1, 1)
make_button(root, "%", 1, 2)
make_button(root, "/", 1, 3)

# second row
make_button(root, "9", 2, 0)
make_button(root, "8", 2, 1)
make_button(root, "7", 2, 2)
make_button(root, "*", 2, 3)

# third row
make_button(root, "4", 3, 0)
make_button(root, "5", 3, 1)
make_button(root, "6", 3, 2)
make_button(root, "-", 3, 3)

# fourth row
make_button(root, "1", 4, 0)
make_button(root, "2", 4, 1)
make_button(root, "3", 4, 2)
make_button(root, "+", 4, 3)

# last row
make_button(root, "🔙", 5, 0)
make_button(root, "0", 5, 1)
make_button(root, ".", 5, 2)
make_button(root, "=", 5, 3)

# keyboard support
def key_press(event):
    char = event.char
    if char in "0123456789+-*/%.":
        button_click(char)
    elif char == "\r":   # Enter key
        button_click("=")
    elif char == "\x08": # Backspace
        button_click("🔙")

root.bind("<Key>", key_press)

root.mainloop()
