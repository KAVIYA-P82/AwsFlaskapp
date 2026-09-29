from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Welcome to Google Cloud Run."

@app.route("/about")
def about():
    return "This application is deployed on Google Cloud Run."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
