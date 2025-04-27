
import svg     # https://pypi.org/project/svg.py/

from base import *
from config import *
from keyswitch import *
from keycap import *
from keycapjig import *
from mcu import *
from rj45 import *
from extra import *
from plate import *

def gen_switches_transforms(for_left, sx, sy, w):
    u = 19.05
    CS = [3*u/8, u/8, 0, u/8, u/4]
    sx = u/2 + sx
    sy = u/2 + sy
    S = []
    for i in range(5):
        for j in range(3):
            xi = sx + i * u
            yi = sy + CS[i] + j * u
            if for_left:
                S.append([svg.Translate(xi, yi)])
            else:
                S.append([svg.Translate(w - xi, yi)])

    # Special transformations for the six thumb keys (don't know which one is best)
    x0 = sx + 4 * u         # Coordinate of the last switch in the grid
    y0 = sy + CS[4] + 2 * u
    x1 = x0 - 28.575
    y1 = y0 + u
    x2 = x0 - 7.760
    y2 = y0 + 21.227
    x3 = x0 + 14.081
    y3 = y0 + 23.308
    if for_left:
        S.append([svg.Translate(x1, y1), svg.Rotate(0)])
        S.append([svg.Translate(x2, y2), svg.Rotate(12)])
        S.append([svg.Translate(x3, y3), svg.Rotate(23)])
    else:
        S.append([svg.Translate(w - x1, y1), svg.Rotate(0)])
        S.append([svg.Translate(w - x2, y2), svg.Rotate(-12)])
        S.append([svg.Translate(w - x3, y3), svg.Rotate(-23)])

    return S

def make_plates(for_left, w, conf):
    S = gen_switches_transforms(for_left, 5, 5, w)

    top_elms = [svg_switch_mounting_plate(t, conf) for t in S]
    pcb_elms = [svg_switch_hotswap(t, conf) for t in S]
    bottom_elms = []

    # Add the MCU (left side only) and RJ45
    if for_left:
        nicenano_placement_transform = [svg.Translate(120, 45)]
        rj45_placement_transform = [svg.Translate(140-19+8, 5 + 8)]
        top_elms += [svg_nicenano_top(nicenano_placement_transform), svg_rj45_top(rj45_placement_transform)]
        pcb_elms += [svg_nicenano_pcb(nicenano_placement_transform), svg_rj45_pcb(rj45_placement_transform)]
    else:
        rj45_placement_transform = [svg.Translate(w - (140-19+8), 5 + 8), svg.Rotate(180)]
        top_elms += [svg_rj45_top(rj45_placement_transform)] # Rotate by 180 degrees
        pcb_elms += [svg_rj45_pcb(rj45_placement_transform)]

    if conf.with_key_cap:
        bottom_elms = [svg_keycap(t, conf) for t in S]

    if conf.with_plate_outlines:
        top_elms += [gen_plate(for_left, w)]
        pcb_elms += [gen_plate(for_left, w)]
        bottom_elms += [gen_plate(for_left, w)]

    elms = [svg.G(elements=top_elms)]
    if conf.overlay:
        elms += [svg.G(elements=pcb_elms)]
        elms += [svg.G(elements=bottom_elms)]
    else:
        elms += [svg.G(elements=pcb_elms, transform=[ svg.Translate(0, 110) ])]
        elms += [svg.G(elements=bottom_elms, transform=[ svg.Translate(0, 220) ])]

    return elms

def make_keycaps(t, conf):
    kc1u = gen_grid(4, 10, 33, 20, 10, 10)     # 33 1u keycaps
    kc15u = gen_grid(1, 2, 2, 30, 75, 70)      # two 1.5u keycaps
    kc2u = gen_grid(1, 2, 2, 40, 140, 70)      # two 2u keycaps
    kcs = gen_grid(2, 21, 42, 9, 5, 85)        # 42 cylindrical stems
    kc_elms = [svg_keycap(t, 1, conf) for t in kc1u]
    kcs_elms = [svg_keycap_stem(t, conf) for t in kcs]
    elms = kc_elms + kcs_elms
    return svg.G(
        transform=t,
        elements = elms + [
            svg.G(elements = [svg_keycap(t, 1.5, conf) for t in kc15u]),
            svg.G(elements = [svg_keycap(t, 2, conf) for t in kc2u])
        ]
    )

def gen_main_layout(conf):
    w = 500
    h = 100

    elms = make_plates(True, 285, conf) + make_plates(False, 285, conf)
    style = svg.Style(
        elements = [
            "rect { fill: none; stroke: black; stroke-width: 0.05; }",
            "circle { fill: none; stroke: black; stroke-width: 0.05; }",
            "path { fill: none; stroke: black; stroke-width: 0.05; }"
        ]
    )

    if conf.separate_plate_files:
        file = open("svgoutput/top_2mm.svg", "w")
        canvas = svg.SVG(
            width=svg.Length(w, "mm"),
            height=svg.Length(h, "mm"),
            viewBox=(0,0,w,h), # This set 1 user unit equal 1mm for both x and y.
            elements=[
                style,
                elms[0],
                elms[3],
                make_stabs([svg.Translate(290, 0)], conf),
                make_plate_walls([svg.Translate(432, 0)], conf),
                make_plate_clampers([svg.Translate(290, 40)], conf)
            ],
        )
        file.write(str(canvas))

        file = open("svgoutput/pcb_1.5mm.svg", "w")
        canvas = svg.SVG(
            width=svg.Length(w, "mm"),
            height=svg.Length(h, "mm"),
            viewBox=(0,0,w,h), # This set 1 user unit equal 1mm for both x and y.
            elements=[
                style,
                elms[1],
                elms[4],
                make_keycap_jig([svg.Translate(290, 0)], conf),
                # make_stabs([svg.Translate(290, 75)], conf),
            ],
        )
        file.write(str(canvas))

        file = open("svgoutput/bottom_5mm.svg", "w")
        canvas = svg.SVG(
            width=svg.Length(w, "mm"),
            height=svg.Length(h, "mm"),
            viewBox=(0,0,w,h), # This set 1 user unit equal 1mm for both x and y.
            elements=[
                style,
                elms[2],
                elms[5],
                make_keycaps([svg.Translate(285, 0)], conf)
            ],
        )
        file.write(str(canvas))
    else:
        file = open("svgoutput/main.svg", "w")
        canvas = svg.SVG(
            width=svg.Length(w, "mm"),
            height=svg.Length(h, "mm"),
            viewBox=(0,0,w,h), # This set 1 user unit equal 1mm for both x and y.
            elements=[style] + elms,
        )
        file.write(str(canvas))

if __name__ == '__main__':
    print("Generate laser cut layout")
    conf = prodConfig
    # conf = devConfig
    # conf = modelConfig
    # In inkscape, put zoom = 165% for close to 1:1 rendering ratio
    # gen_keycap_layout(conf)
    gen_main_layout(conf)
