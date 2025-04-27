import svg
from base import *

def make_stabs(t, conf):
    plate_width = 140
    plate_height = 96
    thickness = 3
    elms = [
        svg_trapezoid([svg.Translate(0, i*5)], conf, plate_width, plate_width - 2 * thickness, thickness) 
        for i in range(0, 4)
    ]
    elms += [
        svg_trapezoid([svg.Translate(0, 20+i*5)], conf, plate_height, plate_height - 2 * thickness, thickness)
        for i in range(0, 4)
    ]
    return svg.G(
        transform=t,
        elements = elms
    )

def make_plate_walls(t, conf):
    plate_width = 140
    plate_height = 96
    elms = [
        svg.Rect(
            x=17*i,
            y=0,
            width=15,
            height=plate_height
        )
        for i in range(0, 4)
    ]
    return svg.G(
        transform=t,
        elements = elms
    )

def make_plate_clampers(t, conf):
    plate_width = 140
    plate_height = 96
    elms = [
        svg.Rect(
            x=0,
            y=10*i,
            width=plate_height,
            height=7
        )
        for i in range(0, 4)
    ]
    return svg.G(
        transform=t,
        elements = elms
    )