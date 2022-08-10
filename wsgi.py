from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hi Karthikeyan VG !!!"

@application.route("/hi")
def hello():
    return "Hello Karthikeyan VG !!!"


if __name__ == "__main__":
    application.run()
