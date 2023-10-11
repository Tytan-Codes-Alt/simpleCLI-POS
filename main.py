import yaml
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import time
import os
def select_items(items):
    os.system('clear')
    selected_items = []
    print("Available items:")
    for i, item in enumerate(items):
        print(f"{i+1}. {item['item']} - ${item['price']}")
    
    choices = input(f"{Fore.GREEN}Enter the item numbers separated by commas: ")
    choices = choices.split(',')
    
    for choice in choices:
        if choice.strip() == '0':
            break
        try:
            index = int(choice.strip()) - 1
            if 0 <= index < len(items):
                selected_items.append(items[index])
            else:
                print(f"{Fore.RED}Invalid choice: {choice}. Ignoring.")
        except ValueError:
            print(f"{Fore.RED}Invalid choice: {choice}. Ignoring.")
    
    return selected_items

def calculate_total_cost(selected_items):
    total_cost = sum(item['price'] for item in selected_items)
    return total_cost

def calculate_change(total_cost):
    while True:
        try:
            amount_paid = float(input("Enter the amount paid: $"))
            if amount_paid >= total_cost:
                change = amount_paid - total_cost
                return change
            else:
                print(f"{Fore.RED}Insufficient amount. Please enter a higher value.")
        except ValueError:
            print(f"{Fore.RED}Invalid amount. Please enter a valid number.")

with open('items.yaml', 'r') as file:
    items = yaml.safe_load(file)

selected_items = select_items(items)
total_cost = calculate_total_cost(selected_items)

print(f"Total cost: ${total_cost:.2f}")

change = calculate_change(total_cost)

print(f"Change owed: ${change:.2f}")


input(f"{Fore.GREEN}Enter {Fore.WHITE}to {Fore.RED}Continue")
select_items(items)

