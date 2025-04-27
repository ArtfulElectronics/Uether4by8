import svg

from base import *

def svg_keycap(t, num_u, conf):
    kc_dim = conf.keycap_u * num_u # Keycap horizontal dimension in mm (from number of u)
    return svg.Rect(
        transform=t,
        x=-kc_dim/2,
        y=-conf.keycap_u / 2,
        rx=1.5,
        ry=1.5,
        width=kc_dim,
        height=conf.keycap_u
    )

def svg_keycap_stem(t, conf):
    x = 0
    y = 0
    w1 = conf.keycap_stem_vert_rect_width/2   # half the width of the vertical rectangle
    w2 = conf.keycap_stem_horiz_rect_width/2  # half the width of the horizontal rectangle
    h  = conf.keycap_stem_cross_length/2      # half the length of the rectangles in the + sign
    sr = conf.keycap_stem_dia/2               # radius of the stem circle
    return svg.G(
        transform=t,
        elements = [
            svg.Circle(
                cx=x,
                cy=y,
                r=sr
            ),
            svg.Path(
                d = [
                    svg.MoveTo(x - w1, y - h),
                    svg.LineTo(x + w1, y - h),
                    svg.LineTo(x + w1, y - w2), # Intersection 1
                    svg.LineTo(x + h, y - w2),
                    svg.LineTo(x + h, y + w2),
                    svg.LineTo(x + w1, y + w2), # Intersection 2
                    svg.LineTo(x + w1, y + h),
                    svg.LineTo(x - w1, y + h),
                    svg.LineTo(x - w1, y + w2), # Intersection 3
                    svg.LineTo(x - h, y + w2),
                    svg.LineTo(x - h, y - w2),
                    svg.LineTo(x - w1, y - w2), # Intersection 4
                    svg.ClosePath(),
                ]
            ),
        ]
   )

