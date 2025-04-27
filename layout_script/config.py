from dataclasses import dataclass

@dataclass
class Config:
    """
    This class provide configuration (mainly various dimensions) for the layout generation process.
    The default values are "ideal" dimensions. For example, the specified dimension for a 1u keycap is 18mm (for both width and height).
    However, when put to production (e.g. laser cutting), we need to account for the tool's tolerances (the laser beam width).
    So we render the keycap at 18.2mm instead so the beam will eat away 0.2mm and leaving us the piece at close to 18mm.
    """
    with_key_cap: bool = False
    with_plate_outlines: bool = False
    overlay: bool = False
    separate_plate_files: bool = False
    add_jig_wall: bool = False
    mounting_plate_length: float = 14
    hotswap_mounting_pin_dia: float = 5.1
    hotswap_input_pin_dia: float = 3
    keycap_u = 18 # The standard dimension of 1u for a keycap
    keycap_stem_vert_rect_width: float = 1.10
    keycap_stem_horiz_rect_width: float = 1.23
    keycap_stem_cross_length: float = 4
    keycap_stem_dia: float = 5.7

# The development config will put the components (the 3 wooden plates) on top of each other for verification.
devConfig = Config(
    with_key_cap = True,
    with_plate_outlines = True,
    overlay = True,
    add_jig_wall = True
)

modelConfig = Config(
    with_key_cap = False,
    with_plate_outlines = False,
    overlay = True,
    separate_plate_files = True
)

# The production config is to generate the final pattern for laser cutting.
prodConfig = Config(
    with_key_cap = False,
    with_plate_outlines = True,
    overlay = True,
    separate_plate_files = True,
    add_jig_wall = False,

    # Compensate for the laser's width
    #mounting_plate_length = 13.8,
    #hotswap_mounting_pin_dia = 5.1 - 0.2,
    #hotswap_input_pin_dia = 3 - 0.2,
    keycap_stem_vert_rect_width = 1.10 - 0.4,
    keycap_stem_horiz_rect_width = 1.23 - 0.4,
    keycap_stem_cross_length = 4 - 0.4,
    keycap_stem_dia = 5.7 + 0.4
)