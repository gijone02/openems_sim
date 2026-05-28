from CSXCAD import ContinuousStructure


from CSXCAD import ContinuousStructure


def create_structure():
    CSX = ContinuousStructure()

    # Metal
    metal = CSX.AddMetal("PEC")

    # Dipole parameters (in mm because DeltaUnit = 1e-3)
    arm_length = 25      # each side
    gap = 0.5             # feed gap
    radius = 0.5         # thickness

    # Lower arm (z-direction)
    metal.AddBox(
        priority=10,
        start=[-radius, -radius, -(gap/2 + arm_length)],
        stop=[ radius,  radius, -gap/2]
    )

    # Upper arm
    metal.AddBox(
        priority=10,
        start=[-radius, -radius, gap/2],
        stop=[ radius,  radius, gap/2 + arm_length]
    )

    return CSX


def add_port(FDTD):
    gap = 1  # must match geometry

    port = FDTD.AddLumpedPort(
        1,
        50,
        [0, 0, -gap/2],
        [0, 0, gap/2],
        "z",        # z-direction
        1.0       # excitation
    )

    return port

