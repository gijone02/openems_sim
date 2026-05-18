import sys
import os

print("Starting OpenEMS import test...")

# CHANGE THIS PATH to where you extracted OpenEMS
openems_path = r"C:\Users\\240120945\\OneDrive - GE Appliances\\Documents\\Rotation 4 - Connected Home\\OpenEMS Tool\\openEMS\\include"

sys.path.append(openems_path)

try:
    import openEMS
    import CSXCAD
    print("✅ OpenEMS import SUCCESS")
except Exception as e:
    print("❌ OpenEMS import FAILED")
    print(e)