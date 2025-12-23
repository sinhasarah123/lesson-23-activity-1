import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("400x300")
window.title("- Getting Started with Widgets")
window.config(bg="#f1116a")

# Title label
title_label = tk.Label(window, text="Multiply Two Numbers", font=("Arial", 14, "bold"), bg="#25b8cf", fg="#756868")
title_label.pack(pady=10)

# Label for first number
label1 = tk.Label(window, text="Enter First Number:", bg="#04181d", fg="#06B948", font=("Arial", 10))
label1.pack(pady=5)

# Entry widget for first number
entry1 = tk.Entry(window, width=30, bg="#eae318", fg="#E72424", borderwidth=2)
entry1.pack(pady=5)

# Label for second number
label2 = tk.Label(window, text="Enter Second Number:", bg="#f0f0f0", fg="#555555", font=("Arial", 10))
label2.pack(pady=5)

# Entry widget for second number
entry2 = tk.Entry(window, width=30, bg="#398092", fg="#CE7023", borderwidth=2)
entry2.pack(pady=5)

# Function to calculate product
def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(1.0, f"Product: {product}")
        result_text.config(state=tk.DISABLED)
    except ValueError:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(1.0, "Please enter valid numbers")
        result_text.config(state=tk.DISABLED)

# Calculate button
calc_button = tk.Button(window, text="Calculate", command=calculate_product, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=20)
calc_button.pack(pady=10)

# Result text widget
result_text = tk.Text(window, height=3, width=40, bg="#e8f5e9", fg="#2e7d32", borderwidth=2, state=tk.DISABLED)
result_text.pack(pady=10)

window.mainloop()