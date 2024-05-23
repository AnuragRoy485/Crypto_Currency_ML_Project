import json
import re
import tkinter as tk
from tkinter import messagebox

# Load the JSON data from the file
try:
    with open('crypto_address_patterns.json', 'r') as file:
        crypto_address_patterns = json.load(file)
except FileNotFoundError:
    messagebox.showerror("Error", "The file 'crypto_address_patterns.json' was not found.")
    exit(1)
except json.JSONDecodeError:
    messagebox.showerror("Error", "Error decoding JSON from the file 'crypto_address_patterns.json'.")
    exit(1)

def find_matches(address):
    matches = []
    for crypto in crypto_address_patterns:
        name = crypto['name']
        symbol = crypto['symbol']
        patterns = crypto['patterns']
        for pattern in patterns:
            if re.match(pattern, address):
                matches.append({
                    'name': name,
                    'symbol': symbol,
                    'pattern': pattern
                })
    return matches

def on_search():
    address = entry.get().strip()
    matches = find_matches(address)

    if matches:
        result_text = f'The address {address} matches the following cryptocurrencies:\n'
        for match in matches:
            result_text += f"  - {match['name']} ({match['symbol']}), Pattern: {match['pattern']}\n"
    else:
        result_text = f'The address {address} does not match any known cryptocurrency patterns.'

    result_label.config(text=result_text)

# Create the main window
root = tk.Tk()
root.title("Cryptocurrency Address Checker")

# Create and place the widgets
entry_label = tk.Label(root, text="Enter the cryptocurrency address:")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=on_search)
search_button.pack(pady=5)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()
