import cairo
import math

for c in range(ord('A'), ord('Z') + 1):

    with cairo.SVGSurface("avatar/img/{}.svg".format(chr(c)), 700, 700) as surface:

        context = cairo.Context(surface)

        w = h = 700

        s = chr(c)
        

        context.arc(350, 350, 350, 0, 2*math.pi)

        context.set_source_rgba(40/255, 42/255, 54/255, 1)

        context.fill()

        context.select_font_face(
            "Inter", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        context.set_font_size(w*0.6)
        (x, y, width, height, dx, dy) = context.text_extents(s[0])

        context.set_source_rgb(255/255, 255/255, 255/255)
        context.move_to(w/2 - width/2 - x, h/2 + height/2)
        context.show_text(s[0])


    print("File {}.svg Saved".format(s))
