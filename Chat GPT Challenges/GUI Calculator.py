from tkinter import *

# Function to perform the calculation based on user input
def calculate():
    try:
        num1 = float(entry1.get())  # Get the first number from entry1
        num2 = float(entry3.get())  # Get the second number from entry3
        operator = entry2.get()  # Get the operator from entry2

        # Perform the calculation based on the operator
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        else:
            result = "Error: Invalid operator"
    except ValueError:
        result = "Error: Invalid input"  # Handle invalid input

    # Update the label with the result
    label.config(text="Result: " + str(result))

# Function to clear all entry fields
def clear():
    entry1.delete(0, 'end')  # Clear the first entry field
    entry2.delete(0, 'end')  # Clear the operator entry field
    entry3.delete(0, 'end')  # Clear the second entry field
    label.config(text="Result:")  # Reset the label text

# Function to handle focus in for entry fields
def on_focus_in(event, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, 'end')

# Function to handle focus out for entry fields
def on_focus_out(event, entry, default_text):
    if entry.get() == '':
        entry.insert(0, default_text)

# Create the main Tkinter window
window = Tk()
w = 950  # Width for the Tk root
h = 100  # Height for the Tk root

# Get screen width and height
ws = window.winfo_screenwidth()  # Width of the screen
hs = window.winfo_screenheight()  # Height of the screen

# Calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# Set the dimensions of the screen and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.title("Simple GUI Calculator")

# Create the entry fields

# Create the entry field for the first number
entry1_default_text = "Enter first value"
entry1 = Entry(window)
entry1.insert(0, entry1_default_text)
entry1.bind("<FocusIn>", lambda e: on_focus_in(e, entry1, entry1_default_text))
entry1.bind("<FocusOut>", lambda e: on_focus_out(e, entry1, entry1_default_text))
entry1.pack(side=LEFT)

# Create the entry field for the operator
entry2_default_text = "Enter operator (+, -, *, /)"
entry2 = Entry(window)
entry2.insert(0, entry2_default_text)
entry2.bind("<FocusIn>", lambda e: on_focus_in(e, entry2, entry2_default_text))
entry2.bind("<FocusOut>", lambda e: on_focus_out(e, entry2, entry2_default_text))
entry2.pack(side=LEFT)

# Create the entry field for the second number
entry3_default_text = "Enter second value"
entry3 = Entry(window)
entry3.insert(0, entry3_default_text)
entry3.bind("<FocusIn>", lambda e: on_focus_in(e, entry3, entry3_default_text))
entry3.bind("<FocusOut>", lambda e: on_focus_out(e, entry3, entry3_default_text))
entry3.pack(side=LEFT)

# Create the Calculate button
button = Button(window, text="Calculate", command=calculate)
button.pack(side=LEFT)

# Create the Clear button
clear_button = Button(window, text="Clear", command=clear)
clear_button.pack(side=LEFT)

# Create the label to display the result
label = Label(window, text="Result:")
label.pack(side=LEFT)

# Start the Tkinter event loop
window.mainloop()
