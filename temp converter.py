import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("420x180")

# Celsius to Fahrenheit conversion function
def celsius_to_fahrenheit():
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9 / 5) + 32
    result_label.config(text=f"{celsius}°C = {fahrenheit}°F")

# Fahrenheit to Celsius conversion function
def fahrenheit_to_celsius():
    fahrenheit = float(fahrenheit_entry.get())
    celsius = (fahrenheit - 32) * 5 / 9
    result_label.config(text=f"{fahrenheit}°F = {celsius}°C")
    
# Celsius to Fahrenheit conversion section
celsius_label = tk.Label(window, text="Celsius")
celsius_label.pack()

celsius_entry = tk.Entry(window)
celsius_entry.pack()

celsius_to_fahrenheit_button = tk.Button(window, 
text="Convert to Fahrenheit", command=celsius_to_fahrenheit)

celsius_to_fahrenheit_button.pack()

# Fahrenheit to Celsius conversion section
fahrenheit_label = tk.Label(window, text="Fahrenheit")
fahrenheit_label.pack()

fahrenheit_entry = tk.Entry(window)
fahrenheit_entry.pack()

fahrenheit_to_celsius_button = tk.Button(window, 
text="Convert to Celsius", command=fahrenheit_to_celsius)

fahrenheit_to_celsius_button.pack()

# Result section
result_label = tk.Label(window, text="")
result_label.pack()


window.mainloop()