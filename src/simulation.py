import numpy as np
import os
from openEMS import openEMS


def setup_fdtd(CSX):
    """
    Initializes and configures the FDTD solver
    """
    FDTD = openEMS()

    # Link structure
    FDTD.SetCSX(CSX)

    # Simulation settings
    FDTD.SetNumberOfTimeSteps(1e5)
    FDTD.SetBoundaryCond([3, 3, 3, 3, 3, 3])
    FDTD.SetGaussExcite(2.4e9, 1e9)

    return FDTD


def setup_mesh(CSX):
    """
    Defines the simulation grid
    """
    mesh = CSX.GetGrid()
    mesh.SetDeltaUnit(1e-3)

    mesh.AddLine('x', np.linspace(-10, 10, 51))
    mesh.AddLine('y', np.linspace(-10, 10, 51))
    mesh.AddLine('z', np.linspace(-10, 10, 51))


def run_simulation(FDTD, sim_path):
    """
    Runs the simulation
    """
    if not os.path.exists(sim_path):
        os.makedirs(sim_path)

    print("Running simulation...")
    FDTD.Run(sim_path)

    print("Simulation complete")
    print(f"Results stored in: {sim_path}")
