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


import numpy as np

def setup_mesh(CSX):

    mesh = CSX.GetGrid()
    mesh.SetDeltaUnit(1e-3)

    # High resolution around dipole
    mesh.AddLine('z', np.concatenate([
        np.linspace(-100, -5, 381),
        np.linspace(-5, 5, 81),      # dense region at feed
        np.linspace(5, 100, 381)
    ]))

    # Symmetric grid
    mesh.AddLine('x', np.linspace(-20, 20, 121))
    mesh.AddLine('y', np.linspace(-20, 20, 121))

    return


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
