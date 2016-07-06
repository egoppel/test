from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, This is my python app deployed with shipped.io"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
