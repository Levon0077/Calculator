import tkinter as tk


def click(event):
    current = entry.get()
    if event.widget.cget("text") == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif event.widget.cget("text") == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, event.widget.cget("text"))


root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=16, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    if button in ['+', '-', '*', '/']:
        btn = tk.Button(root, text=button, font=('Arial', 18), width=4, height=2, bg='orange', fg='white')
    else:
        btn = tk.Button(root, text=button, font=('Arial', 18), width=4, height=2, bg='black', fg='white')

    btn.grid(row=row_val, column=col_val)
    btn.bind("<Button-1>", click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
