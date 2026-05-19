import os

# DLL setup (keep ONLY here)
import os
OPENEMS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "openEMS"))
os.add_dll_directory(OPENEMS_PATH)

from geometry import create_structure, add_port
from simulation import setup_fdtd, setup_mesh, run_simulation


def main():
    print("Starting OpenEMS simulation")

    # Create geometry
    CSX = create_structure()

    # Setup simulation
    FDTD = setup_fdtd(CSX)

    # Add port
    port = add_port(FDTD)

    # Setup mesh
    setup_mesh(CSX)

    # Run
    sim_path = os.path.join(os.getcwd(), "sim_output")
    run_simulation(FDTD, sim_path)


if __name__ == "__main__":
    main()