import tkinter as tk
from typing import List

def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculadora')
    root.iconbitmap('icon.ico')
    root.config(padx = 10, pady = 10, background = '#ffffff')
    root.resizable(False, False)
    return root

def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text = 'Ainda não existem valores', 
        anchor = 'e', justify = 'right', background = '#ffffff'
    )
    label.grid(
        row = 0, column = 0, columnspan = 5, 
        sticky = 'news'
    )
    return label

def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(
        row = 1, column = 0, columnspan = 5, 
        sticky = 'news', pady = (0, 10)
    )
    display.config(
        font = ('Helvetica', 40, 'bold'), 
        justify = 'right', border = 1, relief = 'flat',
        highlightthickness = 1, highlightcolor = '#cccccc'
    )
    display.bind('<Control-a>', display_control_a)
    return display

def display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'

def make_buttons(root) -> List[List[tk.Button]]:
    button_text: List[List[str]] = [
        ['7','8','9','+','C'],
        ['4','5','6','-','/'],
        ['1','2','3','*','^'],
        ['0','.','(',')','='],
    ]

    buttons: List[List[tk.Button]] = []

    for row_index, row_value in enumerate(button_text, start = 2):
        button_row = []
        for column_index, column_value in enumerate(row_value):
            button = tk.Button(root, text = column_value)
            button.grid(
                row = row_index, column = column_index, 
                sticky = 'news', padx = 5, pady = 5
            )
            button.config(
                font = ('Helvetica', 15, 'normal'),
                pady = 40, width = 1, background = '#f1f2f3', 
                border = 0, cursor = 'hand2', 
                highlightthickness = 0, highlightcolor = '#cccccc', highlightbackground = '#cccccc',
                activebackground = '#cccccc'
            )
            button_row.append(button)
        buttons.append(button_row)
    return buttons
