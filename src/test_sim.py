
import os
import sys

# ✅ FIX: explicitly add DLL directory
OPENEMS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "openEMS"))
os.add_dll_directory(OPENEMS_PATH)

import numpy as np

print("Starting OpenEMS simulation test...")

from openEMS import openEMS
from CSXCAD import ContinuousStructure


# Create simulation folder
Sim_Path = os.path.join(os.getcwd(), "sim_output")
if not os.path.exists(Sim_Path):
    os.makedirs(Sim_Path)

# Initialize solver
FDTD = openEMS()

# Set number of timesteps
FDTD.SetNumberOfTimeSteps(1000)

# Create geometry container
CSX = ContinuousStructure()
FDTD.SetCSX(CSX)

# Create mesh
mesh = CSX.GetGrid()
mesh.SetDeltaUnit(1e-3)

# Define simulation box
mesh.AddLine('x', np.linspace(-10, 10, 20))
mesh.AddLine('y', np.linspace(-10, 10, 20))
mesh.AddLine('z', np.linspace(-10, 10, 20))

# Boundary conditions
FDTD.SetBoundaryCond([3, 3, 3, 3, 3, 3])

FDTD.SetGaussExcite(2.4e9, 1e9)

print("Running simulation...")
FDTD.Run(Sim_Path)

print("✅ Simulation complete")
print(f"Results stored in: {Sim_Path}")
