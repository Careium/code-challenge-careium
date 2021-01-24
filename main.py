from flask import Flask
from controllers import flask_controllers

import logging.config


logging.config.fileConfig('resources/logging.config')
logger = logging.getLogger('simpleExample')

app = Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(flask_controllers)


def server():
    logging.info("Server starting ...")
    app.run(port=8090)


def main():
    server()


if __name__ == '__main__':
    main()
