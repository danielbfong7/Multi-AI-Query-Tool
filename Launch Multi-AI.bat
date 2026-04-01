@echo off
cd /d "%~dp0"
start "Multi-AI Server" /min python server.py
timeout /t 1 /nobreak >nul
start "" "http://localhost:8731/multi-ai.html"
