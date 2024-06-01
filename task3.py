import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, complexity):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    if complexity == 'weak':
        characters = lower
    elif complexity == 'moderate':
        characters = lower + upper + digits
    elif complexity == 'strong':
        characters = lower + upper + digits + special
    else:
        raise ValueError("Invalid complexity level. Choose 'weak', 'moderate', or 'strong'.")


    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def on_generate():
    try:
        length = int(length_entry.get())
        complexity = complexity_var.get()

        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive number.")
            return
        
        password = generate_password(length, complexity)
        
        result_label.config(text=f"Generated password: {password}")
    
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter the desired length of the password:").grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Select the complexity level:").grid(row=1, column=0, padx=10, pady=5)
complexity_var = tk.StringVar(value="weak")
tk.Radiobutton(root, text="Weak", variable=complexity_var, value="weak").grid(row=1, column=1, padx=10, pady=5, sticky='w')
tk.Radiobutton(root, text="Moderate", variable=complexity_var, value="moderate").grid(row=2, column=1, padx=10, pady=5, sticky='w')
tk.Radiobutton(root, text="Strong", variable=complexity_var, value="strong").grid(row=3, column=1, padx=10, pady=5, sticky='w')

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
