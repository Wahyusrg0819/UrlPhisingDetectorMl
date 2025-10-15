@echo off
echo ========================================
echo Starting Django Backend with Ngrok
echo ========================================
echo.

echo [1/3] Starting Django server...
start "Django Server" cmd /k "python manage.py runserver 0.0.0.0:8000"

echo [2/3] Waiting for Django to start...
timeout /t 5 /nobreak > nul

echo [3/3] Starting Ngrok tunnel...
echo.
echo ========================================
echo Ngrok will show your public URL below:
echo ========================================
echo.

ngrok http 8000

pause
