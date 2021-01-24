import threading
import time
import logging.config
import os
import fetch_handler
import werkzeug

from flask import Flask, jsonify
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
        try:
            fetch_handler.handle_area_data_from_traffic_service()
            fetch_handler.handle_message_data_from_traffic_service()
            time.sleep(5)
        except Exception as e:
            logging.error('Exception in thread: {0}'.format(str(e)))


def main():
    try:
        thread_fetch = threading.Thread(target=fetch_from_traffic_service)
        thread_fetch.daemon = True
        thread_fetch.start()

        server()

        thread_fetch.join()
    except KeyboardInterrupt as ki:
        try:
            os.remove('data/temp/areas.json')
            os.remove('data/temp/areas.json.txt')

            os.remove('data/temp/messages.json')
            os.remove('data/temp/messages.json.txt')

            logging.info("Server was shut down")
        except Exception as e:
            logging.error('Exception: {0}'.format(str(e)))


@app.errorhandler(werkzeug.exceptions.NotFound)
def page_not_found(e):
    return jsonify({'message': 'Page not found'}), 404


@app.errorhandler(werkzeug.exceptions.InternalServerError)
def internal_server_error(e):
    return jsonify({'message': 'internal server error'}), 500


if __name__ == '__main__':
    main()
