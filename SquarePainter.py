from Painter import Painter

class SquarePainter(Painter):
    def __init__(self, canvas, color="#000000", bold=5, hold_ms=500):
        super().__init__(canvas, color, bold)

        self.hold_ms = hold_ms
        self._pressed = False
        self._after_id = None

    def start(self):
        super().start(self.__on_press, self.__on_release)

    def __on_press(self, event):
        self._pressed = True
        self._press_x = event.x
        self._press_y = event.y

        self._after_id = self.widget.after(self.hold_ms, self.__draw_if_still_pressed)

    def __on_release(self, event):
        self._pressed = False
        if self._after_id is not None:
            self.widget.after_cancel(self._after_id)
            self._after_id = None

    def __draw_if_still_pressed(self):
        if not self._pressed:
            return

        r = max(1, int(self.bold)) // 2
        self.widget.create_rectangle(
            self._press_x - r,
            self._press_y - r,
            self._press_x + r,
            self._press_y + r,
            fill=self.color,
            outline=""
        )

