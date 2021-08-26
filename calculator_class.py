import tkinter as tk
from typing import List
import math
import re

class Calculator:
    def __init__(self, root: tk.Tk, label: tk.Label, display: tk.Entry, buttons: List[List[tk.Button]]):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons
    
    def start(self):
        self.config_buttons()
        self.config_display()
        self.root.mainloop()

    def config_buttons(self):
        buttons = self.buttons
        for row_index, row_value in enumerate(buttons):
            for button in row_value:
                button_text = button['text']

                if button_text == 'C':
                    button.bind('<Button-1>', self.clear)
                    button.config(background = '#EA4335', foreground = '#ffffff')
                    self.label.config(text = 'Ainda não existem valores')

                if button_text in '0123456789.+-/*^()':
                    button.bind('<Button-1>', self.add_text_to_display)
                
                if button_text == '=':
                    button.bind('<Button-1>', self.calculate)
                    button.config(background = '#4785F4', foreground = '#ffffff')
    
    def config_display(self):
        self.display.bind('<Return>', self.calculate)
        self.display.bind('<KP_Enter>', self.calculate)
    
    def fix_text(self, text):
        # Substitui tudo o que não for 0123456789.+-/*^
        text = re.sub(r'[^\d\.\/\*\-\+\^\(\)e]', r'', text, 0)
        # Substitui sinais repetidos
        text = re.sub(r'([\.\+\/\-\*\^])\1', r'\1', text, 0)
        # Substitui () ou *() para nada
        text = re.sub(r'\*?\(\)', '', text)
    
        return text

    def clear(self, event = None):
        self.display.delete(0, 'end')
    
    def add_text_to_display(self, event = None):
        self.display.insert('end', event.widget['text'])
    
    def calculate(self, event = None):
        fixed_text = self.fix_text(self.display.get())
        equations = self.get_equations(fixed_text)

        try:
            if len(equations) == 1:
                result = eval(self.fix_text(equations[0]))
            else:
                result = eval(self.fix_text(equations[0]))
                for equation in equations[1:]:
                    result = math.pow(result, eval(self.fix_text(equation)))
            
            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.label.config(text = f'{fixed_text} = {result}')
        except OverflowError:
            self.label.config(text = 'Resultado muito grande')
        except Exception:
            self.label.config(text = 'Conta inválida')
    
    def get_equations(self, text):
        return re.split(r'\^', text, 0)

