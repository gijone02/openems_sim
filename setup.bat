@echo off

echo Installing Python dependencies...

python -m pip install --upgrade pip
python -m pip install numpy matplotlib

echo Installing OpenEMS packages...

python -m pip install openEMS\python\csxcad-0.6.3-cp314-cp314-win_amd64.whl
python -m pip install openEMS\python\openems-0.0.36-cp314-cp314-win_amd64.whl

echo.
echo ✅ Setup complete!
pause