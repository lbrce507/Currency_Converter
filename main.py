import tkinter as tk
from tkinter import ttk
from currency_converter import CurrencyConverter

# Initialize CurrencyConverter
c = CurrencyConverter()

# Function to convert currency
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()
        converted_amount = c.convert(amount, from_currency, to_currency)
        label_result.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")
    except Exception as e:
        label_result.config(text=f"Error: {e}")

# Create main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# Currency options
currencies = list(c.currencies)

# Amount Entry
label_amount = tk.Label(root, text="Enter Amount:")
label_amount.pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

# From Currency Dropdown
label_from = tk.Label(root, text="From Currency:")
label_from.pack()
combo_from = ttk.Combobox(root, values=currencies)
combo_from.pack()
combo_from.set("USD")

# To Currency Dropdown
label_to = tk.Label(root, text="To Currency:")
label_to.pack()
combo_to = ttk.Combobox(root, values=currencies)
combo_to.pack()
combo_to.set("INR")

# Convert Button
button_convert = tk.Button(root, text="Convert", command=convert_currency)
button_convert.pack()

# Result Label
label_result = tk.Label(root, text="Converted Amount:")
label_result.pack()

# Run GUI
root.mainloop()
