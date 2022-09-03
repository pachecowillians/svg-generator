import cairo
import math

with cairo.SVGSurface("avatar/geek.svg", 700, 700) as surface:

    context = cairo.Context(surface)

    w = h = 700

    s = "W"

    context.arc(350, 350, 350, 0, 2*math.pi)

    context.set_source_rgba(40/255, 42/255, 54/255, 1)

    context.fill()

    context.set_source_rgb(255/255, 255/255, 255/255)

    context.select_font_face(
        "Courier", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    context.set_font_size(w*0.9)
    (x, y, width, height, dx, dy) = context.text_extents(s)

    print(x, y, width, height, dx, dy)

    context.set_source_rgb(255/255, 255/255, 255/255)
    context.move_to(w/2 - width/2 - x, h/2 + height/2)
    context.show_text(s)


# printing message when file is saved
print("File Saved")
