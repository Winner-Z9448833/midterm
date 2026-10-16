import tkinter as tk

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        label.config(text=f"Result: {result}")
    except ValueError:
        label.config(text="Please enter valid numbers")

window = tk.Tk()
window.title("Multiply App")
window.geometry("400x300")

label = tk.Label(window, text="Enter two numbers to multiply", font=("Arial", 12))
label.pack(pady=20)

entry_frame = tk.Frame(window)
entry_frame.pack(pady=10)

entry1 = tk.Entry(entry_frame, width=10, font=("Arial", 14))
entry1.pack(side="left", padx=5)

entry2 = tk.Entry(entry_frame, width=10, font=("Arial", 14))
entry2.pack(side="left", padx=5)

button = tk.Button(window, text="Multiply", font=("Arial", 12), command=multiply)
button.pack(pady=20)

window.mainloop()