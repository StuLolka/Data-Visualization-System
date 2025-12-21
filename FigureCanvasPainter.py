import tkinter as tk
from Painter import Painter

class FigureCanvasPainter(Painter):
    __last_added_line_ids = []

    def __init__(self, canvas, color="#000000", bold=5,):
        super().__init__(canvas, color, bold)

        self._painting = False
        self._last = None

    def start(self):
        self.widget.bind("<B1-Motion>", self.__paint)
        super().start(self.__start_paint, self.__stop_paint)

    def stop(self):
        super().stop()
        self.widget.unbind("<B1-Motion>")

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
        dot = self.widget.create_oval(
            event.x - r,
            event.y - r,
            event.x + r,
            event.y + r,
            fill=self.color,
            outline="")
        self.__last_added_line_ids.append(dot)

    def __paint(self, event):
        if not self._painting or self._last is None:
            self.__last_added_line_ids = []
            return

        x0, y0 = self._last
        x1, y1 = event.x, event.y

        line = self.widget.create_line(
            x0, y0, x1, y1,
            fill=self.color,
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
