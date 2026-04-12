#!/bin/bash
cd "$(dirname "$0")"
echo "Starting Multi-AI Tool server..."
echo "Keep this window open while using the tool. Close it when done."
python3 server.py &
sleep 1.5
open "http://localhost:8731/multi-ai.html"
wait
