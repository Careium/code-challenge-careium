from flask import Flask
import logging.config


logging.config.fileConfig('resources/logging.config')
logger = logging.getLogger('simpleExample')


app = Flask(__name__)
app.config["DEBUG"] = True


def server():
    logging.info("Server starting ...")
    app.run(port=8090)


def main():
    server()


if __name__ == '__main__':
    main()
