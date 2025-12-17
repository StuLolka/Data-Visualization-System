import tkinter as tk

class SunkenButton(tk.Frame):
    def __init__(self, master, text, command=None, **kw):
        super().__init__(master, bd=2, relief=tk.RAISED, bg='white', **kw)
        self._pressed = False
        self._command = command

        self.label = tk.Label(self, text=text, bg='white')
        self.label.pack(padx=10, pady=4)

        # клики по фрейму и по лейблу
        for w in (self, self.label):
            w.bind("<Button-1>", self._toggle)

    def disable_press_effect(self):
        if self._pressed:
            self._toggle()

    def change_press_effect(self):
        if self._pressed:
            self.config(relief=tk.SUNKEN)
            self.configure(bg='#D3D3D3')
            self.label.configure(bg='#D3D3D3')
        else:
            self.config(relief=tk.RAISED)
            self.configure(bg='white')
            self.label.configure(bg='white')


    def _toggle(self, event=None):
        self._pressed = not self._pressed
        self.change_press_effect()

        if self._command:
            self._command(self._pressed)

