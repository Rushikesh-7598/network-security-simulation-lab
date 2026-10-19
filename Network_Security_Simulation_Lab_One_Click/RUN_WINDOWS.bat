@echo off
setlocal
cd /d "%~dp0"
echo Starting Network Security Simulation Lab...
where py >nul 2>nul
if %errorlevel%==0 (
  start "" http://127.0.0.1:8765
  py -3 app\server.py
) else (
  where python >nul 2>nul
  if %errorlevel%==0 (
    start "" http://127.0.0.1:8765
    python app\server.py
  ) else (
    echo Python 3 was not found. Install Python 3.10+ from https://www.python.org/downloads/
    echo Then run this file again.
    pause
  )
)
endlocal
