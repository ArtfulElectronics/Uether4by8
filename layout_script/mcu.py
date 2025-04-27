import svg

def svg_rp2040_zero_top():
    RP2040_ZERO_WIDTH = 23.50
    RP2040_ZERO_HEIGHT = 18
    return svg.Rect(
        x=0,
        y=5,
        width=RP2040_ZERO_WIDTH,
        height=RP2040_ZERO_HEIGHT
    )

NICE_NANO_WIDTH = 18.3
NICE_NANO_HEIGHT = 33.3
HOLE_RADIUS = 0.5
HOLE_PITCH = 2.54

def svg_pad_hole(x, y):
    return svg.Circle(
        cx=x,
        cy=y,
        r=HOLE_RADIUS
    )

def svg_nicenano_pcb(t):
    # The copper pad holes
    pads_holes = [
        svg_pad_hole(-7.62, -13.69 + i * HOLE_PITCH)
        for i in range(0, 12)
    ]
    pads_holes += [
        svg_pad_hole(7.62, -13.69 + i * HOLE_PITCH)
        for i in range(0, 12)
    ]
    return svg.G(
        transform=t,
        elements = pads_holes
    )

def svg_nicenano_top(t):
    # From the silkscreen
    return svg.Rect(
        transform=t,
        x=-9.15,
        y=-17.78,
        width=NICE_NANO_WIDTH,
        height=NICE_NANO_HEIGHT
    )