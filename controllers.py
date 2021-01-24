from flask import Flask, jsonify, make_response, abort, Blueprint


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
