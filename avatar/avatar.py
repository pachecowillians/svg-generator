import cairo
import math
import numpy

for c in range(ord('A'), ord('Z') + 1):

    with cairo.SVGSurface("avatar/img/{}.svg".format(chr(c)), 48, 48) as surface:

        context = cairo.Context(surface)

        w = h = 48

        s = chr(c)
    
        context.arc(w/2, h/2, w/2, 0, 2*math.pi)

        color = list(numpy.random.choice(range(256), size=3))

        context.set_source_rgba(color[0]/255, color[1]/255, color[2]/255, 1)

        context.fill()

        context.select_font_face(
            "Inter", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        context.set_font_size(w*0.6)
        (x, y, width, height, dx, dy) = context.text_extents(s[0])

        context.set_source_rgb(255/255, 255/255, 255/255)
        context.move_to(w/2 - width/2 - x, h/2 + height/2)
        context.show_text(s[0])


    print("File {}.svg Saved".format(s))
