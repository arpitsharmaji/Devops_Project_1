from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
    return "I am Arpit from Saharanpur"

@app.route("/phone")
def lwphone():
    return "9084511318"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

