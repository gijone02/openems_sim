@echo off

REM Get project directory
set PROJECT_DIR=%~dp0
set OPENEMS_DIR=%PROJECT_DIR%openEMS

echo ==========================
echo Running OpenEMS Simulation
echo ==========================

echo Adding OpenEMS DLL path:
echo %OPENEMS_DIR%

REM ✅ FIX: point directly to folder containing DLLs
set PATH=%PATH%;%OPENEMS_DIR%

echo.

echo Running simulation...

python src\test_sim.py

pause