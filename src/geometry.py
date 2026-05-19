from CSXCAD import ContinuousStructure


def create_structure():
    """
    Creates the CSX structure and adds geometry
    """
    CSX = ContinuousStructure()

    # Add PEC metal
    metal = CSX.AddMetal("PEC")

    CSX.AddBox(
        metal,
        priority=10,
        start=[-2, -2, 0],
        stop=[2, 2, 0.5]
    )

    return CSX


def add_port(FDTD):
    """
    Adds a lumped port to the simulation
    """
    port = FDTD.AddLumpedPort(
        port_nr=1,
        R=50,
        start=[0, 0, 0],
        stop=[0, 0, 0.5],
        direction='z'
    )
    return port
