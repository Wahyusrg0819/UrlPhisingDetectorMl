# Test CORS configuration

$url = "https://ef8848b14210.ngrok-free.app/api/predict/"
$origin = "https://url-phising-detector-ml.vercel.app"

Write-Host "Testing CORS..." -ForegroundColor Cyan
Write-Host ""

# Test OPTIONS (preflight)
Write-Host "1. Testing OPTIONS (preflight)..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri $url -Method OPTIONS `
        -Headers @{
            "Origin" = $origin
            "Access-Control-Request-Method" = "POST"
            "Access-Control-Request-Headers" = "content-type"
        } -UseBasicParsing
    
    Write-Host "Status: $($response.StatusCode)" -ForegroundColor Green
    Write-Host "Headers:" -ForegroundColor Green
    $response.Headers.GetEnumerator() | Where-Object { $_.Key -like "*Access-Control*" } | ForEach-Object {
        Write-Host "  $($_.Key): $($_.Value)" -ForegroundColor Green
    }
} catch {
    Write-Host "ERROR: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""

# Test POST
Write-Host "2. Testing POST..." -ForegroundColor Yellow
try {
    $body = @{
        url = "https://google.com"
    } | ConvertTo-Json
    
    $response = Invoke-WebRequest -Uri $url -Method POST `
        -Headers @{
            "Origin" = $origin
            "Content-Type" = "application/json"
            "ngrok-skip-browser-warning" = "true"
        } `
        -Body $body -UseBasicParsing
    
    Write-Host "Status: $($response.StatusCode)" -ForegroundColor Green
    Write-Host "Response:" -ForegroundColor Green
    Write-Host $response.Content
} catch {
    Write-Host "ERROR: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
Write-Host "Done!" -ForegroundColor Cyan
