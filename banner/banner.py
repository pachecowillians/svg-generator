import cairo
import numpy

sizes = [(250, 250), (468, 60), (970, 250), (970, 90)]

for size in sizes:

    with cairo.SVGSurface("banner/img/{}x{}.svg".format(size[0], size[1]), size[0], size[1]) as surface:

        context = cairo.Context(surface)

        w = size[0]

        h = size[1]

        s = "{} x {}".format(size[0], size[1])

        context.rectangle(0, 0, w, h)

        color = list(numpy.random.choice(range(256), size=3))

        context.set_source_rgba(color[0]/255, color[1]/255, color[2]/255, 1)

        context.fill()

        context.select_font_face(
            "Inter", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

        context.set_font_size((min(w, h))*0.3)

        (x, y, width, height, dx, dy) = context.text_extents(s)

        factor = 0.3

        while width > max(w, h) * 0.7:
            factor -= 0.1
            context.set_font_size((min(w, h))*factor)
            (x, y, width, height, dx, dy) = context.text_extents(s)

        context.set_source_rgb(255/255, 255/255, 255/255)
        context.move_to(w/2 - width/2 - x, h/2 + height/2)
        context.show_text(s)

    print("File {}.svg Saved".format(s))
