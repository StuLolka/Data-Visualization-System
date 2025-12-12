from tkinter import ttk

from pygments.lexer import include
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from FigureCanvas import FigureCanvas
from datatest import df
import tkinter as tk

def get_style_number(id):
    style_number = sum([int(i) for i in id])
    if style_number < 10:
        return style_number
    style_number = str(style_number)
    return get_style_number(style_number)

print(get_style_number('70214517'))

def setup_win(window_title):
    win = tk.Tk()
    win.title(window_title)
    width = 1200
    height = 600
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = int(screen_width/2 - width/2)
    y = int(screen_height/2 - height/2)
    win.geometry(f"{width}x{height}+{x}+{y}")
    return win

def setup_main_frame(win):
    frame = tk.Frame(win)
    frame.pack(expand=True, fill='both')
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    return frame

win = setup_win('LoL')
frame = setup_main_frame(win)
columns = df.select_dtypes(include='number').columns[1:]

x = df[columns[0]].to_numpy()
y = df[columns[0]].to_numpy()

canvas_axes = FigureCanvas(frame, x, y, columns[0], columns[0])


def set_x(x, xlabel):
    canvas_axes.set_x(x, xlabel)

def set_y(y, ylabel):
    canvas_axes.set_y(y, ylabel)

def save():
    canvas_axes.save_figure()

def setup_X_buttons(frame, cols):
    if not len(cols): return []

    buttons_frame = tk.Frame(frame)
    buttons_frame.grid(row=1, column=1, sticky=tk.NW, pady=5, ipadx=5)
    # buttons_frame.columnconfigure(0, weight=1)
    for index, name in enumerate(cols):
        button = tk.Button(buttons_frame, text=name)
        row = index // 7
        column = index % 7
        button.grid(row=row, column=column, sticky=tk.W)
        # button.grid(row=0, column=index, sticky=tk.W)

        button.configure(command=lambda x=df[name].to_numpy(), name=name: set_x(x, name))

def setup_Y_buttons(frame, cols):
    if not len(cols): return []

    buttons_frame = tk.Frame(frame)
    buttons_frame.grid(row=0, column=0, sticky=tk.NW, pady=5, ipadx=5)
    # buttons_frame.columnconfigure(0, weight=1)
    for index, name in enumerate(cols):
        button = tk.Button(buttons_frame, text=name)
        button.grid(row=index, column=0, sticky=tk.W)
        button.configure(command=lambda y=df[name].to_numpy(), name=name: set_y(y, name))

save_button = tk.Button(frame, text='Сохранить', command=save)
save_button.grid(row=1, column=0, sticky=tk.NW, pady=5, ipadx=5)

setup_Y_buttons(frame, columns)
setup_X_buttons(frame, columns)
win.mainloop()
