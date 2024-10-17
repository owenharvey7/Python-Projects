"""
# 18
# Regular Expressions Challenge:
# Write a program that validates if a phone number is in the correct format using regular expressions.
# Difficulty: Medium
"""

import re
import tkinter as tk
import tkinter.messagebox as mb

# Function to validate phone number format
def validate_phone_number():
    phone_number = entry.get()  # Get the phone number from the entry field
    pattern = r"^\d{3}-\d{3}-\d{4}$"  # Define the regular expression pattern

    # Check if the phone number matches the pattern
    if re.match(pattern, phone_number):
        mb.showinfo("Validation Result", "Phone number is valid")
        # Ask user if they want to validate another phone number
        if mb.askyesno("Validate Another Number", "Do you want to validate another phone number?"):
            entry.delete(0, 'end')
        else:
            mb.showwarning("Exiting", "Thank you for using the phone number validator")
            window.destroy()



    else:
        mb.showerror("Validation Result", "Phone number is not in the correct format")

# Create the main Tkinter window
window = tk.Tk()
# Set the dimensions of the window
w = 400  # Width for the Tk root
h = 75  # Height for the Tk root
# Get screen width and height
ws = window.winfo_screenwidth()  # Width of the screen
hs = window.winfo_screenheight()  # Height of the screen
# Calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# Set the dimensions of the screen and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
# Set the window title
window.title("Phone Number Validator")

# Create a label for instructions
label = tk.Label(window, text="Enter a phone number in the format XXX-XXX-XXXX:")
label.pack()

# Create an entry field for the phone number
entry = tk.Entry(window)
entry.pack()

# Create a button to validate the phone number
button = tk.Button(window, text="Validate", command=validate_phone_number)
button.pack()

# Run the Tkinter main loop
window.mainloop()