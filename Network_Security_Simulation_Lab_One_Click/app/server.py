from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
import threading
import webbrowser

ROOT = Path(__file__).resolve().parent
PORT = int(os.environ.get("PORT", "8765"))

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt, *args):
        print("[lab-server] " + fmt % args)

def main():
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://127.0.0.1:{PORT}/index.html"
    print("=" * 62)
    print(" Network Security Simulation Lab is running")
    print(f" Open: {url}")
    print(" Bound to 127.0.0.1 only. Press Ctrl+C to stop.")
    print("=" * 62)
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\\nStopping lab server...")
    finally:
        server.server_close()

if __name__ == "__main__":
    main()
