import tkinter as tk

class ColorButton(tk.Frame):
    def __init__(self, master, bg, command=None, **kw):
        super().__init__(master, bd=2, relief='raised', bg=bg, **kw)
        self._command = command
        self.bind("<Button-1>", self._command)

    def set_command(self, command=None):
        super().configure()
        self._command = command
        self.bind("<Button-1>", self._command)

    def set_bg(self, bg=None):
        self.configure(bg=bg)


