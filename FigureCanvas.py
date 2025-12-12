from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

from datatest import df
import tkinter as tk

class FigureCanvas:
    __x = []
    __y = []
    __xlabel = ''
    __ylabel = ''
    __frame = None
    __fig = None

    def __init__(self, frame, x, y, xlabel, ylabel):
        self.__x = x
        self.__y = y
        self.__xlabel = xlabel
        self.__ylabel = ylabel
        self.__frame = frame
        self.create_canvas()

    def create_canvas(self):
        self.__fig = Figure(figsize=(10, 5))
        self.ax = self.__fig.add_subplot()
        self.ax.set_xlabel(self.__xlabel)
        self.ax.set_ylabel(self.__ylabel)
        canvas = FigureCanvasTkAgg(self.__fig, master=self.__frame)
        canvas.get_tk_widget().grid(row=0, column=1, sticky=tk.NW, padx=5, pady=5)
        self.ax.scatter(self.__x, self.__y, marker='<')
        canvas.draw()


    def set_x(self, x, xlabel):
        self.__x = x
        self.__xlabel = xlabel
        self.ax.clear()
        self.create_canvas()

    def set_y(self, y, ylabel):
        self.__y = y
        self.__ylabel = ylabel
        self.ax.clear()
        self.create_canvas()

    def save_figure(self):
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        self.__fig.savefig(f'graph{current_time}.png')


