import svg

def svg_switch_mounting_plate(t, conf):
    return svg.Rect(
        x=-conf.mounting_plate_length/2,
        y=-conf.mounting_plate_length/2,
        transform=t,
        width=conf.mounting_plate_length,
        height=conf.mounting_plate_length
    )

def svg_switch_hotswap(t, conf):
    return svg.G(
        transform=t,
        elements = [
            svg.Circle(
                cx=0,
                cy=0,
                r=conf.hotswap_mounting_pin_dia/2
            ),
            svg.Circle(
                cx=-4.4,
                cy=+4.7,
                r=conf.hotswap_input_pin_dia/2
            ),
            svg.Circle(
                cx=+2.6,
                cy=+5.75,
                r=conf.hotswap_input_pin_dia/2
            ),
        ]
    )