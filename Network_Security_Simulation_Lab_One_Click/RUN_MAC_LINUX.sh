#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
echo "Starting Network Security Simulation Lab..."
if command -v python3 >/dev/null 2>&1; then
  (sleep 1; python3 -c "import webbrowser; webbrowser.open('http://127.0.0.1:8765')" >/dev/null 2>&1 || true) &
  python3 app/server.py
else
  echo "Python 3 was not found. Install Python 3.10+ and retry."
  exit 1
fi
