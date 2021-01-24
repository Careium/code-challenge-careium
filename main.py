from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


def server():
    app.run(port=8090)


def main():
    server()


if __name__ == '__main__':
    main()
