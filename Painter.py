import tkinter as tk

class Painter:
    __last_added_line_ids = []

    def __init__(self, canvas, pen_color=None, bold=None):
        self.canvas = canvas
        self.pen_color = pen_color
        self.bold = bold

        self._painting = False
        self._last = None

        self.widget = self.canvas.get_tk_widget()


    def start(self):
        self.widget.bind("<Button-1>", self.__start_paint)
        self.widget.bind("<B1-Motion>", self.__paint)
        self.widget.bind("<ButtonRelease-1>", self.__stop_paint)

    def stop(self):
        self.widget.unbind("<Button-1>")
        self.widget.unbind("<B1-Motion>")
        self.widget.unbind("<ButtonRelease-1>")

    def set_color(self, color):
        self.pen_color = color

    def set_bold(self, bold):
        self.bold = bold

    def remove_paint(self):
        for id in self.__last_added_line_ids:
            self.widget.delete(id)
        self.__last_added_line_ids = []
        self._painting = False
        self._last = None

    def __start_paint(self, event):
        self._painting = True
        self._last = (event.x, event.y)
        self.__last_added_line_ids = []

        r = float(self.bold) / 2
        dot = self.widget.create_oval(event.x - r, event.y - r, event.x + r, event.y + r,
                                fill=self.pen_color, outline="")
        self.__last_added_line_ids.append(dot)

    def __paint(self, event):
        if not self._painting or self._last is None:
            self.__last_added_line_ids = []
            return

        x0, y0 = self._last
        x1, y1 = event.x, event.y

        line = self.widget.create_line(
            x0, y0, x1, y1,
            fill=self.pen_color,
            width=self.bold,
            capstyle=tk.ROUND,     # круглые концы
            joinstyle=tk.ROUND,    # круглые стыки
            smooth=True,           # сглаживание
            splinesteps=12
        )

        self.__last_added_line_ids.append(line)
        self._last = (x1, y1)

    def __stop_paint(self, event):
        self._painting = False
        self._last = None
