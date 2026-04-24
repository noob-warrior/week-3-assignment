from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import sys


class SpaHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        requested = self.path.split("?", 1)[0]
        file_path = Path(self.directory, requested.lstrip("/"))

        if requested == "/" or (not file_path.exists() and "." not in Path(requested).name):
            self.path = "/index.html"

        return super().do_GET()


def main():
    port = 4173
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    directory = Path(__file__).resolve().parent
    handler = lambda *args, **kwargs: SpaHandler(*args, directory=str(directory), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", port), handler)

    print(f"Serving Interactive Book Showcase at http://127.0.0.1:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
