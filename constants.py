my_id = '70214517'
cmap = 'magma'

def get_style_number(id=my_id):
    style_number = sum([int(i) for i in id])
    if style_number < 10:
        return style_number
    style_number = str(style_number)
    return get_style_number(style_number)

def get_rgb(id=my_id):
    return int(id[-6:-4]), int(id[-4:-2]), int(id[-2:])

def get_bold(id=my_id):
    return get_style_number() // 2 +5



color_val = "#%02x%02x%02x" % get_rgb()

print(color_val)

