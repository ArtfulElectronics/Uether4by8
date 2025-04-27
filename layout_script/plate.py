import svg

def gen_plate(for_left=True, w=300):
    plate_width = 140
    plate_height = 96
    margin = 3
    screw_holes = [
        svg.Circle(
            cx=35*i if for_left else w-35*i,
            cy=margin,
            r=0.6
        )
        for i in range(1, 4)
    ]
    screw_holes += [
        svg.Circle(
            cx=35*i if for_left else w-35*i,
            cy=plate_height - margin,
            r=0.6
        )
        for i in range(1, 4)
    ]
    screw_holes += [
        svg.Circle(
            cx=margin if for_left else w-margin,
            cy=i*32,
            r=0.6
        )
        for i in range(1, 3)
    ]
    screw_holes += [
        svg.Circle(
            cx=plate_width-margin if for_left else w - (plate_width-margin),
            cy=i*32,
            r=0.6
        )
        for i in range(1, 3)
    ]
    if for_left:
        return svg.G(
            elements = screw_holes + [
                svg.Rect(
                    x=0,
                    y=0,
                    width=plate_width,
                    height=plate_height
                )
            ]
        )
    else:
        return svg.G(
            elements = screw_holes + [
                svg.Rect(
                    x=w-plate_width,
                    y=0,
                    width=plate_width,
                    height=plate_height
                )
            ]
        )