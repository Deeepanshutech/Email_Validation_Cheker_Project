import re
import tkinter as tk
from tkinter import messagebox


def validate_email():
    email = email_entry.get()
    email_condition = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$'

    if re.search(email_condition, email):
        messagebox.showinfo("Validation Result", "Right Email")
    else:
        messagebox.showerror("Validation Result", "Wrong Email")


# Create the main window
root = tk.Tk()
root.title("Email Validation by Deepanshu Thakur")

# Create and place widgets
label = tk.Label(root, text="Enter your Email:")
label.pack(pady=30)

email_entry = tk.Entry(root, width=50)
email_entry.pack()

validate_button = tk.Button(
    root, text="Validate Email", command=validate_email)
validate_button.pack(pady=30)


root.mainloop()
