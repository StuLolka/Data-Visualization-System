from FigureCanvas import FigureCanvas
from datatest import df
from setup_ui import *
from constants import *

print(get_style_number(id))

win = setup_win('LoL')
main_frame = setup_main_frame(win)
columns = df.select_dtypes(include='number').columns[1:]

x = df[columns[0]]
y = df[columns[0]]

figure_canvas = FigureCanvas(main_frame, x, y, columns[0], columns[0])


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
