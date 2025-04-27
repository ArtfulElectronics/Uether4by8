### Common SVG shapes and layout utilities

import svg

def svg_trapezoid(t, conf, base, width, height):
    d = (base - width) / 2
    return svg.G(
        transform=t,
        elements = [
            svg.Path(
                d = [
                    svg.MoveTo(d, 0),
                    svg.LineTo(d + width, 0),
                    svg.LineTo(base, height),
                    svg.LineTo(0, height),
                    svg.ClosePath(),
                ]
            ),
        ]
   )

def gen_grid(num_rows, num_cols, num_elms, spacing, startx, starty):
    S = []
    c = 0
    for i in range(num_rows):
        for j in range(num_cols):
            S.append( [svg.Translate(startx + j * spacing, starty + i * spacing)] )
            c = c + 1
            if c == num_elms:
                break
    return S