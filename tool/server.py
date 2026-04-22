#!/usr/bin/env python3
import http.server
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
GITHUB_RAW = "https://raw.githubusercontent.com/generative-design/Code-Package-Processing-1.5.1/master"


class GalleryHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path in ("/", ""):
            self.path = "/tool/index.html"
        if self.path == "/api/sketches":
            self.serve_sketches()
            return
        super().do_GET()

    def serve_sketches(self):
        sections = []
        for section_dir in sorted(ROOT.iterdir()):
            if not section_dir.is_dir() or not re.match(r"^\d+_", section_dir.name):
                continue

            sketches = []
            for sketch_dir in sorted(section_dir.iterdir()):
                if not sketch_dir.is_dir() or sketch_dir.name.startswith("."):
                    continue

                thumbnail = f"{GITHUB_RAW}/{section_dir.name}/{sketch_dir.name}/{sketch_dir.name}.png"

                sketches.append(
                    {
                        "name": sketch_dir.name,
                        "section": section_dir.name,
                        "thumbnail": thumbnail,
                    }
                )

            if sketches:
                sections.append({"name": section_dir.name, "sketches": sketches})

        data = json.dumps(sections).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        pass  # silence request logs


if __name__ == "__main__":
    port = 8080
    server = http.server.HTTPServer(("", port), GalleryHandler)
    print(f"\n  Generative Design Gallery")
    print(f"  → http://localhost:{port}\n")
    print(f"  Press Ctrl+C to stop\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Stopped.")
