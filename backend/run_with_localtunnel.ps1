# PowerShell script untuk run Django dengan LocalTunnel

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Django Backend with LocalTunnel" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if localtunnel is installed
if (-not (Get-Command lt -ErrorAction SilentlyContinue)) {
    Write-Host "LocalTunnel not found. Installing..." -ForegroundColor Yellow
    npm install -g localtunnel
    Write-Host ""
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

Write-Host "[3/3] Starting LocalTunnel..." -ForegroundColor Green
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "LocalTunnel Public URL:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Copy the URL and update in:" -ForegroundColor Yellow
Write-Host "  frontend/.env.local" -ForegroundColor Yellow
Write-Host "  NEXT_PUBLIC_API_URL=YOUR_URL_HERE" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop" -ForegroundColor Yellow
Write-Host ""

# Start localtunnel
try {
    lt --port 8000
}
finally {
    Write-Host ""
    Write-Host "Stopping Django server..." -ForegroundColor Yellow
    Stop-Job -Job $djangoJob
    Remove-Job -Job $djangoJob
    Write-Host "Done!" -ForegroundColor Green
}
