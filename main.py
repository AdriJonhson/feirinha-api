from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return jsonify(
        app="Feirinha API"
    )


@app.route('/api/v1/feiras', methods=["GET"])
def getShoppings():
    return jsonify(
        app="Feirinha API"
    )


if __name__ == '__main__':
    app.Debug = True
    app.run(host = '0.0.0.0', port = 5000)
