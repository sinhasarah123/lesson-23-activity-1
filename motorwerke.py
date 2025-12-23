import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        
        dob = datetime(year, month, day)
        today = datetime.today()
        
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        messagebox.showinfo("Age", f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid date values")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")

tk.Label(root, text="Date of Birth Calculator", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Day:").pack()
entry_day = tk.Entry(root, width=20)
entry_day.pack()

tk.Label(root, text="Month:").pack()
entry_month = tk.Entry(root, width=20)
entry_month.pack()

tk.Label(root, text="Year:").pack()
entry_year = tk.Entry(root, width=20)
entry_year.pack()

tk.Button(root, text="Calculate Age", command=calculate_age, bg="blue", fg="white").pack(pady=10)

root.mainloop()