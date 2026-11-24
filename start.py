"""Start a private local FE Civil Prep server with its bundled PDFs.

This app binds only to the computer's loopback interface, never to the public network.
It requires only Python 3 and a modern desktop browser.
"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from functools import partial
from pathlib import Path
import os
import sys
import webbrowser

ROOT = Path(__file__).resolve().parent
EXPECTED = {"books/learnova.pdf": 809, "books/islam.pdf": 638, "books/handbook.pdf": 506}
missing = [name for name in EXPECTED if not (ROOT / name).is_file()]
if missing:
    print("Missing files from the extracted private package:")
    for name in missing:
        print(" -", name)
    print("Extract the ENTIRE ZIP before launching the site.")
    input("Press Enter to close...")
    sys.exit(1)

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        # No browsing history is stored by this local launcher.
        pass

try:
    server = ThreadingHTTPServer(("127.0.0.1", 8765), partial(Handler, directory=str(ROOT)))
except OSError as exc:
    print("Cannot start FE Civil Prep on port 8765:", exc)
    print("Close another FE Civil Prep terminal window and try again.")
    input("Press Enter to close...")
    sys.exit(1)

url = "http://127.0.0.1:8765/"
print("FE Civil Prep is running privately on this computer.")
print("Open this link in your browser:", url)
print("Your books are loaded automatically. No PDF upload is needed.")
print("Leave this window open while studying. Press Ctrl+C to stop.")
webbrowser.open(url)
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nFE Civil Prep stopped.")
finally:
    server.server_close()
