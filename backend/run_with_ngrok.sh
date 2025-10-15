#!/bin/bash

echo "========================================"
echo "Starting Django Backend with Ngrok"
echo "========================================"
echo ""

echo "[1/3] Starting Django server..."
python manage.py runserver 0.0.0.0:8000 &
DJANGO_PID=$!

echo "[2/3] Waiting for Django to start..."
sleep 5

echo "[3/3] Starting Ngrok tunnel..."
echo ""
echo "========================================"
echo "Ngrok will show your public URL below:"
echo "========================================"
echo ""

ngrok http 8000

# Cleanup on exit
kill $DJANGO_PID
