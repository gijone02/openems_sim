from CSXCAD import ContinuousStructure


def create_structure():
    """
    Creates the CSX structure and adds geometry
    """
    CSX = ContinuousStructure()

    # --- Material definition ---
    metal = CSX.AddMetal("PEC")

    # --- Geometry ---
    
    metal.AddBox(
    priority=10,
    start=[-2, -2, 0],
    stop=[2, 2, 0.5]
    )

    return CSX


def add_port(FDTD):
    """
    Define excitation/measurement region
    """
    port = FDTD.AddLumpedPort(
    1,          # port number
    50,         # resistance
    [0, 0, 0],  # start
    [0, 0, 0.4],# stop
    'z',        # direction
    1.0         # excitation
    )

    

    return port
