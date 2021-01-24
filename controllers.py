import logging
from flask import jsonify, make_response, Blueprint


flask_controllers = Blueprint('controller', __name__)


@flask_controllers.route('/api/v0/info', methods=['GET'])
def get_info():
    """
    return general information about the current application in a JSON format
    It can be used to see if the server is up
    """
    info = {
        'version': '0.0.1',
        'serviceDescription': 'code challenge backend',
        'programmingLanguage': 'Python 3.8 +',
        'servicePlatform': 'RESTful',
        'developer': 'Pezhman Kasraee',
        'email': 'me@pezhmankasraee.com'
    }
    return make_response(jsonify(info), 200)


@flask_controllers.route('/api/v0/areas', methods=['GET'])
def get_areas():
    try:
        with open('data/temp/areas.json', 'r') as file:
            json_string = file.read()
            return make_response(jsonify(eval(json_string)), 200)
    except Exception as e:
        logging.error("An exception related to area.json: {0}".format(str(e)))
        return make_response(jsonify({'error': 'API is temporarily down, please be patient'}), 500)


@flask_controllers.route('/api/v0/messages', methods=['GET'])
def get_messages():
    try:
        with open('data/temp/messages.json', 'r') as file:
            json_string = file.read()
            return make_response(jsonify(eval(json_string)), 200)
    except Exception as e:
        logging.error("An exception related to area.json: {0}".format(str(e)))
        return make_response(jsonify({'error': 'API is temporarily down, please be patient'}), 500)
