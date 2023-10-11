import yaml
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import time
import os
import tkinter as tk
from tkinter import messagebox

def select_items(items):
    selected_items = []
    
    def submit_choices():
        for i, checkbox in enumerate(checkboxes):
            if checkbox.get() == 1:
                selected_items.append(items[i])
        
        window.destroy()
    
    window = tk.Tk()
    window.title("Select Items")
    
    label = tk.Label(window, text="Available items:")
    label.pack()
    
    checkboxes = []
    for i, item in enumerate(items):
        checkbox = tk.IntVar()
        checkbox_widget = tk.Checkbutton(window, text=f"{item['item']} - ${item['price']}", variable=checkbox)
        checkbox_widget.pack()
        checkboxes.append(checkbox)
    
    submit_button = tk.Button(window, text="Submit", command=submit_choices)
    submit_button.pack()
    
    window.mainloop()
    
    return selected_items

def calculate_total_cost(selected_items):
    total_cost = sum(item['price'] for item in selected_items)
    return total_cost

def get_amount_paid(selected_items):
    window = tk.Tk()
    window.title("Amount Paid")
    
    for item in selected_items:
        label = tk.Label(window, text=f"{item['item']} - ${item['price']}")
        label.pack()
    
    label = tk.Label(window, text="Total cost:")
    label.pack()
    
    total_cost_label = tk.Label(window, text=f"${calculate_total_cost(selected_items):.2f}")
    total_cost_label.pack()
    
    amount_entry = tk.Entry(window)
    amount_entry.pack()
    
    def submit_amount(event=None):
        nonlocal amount_paid
        amount_paid = float(amount_entry.get())
        window.destroy()
    
    submit_button = tk.Button(window, text="Submit", command=submit_amount)
    submit_button.pack()
    
    amount_entry.bind("<Return>", submit_amount)  # Bind Enter key to submit_amount function
    
    window.mainloop()
    
    while amount_paid is None or amount_paid < calculate_total_cost(selected_items):
        window = tk.Tk()
        window.withdraw()
        messagebox.showerror("Error", "Insufficient amount. Please enter a higher value.")
        amount_entry.delete(0, tk.END)
        amount_entry.focus()
        window.mainloop()
        amount_paid = float(amount_entry.get())
    
    return amount_paid

while True:
    with open('items.yaml', 'r') as file:
        items = yaml.safe_load(file)

    selected_items = select_items(items)
    amount_paid = get_amount_paid(selected_items)
    total_cost = calculate_total_cost(selected_items)
    change = amount_paid - total_cost

    print(f"Total cost: ${total_cost:.2f}")
    print(f"Change owed: ${change:.2f}")

    messagebox.showinfo("Information", f"Total cost: ${total_cost:.2f}\nChange owed: ${change:.2f}")