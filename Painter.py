import tkinter as tk

class Painter:
    def __init__(self, canvas, pen_color=None, bold=None):
        self.canvas = canvas
        self.pen_color = pen_color
        self.bold = bold  # толщина кисти

        self._painting = False
        self._last = None  # (x, y)

        w = self.canvas  # tk.Canvas

        w.bind("<Button-1>", self._start_paint)
        w.bind("<B1-Motion>", self._paint)
        w.bind("<ButtonRelease-1>", self._stop_paint)

    def _start_paint(self, event):
        self._painting = True
        self._last = (event.x, event.y)

        # точка, чтобы был след даже при клике без движения
        r = self.bold / 2
        self.canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r,
                                fill=self.pen_color, outline="")

    def _paint(self, event):
        if not self._painting or self._last is None:
            return

        x0, y0 = self._last
        x1, y1 = event.x, event.y

        self.canvas.create_line(
            x0, y0, x1, y1,
            fill=self.pen_color,
            width=self.bold,
            capstyle=tk.ROUND,     # круглые концы
            joinstyle=tk.ROUND,    # круглые стыки
            smooth=True,           # сглаживание
            splinesteps=12
        )

        self._last = (x1, y1)

    def _stop_paint(self, event):
        self._painting = False
        self._last = None
