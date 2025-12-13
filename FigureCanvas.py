from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import colormaps
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import tkinter as tk

class FigureCanvas:

    def __init__(self, frame, x, y, xlabel, ylabel, task_number=2, cmap="magma"):
        self.__x = x
        self.__y = y
        self.__xlabel = xlabel
        self.__ylabel = ylabel
        self.__frame = frame
        self.__task_number = task_number
        self.__cmap = cmap
        self.create_canvas()

    def create_canvas(self):
        self.__fig = Figure(figsize=(10, 7))
        self.__ax = self.__fig.add_subplot()
        self.__ax.set_xlabel(self.__xlabel)
        self.__ax.set_ylabel(self.__ylabel)
        self.__canvas = FigureCanvasTkAgg(self.__fig, master=self.__frame)
        row = 1 if self.__task_number == 3 else 0
        self.__canvas.get_tk_widget().grid(row=row, column=1, sticky=tk.NW, padx=5, pady=5)
        if np.dtype(self.__x) != object and np.dtype(self.__y) != object:
            self.__draw_numerics()
        else:
            self.__draw_objects()
        self.__fig.tight_layout()
        self.__canvas.draw()

    def __draw_numerics(self):
        if self.__xlabel == self.__ylabel and self.__task_number == 3:
            _, _, patches = self.__ax.hist(self.__x, bins=10)
            norm = plt.Normalize(vmin=0, vmax=len(patches) - 1)
            cmap = colormaps[self.__cmap]
            for i, patch in enumerate(patches):
                patch.set_facecolor(cmap(norm(i)))
        else:
            x = self.__x.to_numpy()
            c = x if self.__task_number == 3 else None
            cmap = self.__cmap if self.__task_number == 3 else None
            self.__ax.scatter(x, self.__y.to_numpy(), marker='<', c=c, cmap=cmap)

    def __draw_objects(self):
        if np.dtype(self.__x) == object and np.dtype(self.__y) == object and self.__xlabel == self.__ylabel:
                value_counts = self.__x.value_counts()
                labels = [a + ": " + str(b) for a, b in zip(value_counts.index, value_counts.values)] if len(value_counts) < 20 else value_counts.values
                self.__ax.set_ylabel('')
                cmap = colormaps[self.__cmap]
                colors = cmap(np.linspace(0, 1, len(value_counts.values)))
                self.__ax.pie(value_counts.values, labels=labels, colors=colors)
        elif np.dtype(self.__x) == object:
            value_counts = self.__x.value_counts()
            cmap = colormaps[self.__cmap]

            labels = value_counts.index.astype(str)
            colors = cmap(np.linspace(0, 1, len(labels)))
            self.__ax.bar(labels, value_counts.values, color=colors)
            self.__ax.set_ylabel('')
            if len(labels) > 21:
                self.__ax.set_xticklabels([s[:2] for s in labels])

        else:
            x_aligned, y_aligned = self.__x.align(self.__y, join="inner")
            groups = [g.dropna().to_numpy() for _, g in x_aligned.groupby(y_aligned)]
            labels = [str(k) for k in y_aligned.dropna().unique()]
            cmap = colormaps[self.__cmap]
            colors = cmap(np.linspace(0, 1, len(groups)))
            bp = self.__ax.boxplot(groups, labels=labels, patch_artist=True, vert=False)
            for box, color in zip(bp["boxes"], colors):
                box.set_facecolor(color)



    def set_x(self, x, xlabel):
        self.__x = x
        self.__xlabel = xlabel
        self.__ax.clear()
        self.create_canvas()

    def set_y(self, y, ylabel):
        self.__y = y
        self.__ylabel = ylabel
        self.__ax.clear()
        self.create_canvas()

    def set_cmap(self, cmap):
        self.__cmap = cmap
        self.__ax.clear()
        self.create_canvas()

    def save_figure(self):
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        self.__fig.savefig(f'graph{current_time}.png')




