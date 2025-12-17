import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Paint")
        self.root.geometry("600x400")

        self.pen_color = "black"
        self.canvas = tk.Canvas(self.root, bg="white", bd=2, relief=tk.SOLID)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse motion event for drawing
        self.canvas.bind("<B1-Motion>", self.paint)

        # Color picker button
        self.color_button = tk.Button(self.root, text="Change Color", command=self.change_color)
        self.color_button.pack(side=tk.LEFT, padx=5, pady=5)

    def paint(self, event):
        # Draw a small oval (dot) at the current mouse position
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.pen_color, outline=self.pen_color)

    def change_color(self):
        # Open a color chooser dialog
        color = colorchooser.askcolor()
        if color[1]: # color[1] is the hex code
            self.pen_color = color[1]

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
