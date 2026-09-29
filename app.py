from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "Hello! Welcome to AWS Elastic Beanstalk."

@application.route("/about")
def about():
    return "This application is deployed on AWS."

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)