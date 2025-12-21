import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def setup_win(window_title):
    win = tk.Tk()
    win.title(window_title)
    win.geometry("{0}x{1}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight()))
    return win

def setup_main_frame(win):
    frame = tk.Frame(win)
    frame.pack(expand=True, fill='both')
    return frame

def setup_figure_frame(main_frame):
    frame = tk.Frame(main_frame)
    frame.grid(row=0, column=1)
    return frame

def setup_cmap_frame(main_frame, cmap_var, *cmaps, command):
    frame = tk.Frame(main_frame)
    frame.grid(row=0, column=0, sticky=tk.NW)
    cmap_label = tk.Label(frame, text='cmap:')
    cmap_label.grid(row=0, column=0, ipadx=0)
    cmap_menu = tk.OptionMenu(frame, cmap_var, *cmaps, command=command)
    cmap_menu.grid(row=0, column=1, ipadx=0)

def setup_top_settings_frame(figure_frame):
    frame = tk.Frame(figure_frame)
    frame.grid(row=0, column=1, sticky=tk.NW)
    return frame

def setup_top_canvas_frame(frame):
    fig = Figure(figsize=(10, 1))
    fig.patch.set_facecolor('#f0f0f0')
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().grid(row=0, column=0)
    return canvas

def setup_X_buttons(frame, cols):
    if not len(cols): return []

    buttons_frame = tk.Frame(frame)
    buttons_frame.grid(row=2, column=1, sticky=tk.NW, pady=5, ipadx=5)
    buttons = []
    for index, name in enumerate(cols):
        button = tk.Button(buttons_frame, text=name)
        row = index // 10
        column = index % 10
        button.grid(row=row, column=column, sticky=tk.W, padx=2.5, pady=2.5)
        buttons.append(button)
        buttons.append(button)
        buttons.append(button)
    return buttons

def setup_Y_buttons(frame, cols):
    if not len(cols): return []

    buttons_frame = tk.Frame(frame)
    buttons_frame.grid(row=0, column=0, sticky=tk.NW, pady=5, ipadx=5)
    buttons = []
    for index, name in enumerate(cols):
        button = tk.Button(buttons_frame, text=name,)
        button.grid(row=index, column=0, sticky=tk.W, pady=2.5)
        buttons.append(button)
        buttons.append(button)
    return buttons