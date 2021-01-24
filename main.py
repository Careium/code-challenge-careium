import threading
import time
import logging.config
import requests
import json
import os

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
        try:
            areas_json_object = fetch_area_data()
            save_area_data_in_temp_files(areas_json_object)
        except Exception as e:
            logging.error('Exception in thread: {0}'.format(str(e)))


def fetch_area_data():
    try:
        response_area = requests.get('http://api.sr.se/api/v2/traffic/areas?format=json&indent=true')
        response_area_json = response_area.json()
        areas = response_area_json["areas"]
        areas_json_object = {'areas': areas}
        return areas_json_object
    except Exception as e:
        logging.error('Exception in thread: {0}'.format(str(e)))


def save_area_data_in_temp_files(areas_json_object):
    try:
        with open('data/temp/areas.json', 'w') as file:
            file.write(str(areas_json_object))
        with open('data/temp/areas.json.txt', 'w') as file:
            area_json_string = json.dumps(areas_json_object, indent=2)
            file.write(area_json_string)

        logging.info('All AREAs are fetched and saved successfully')
    except IOError as ioe:
        logging.error('IOException in thread: {0}'.format(str(ioe)))
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
            logging.info("Server was shut down")
        except Exception as e:
            logging.error('Exception writing areas.json.txt. {0}'.format(str(e)))


if __name__ == '__main__':
    main()
