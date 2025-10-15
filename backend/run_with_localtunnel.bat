@echo off
echo ========================================
echo Starting Django Backend with LocalTunnel
echo ========================================
echo.

echo [1/3] Checking LocalTunnel installation...
where lt >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: LocalTunnel not found!
    echo.
    echo Installing LocalTunnel...
    npm install -g localtunnel
    echo.
)

echo [2/3] Starting Django server...
start "Django Server" cmd /k "python manage.py runserver 0.0.0.0:8000"

echo [3/3] Waiting for Django to start...
timeout /t 5 /nobreak > nul

echo.
echo ========================================
echo LocalTunnel Public URL:
echo ========================================
echo.
echo Copy the URL below and update in:
echo   frontend/.env.local
echo   NEXT_PUBLIC_API_URL=YOUR_URL_HERE
echo.
echo ========================================
echo.

lt --port 8000

pause
