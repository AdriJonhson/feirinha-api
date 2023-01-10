from flask import jsonify

from deta import Deta

import os

deta = Deta(os.environ.get('DETA_PROJECT_KEY'))

def listAllShoppings():
    shoppings = deta.Base("shoppings")

    shoppings = shoppings.fetch({})

    return shoppings.items

def createNewShopping(request):
    shoppings = deta.Base("shoppings")

    key = "{}_{}_key".format(request['year'], request['month'])

    verifyIfExists = shoppings.fetch({"key": key}).count > 0

    if(verifyIfExists):
        return {
            "message": "Feira já cadastrada",
            "code": 422
        }

    data = {
        'key': key,
        'month': request['month'],
        'year': request['year'],
        'total': request['total'],
        'date_of_purchase': request['date'],
        'status': 'PENDING'
    }

    shoppings.insert(data)

    return {
        "message": "Feira criada com sucesso",
        "code": 201
    }
