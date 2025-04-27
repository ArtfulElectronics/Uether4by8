import svg

RJ45_WIDTH = 16
RJ45_HEIGHT = 16
RJ45_LEFT = -RJ45_WIDTH/2
RJ45_TOP = -RJ45_HEIGHT/2

def svg_hole(x, y, rad):
    return svg.Circle(
        cx=x,
        cy=y,
        r=rad
    )

def svg_rj45_pcb(t):
    RJ45_BOTTOM = RJ45_TOP + RJ45_HEIGHT
    return svg.G(
        transform=t,
        elements = [
            # The smaller holes for the metal pins on the case
            svg_hole(RJ45_LEFT+7, RJ45_TOP, 0.5),
            svg_hole(RJ45_LEFT+7, RJ45_BOTTOM, 0.5),
            # The bigger holes for the black 3mm pins
            svg_hole(RJ45_LEFT+10, RJ45_TOP+1.5, 1.5),
            svg_hole(RJ45_LEFT+10, RJ45_BOTTOM-1.5, 1.5),
            # Cut out a rectangle for the 8 main pins
            svg.Rect(
                x=RJ45_LEFT+5,
                y=RJ45_TOP+4,
                width=3,
                height=RJ45_HEIGHT-8
            )
        ]
    )

def svg_rj45_top(t):
    return svg.Rect(
        transform=t,
        x=RJ45_LEFT,
        y=RJ45_TOP,
        width=RJ45_WIDTH,
        height=RJ45_HEIGHT
    )