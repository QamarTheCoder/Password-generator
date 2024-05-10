import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + '!@#$%^&*()_+=|;:,.<>?'

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def save_password(password):
    with open("generated_password.txt", "a") as file:
        file.write(f"{password}\n")
    messagebox.showinfo("Password Saved", "Password saved to generated_password.txt")

def generate_and_save_password():
    length = int(length_entry.get())
    password = generate_password(length)
    save_password(password)

window = tk.Tk()
window.title("Password Generator")

length_label = tk.Label(window, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.insert(0, "12")

generate_button = tk.Button(window, text="Generate Password", command=generate_and_save_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
