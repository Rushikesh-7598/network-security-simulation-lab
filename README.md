# Network Security Simulation Lab — One-Click Edition

A small, dependency-free local web app that demonstrates network security concepts through **simulation**:
- VLAN segmentation and subnet mapping
- Least-privilege ACL decisions
- Firewall policy checks
- Example TCP/IP traffic inspection
- Simulated IDS alerts
- Automated test results and downloadable report

## Quick start (Windows)
1. Extract this ZIP to a folder.
2. Install Python 3.10+ from https://www.python.org/downloads/ if it is not already installed. During setup, select **Add Python to PATH**.
3. Double-click `RUN_WINDOWS.bat`.
4. Your browser should open the lab dashboard. If it does not, open http://127.0.0.1:8765 manually.
5. Click **Run all tests**. Use **Download report** to save a JSON report.

## Quick start (macOS / Linux)
1. Install Python 3.10+.
2. Extract the ZIP.
3. Open a terminal in the extracted folder and run:
   `bash RUN_MAC_LINUX.sh`
4. Open http://127.0.0.1:8765 if your browser does not open automatically.

## Stop the app
Close the terminal window running the server, or press Ctrl+C in the terminal.

## Important distinction
This is a **working educational simulator**, not a live network emulator. It simulates policy decisions in the browser; it does not configure a physical switch/router, create actual VLANs, block real traffic, or run real IDS/IPS inspection. Cisco and Suricata example files are included as reference artifacts and must be deployed/tested separately in a suitable lab. Do not claim real device configuration or real packet capture based only on the simulator.

## Folder structure
- `RUN_WINDOWS.bat` — double-click launcher for Windows
- `RUN_MAC_LINUX.sh` — launcher for macOS/Linux
- `app/server.py` — local Python HTTP server, standard library only
- `app/index.html` — interactive simulator
- `configs/cisco/` — example IOS-style reference configs
- `configs/suricata/` — sample alert rules for controlled lab traffic
- `docs/TESTING_GUIDE.md` — test walkthrough and limitations
- `reports/` — location to save downloaded reports

## Troubleshooting
- **Python not found:** install Python 3.10+ and enable PATH, then retry.
- **Port 8765 busy:** close another local app using that port, or change `PORT` in the launcher/server command.
- **Browser didn't open:** manually visit `http://127.0.0.1:8765`.
- **Security software warning:** the server binds only to `127.0.0.1` (your own computer), not the local network.
