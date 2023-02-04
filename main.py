from config import config
from server.server import app

if __name__ == "__main__":
    app.run(host=config.host, port=config.port, threaded=True, debug=True)
