import tkinter as tk

def setup_win(window_title):
    win = tk.Tk()
    # win.configure(background='white')
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

def setup_X_buttons(frame, cols):
    if not len(cols): return []

    buttons_frame = tk.Frame(frame)
    buttons_frame.grid(row=2, column=1, sticky=tk.NW, pady=5, ipadx=5)
    buttons = []
    for index, name in enumerate(cols):
        button = tk.Button(buttons_frame, text=name)
        row = index // 7
        column = index % 7
        button.grid(row=row, column=column, sticky=tk.W)
        buttons.append(button)
    return buttons

def setup_Y_buttons(frame, cols):
    if not len(cols): return []

    buttons_frame = tk.Frame(frame)
    buttons_frame.grid(row=0, column=0, sticky=tk.NW, pady=5, ipadx=5)
    buttons = []
    for index, name in enumerate(cols):
        button = tk.Button(buttons_frame, text=name,)
        button.grid(row=index, column=0, sticky=tk.W)
        buttons.append(button)
    return buttons