import tkinter as tk

MAX_LENGTH = 20  # Character limit on display

def click_button(value):
    current = entry.get()

    # Character limit
    if len(current) >= MAX_LENGTH:
        return

    # Prevent operators at the beginning
    if current == '' and value in ('+', '*', '/'):
        return

    # Prevent two consecutive operators
    if current and current[-1] in '+-*/' and value in '+*/':
        return

    # Prevent multiple decimal points in the same number
    if value == '.':
        parts = current.split('+') + current.split('-') + current.split('*') + current.split('/')
        if '.' in parts[-1]:
            return

    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, text[:-1])

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result)[:MAX_LENGTH])
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

window = tk.Tk()
window.title("Safe Calculator")
window.configure(bg="#2b2b2b")

entry = tk.Entry(window, width=16, font=('Consolas', 30), borderwidth=0, bg="#3c3f41", fg="#ffffff", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10, ipady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('←', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('=', 5, 1, 3)
]

def create_button(text, row, column, colspan=1):
    colors = {
        'btn_bg': '#4a4a4a',
        'func_bg': '#ff9500',
        'erase_bg': '#d9534f',
        'fg': '#ffffff',
    }
    if text in ('C', '←'):
        bg_color = colors['erase_bg']
    elif text == '=' or text in ('/', '*', '-', '+'):
        bg_color = colors['func_bg']
    else:
        bg_color = colors['btn_bg']

    def cmd():
        if text == 'C':
            clear()
        elif text == '←':
            backspace()
        elif text == '=':
            calculate()
        else:
            click_button(text)

    button = tk.Button(window, text=text, bg=bg_color, fg=colors['fg'], font=('Consolas', 24),
                       borderwidth=0, command=cmd)
    button.grid(row=row, column=column, columnspan=colspan, sticky="nsew", padx=5, pady=5)

for b in buttons:
    if len(b) == 3:
        create_button(b[0], b[1], b[2])
    else:
        create_button(b[0], b[1], b[2], b[3])

for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

window.mainloop()

# by sixsdev
