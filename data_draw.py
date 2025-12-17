import tkinter as tk

from tkinter import colorchooser

from matplotlib import colormaps
from FigureCanvas import FigureCanvas
from datatest import df
import random
from setup_ui import *
from SunkenButton import SunkenButton
from constants import get_bold, color_val
from ColorButton import ColorButton

win = setup_win('LoL')
main_frame = setup_main_frame(win)
figure_frame = setup_figure_frame(main_frame)
columns = df.columns[1:]

x = df[columns[0]]
y = df[columns[0]]

default_cmap = "magma"
opt = tk.StringVar(value=default_cmap)

colors = random.sample(colormaps(), 29)
if default_cmap not in colors:
    colors.pop(random.randrange(len(colors)))
    colors.append(default_cmap)
colors = sorted(colors)

figure_canvas = FigureCanvas(figure_frame, x, y, columns[0], columns[0], task_number=3, cmap=default_cmap)


settings_frame = setup_top_settings_frame(figure_frame)

colors_menu = tk.OptionMenu(settings_frame, opt, *colors, command=figure_canvas.set_cmap)
colors_menu.grid(row=0, column=0)

def on_paint_toggle(is_on):
    if is_on:
        figure_canvas.turn_on_paint_mode()
    else:
        figure_canvas.turn_off_paint_mode()


paint_button = SunkenButton(settings_frame, text="Рисование", command=on_paint_toggle)
# paint_button.configure(command=lambda button=paint_button: paint_button_clicked(button))
paint_button.grid(row=0, column=1, pady=15, padx=15)

bold_label = tk.Label(settings_frame, text='Толщина:')
bold_label.grid(row=0, column=2, pady=15)

def on_key_release(event):
    current_value = bold_field.get()
    figure_canvas.set_bold(current_value)

default_bold = tk.StringVar(value=get_bold())
bold_field = tk.Entry(settings_frame, textvariable=default_bold, width=3)
bold_field.bind("<KeyRelease>", on_key_release)
bold_field.grid(row=0, column=3)

space_frame = tk.Frame(settings_frame, width=15)
space_frame.grid(row=0, column=4, pady=15)

color_label = tk.Label(settings_frame, text='Цвет:')
color_label.grid(row=0, column=5, pady=15)

blank_image = tk.PhotoImage(width=1, height=1)
color_button = ColorButton(settings_frame, width=25, height=25, bg=color_val)

def choose_color(event=None):
    color_code = colorchooser.askcolor(title="Choose color")

    if color_code[1]:
        color = color_code[1]
        color_button.set_bg(bg=color)
        figure_canvas.set_pen_color(color)

color_button.set_command(command=choose_color)
color_button.grid(row=0, column=6, pady=15, sticky=tk.W)


save_button = tk.Button(main_frame, text='Сохранить', command=figure_canvas.save_figure)
save_button.grid(row=1, column=0, sticky=tk.NW, pady=5, ipadx=5)

def y_button_pressed(y, name, paint_button):
    figure_canvas.set_y(y, name)
    paint_button.disable_press_effect()

def x_button_pressed(x, name, paint_button):
    figure_canvas.set_x(x, name)
    paint_button.disable_press_effect()

Y_buttons = setup_Y_buttons(main_frame, columns)
for button in Y_buttons:
    name = button['text']
    button.configure(command=lambda y=df[name], name=name, paint_button=paint_button: y_button_pressed(y, name, paint_button))

X_buttons = setup_X_buttons(main_frame, columns)
for button in X_buttons:
    name = button['text']
    button.configure(command=lambda x=df[name], name=name, paint_button=paint_button: x_button_pressed(x, name, paint_button))

def right_button_pressed(event=None):
    figure_canvas.turn_off_paint_mode()
    paint_button.disable_press_effect()


main_frame.bind_all("<Button-3>", right_button_pressed)
win.mainloop()