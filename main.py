from flask import Flask, jsonify, make_response, request

import shoppingService

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return jsonify(
        app="Feirinha API"
    )

@app.route('/api/v1/feiras', methods=["GET"])
def getShoppings():
    return make_response(jsonify(shoppingService.listAllShoppings()), 200)

@app.route('/api/v1/feiras/cadastro', methods=["POST"])
def createShopping():
    request_data = request.get_json()

    response = shoppingService.createNewShopping(request_data)

    return make_response({"description": response['message']}, response['code'])


if __name__ == '__main__':
    app.Debug = True
    app.run(host = '0.0.0.0', port = 5000)
