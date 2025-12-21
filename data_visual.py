from matplotlib import colormaps
from FigureCanvas import FigureCanvas
from dataset import df
import random
from setup_ui import *
from constants import cmap

win = setup_win('LoL')
main_frame = setup_main_frame(win)
figure_frame = setup_figure_frame(main_frame)
columns = df.columns[1:]

x = df[columns[0]]
y = df[columns[0]]

default_cmap = cmap
cmap_var = tk.StringVar(value=default_cmap)

cmaps = random.sample(colormaps(), 29)
if default_cmap not in cmaps:
    cmaps.pop(random.randrange(len(cmaps)))
    cmaps.append(default_cmap)
cmaps = sorted(cmaps)

figure_canvas = FigureCanvas(figure_frame, x, y, columns[0], columns[0], task_number=3, cmap=default_cmap)

cmap_frame = setup_cmap_frame(figure_frame, cmap_var, *cmaps, command=figure_canvas.set_cmap)


save_button = tk.Button(main_frame, text='Сохранить', command=figure_canvas.save_figure)
save_button.grid(row=1, column=0, sticky=tk.NW, pady=5, ipadx=5)

Y_buttons = setup_Y_buttons(main_frame, columns)
for button in Y_buttons:
    name = button['text']
    button.configure(command=lambda y=df[name], name=name: figure_canvas.set_y(y, name))

X_buttons = setup_X_buttons(main_frame, columns)
for button in X_buttons:
    name = button['text']
    button.configure(command=lambda x=df[name], name=name: figure_canvas.set_x(x, name))

win.mainloop()