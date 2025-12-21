class Painter:
    def __init__(self, canvas, color="#000000", bold=5,):
        self.canvas = canvas
        self.color = color
        self.bold = bold

        self.widget = self.canvas.get_tk_widget()

    def set_color(self, color):
        self.color = color

    def set_bold(self, bold):
        self.bold = bold

    def start(self, on_press, on_release):
        self.widget.bind("<Button-1>", on_press)
        self.widget.bind("<ButtonRelease-1>", on_release)

        self.widget.config(cursor="pencil")

    def stop(self):
        self.widget.unbind("<Button-1>")
        self.widget.unbind("<ButtonRelease-1>")

        self.widget.config(cursor="arrow")