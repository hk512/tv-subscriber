import logging
import sys

from config import config
from server.server import app

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='[%(levelname)s][%(asctime)s] %(message)s')
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    app.run(host=config.host, port=config.port, threaded=True, debug=True)
