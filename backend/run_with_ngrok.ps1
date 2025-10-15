# PowerShell script untuk run Django dengan Ngrok

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Django Backend with Ngrok" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if ngrok is installed
if (-not (Get-Command ngrok -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Ngrok not found!" -ForegroundColor Red
    Write-Host "Please install ngrok from: https://ngrok.com/download" -ForegroundColor Yellow
    Write-Host "Or install via Chocolatey: choco install ngrok" -ForegroundColor Yellow
    pause
    exit
}

# Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Python not found!" -ForegroundColor Red
    pause
    exit
}

Write-Host "[1/3] Starting Django server..." -ForegroundColor Green
$djangoJob = Start-Job -ScriptBlock {
    Set-Location $using:PWD
    python manage.py runserver 0.0.0.0:8000
}

Write-Host "[2/3] Waiting for Django to start..." -ForegroundColor Green
Start-Sleep -Seconds 5

Write-Host "[3/3] Starting Ngrok tunnel..." -ForegroundColor Green
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Ngrok Public URL will appear below:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop both Django and Ngrok" -ForegroundColor Yellow
Write-Host ""

# Start ngrok
try {
    ngrok http 8000
}
finally {
    # Cleanup: Stop Django server when ngrok stops
    Write-Host ""
    Write-Host "Stopping Django server..." -ForegroundColor Yellow
    Stop-Job -Job $djangoJob
    Remove-Job -Job $djangoJob
    Write-Host "Done!" -ForegroundColor Green
}
