import svg

from keyswitch import *
from keycap import *

def make_keycap_jig(t, conf):
    # Make a small grid
    num_rows = 2
    num_cols = 4
    thickness = 1.5
    keycap_length = 18
    spacing = keycap_length + thickness
    plate_width = num_cols * keycap_length + thickness * (num_cols + 1)
    plate_height = num_rows * keycap_length + thickness * (num_rows + 1)
    base_to_stem_height = 11.75 - 5.65 + (5.85 - 3.35)

    # The rectangular plate containing the hotswaps
    kc = gen_grid(num_rows, num_cols, num_rows * num_cols, spacing, thickness + keycap_length / 2, thickness + keycap_length / 2)
    elms = [svg_switch_hotswap(t, conf) for t in kc]
    elms += [
        svg.Rect(
            x=0,
            y=0,
            width=plate_width,
            height=plate_height
        )
    ]

    if conf.add_jig_wall:
        elms += [
            svg.Rect(
                x=i * spacing,
                y=0,
                width=1.5,
                height=plate_height
            )
            for i in range(0, num_cols + 1)
        ]
        elms += [
            svg.Rect(
                x=0,
                y=i*spacing,
                width=plate_width,
                height=1.5
            )
            for i in range(0, num_rows + 1)
        ]

    # The row walls
    elms += [
        svg.Rect(
            x=plate_width + 2,
            y=i*(base_to_stem_height + 9),
            width=plate_width,
            height=base_to_stem_height + 7 # 7mm for the keycap to slide between the walls
        )
        for i in range(0, num_rows + 1)
    ]

    # The column walls
    elms += [
        svg.Rect(
            x=i * spacing,
            y=53,
            width=base_to_stem_height + 4, # extra 4mm to fit the keycap right in the middle
            height=keycap_length
        )
        for i in range(0, num_rows * (num_cols + 1))
    ]

    return svg.G(
        transform=t,
        elements = elms
    )