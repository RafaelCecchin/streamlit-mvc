import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from routes import web_routes

if __name__ == "__main__":
    web_routes()
