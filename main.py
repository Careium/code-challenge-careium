import threading
import time
import logging.config

from flask import Flask
from controllers import flask_controllers


logging.config.fileConfig('resources/logging.config')
logger = logging.getLogger('simpleExample')

app = Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(flask_controllers)


def server():
    logging.info("Server starting ...")
    app.run(port=8090)


def fetch_from_traffic_service():
    while True:
        time.sleep(5)


def main():
    try:
        thread_fetch = threading.Thread(target=fetch_from_traffic_service)
        thread_fetch.daemon = True
        thread_fetch.start()

        server()

        thread_fetch.join()
    except KeyboardInterrupt as ki:
        logging.info("Server was shut down")


if __name__ == '__main__':
    main()
