from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

FREIGHTS = {
    '1': {'state': 'PR', 'price': 15.00, 'city': 'test'},
    '2': {'state': 'SP', 'price': 15.00, 'city': 'test2'},
    '3': {'state': 'RS', 'price': 15.00, 'city': 'test3'}
}


class Freights(Resource):
    # Here list all items registered
    def get (self):
        return FREIGHTS

    # Here u can add another item
    def post (self):
        parser.add_argument('cep')
        parser.add_argument('price')
        args = parser.parse_args()

        via_cep = consult_via_cep(args['cep'])  # call the function to consult viaCep.api

        # add new index
        freight_id = int(max(FREIGHTS.keys())) + 1
        freight_id = '%i' % freight_id

        # append on dict
        FREIGHTS[freight_id] = {
            "state": via_cep['uf'],
            "price": args['price'],
            "city": via_cep['localidade']
        }
        return FREIGHTS[freight_id], 201  # return id of item with status code 201(work successful)


# add new route
api.add_resource(Freights, '/freights/')


class Freight(Resource):
    # Consult a specific item
    def get (self, freight_id):
        if freight_id not in FREIGHTS:
            return "Not found", 404
        else:
            return FREIGHTS[freight_id]

    # edit a specific item
    def put (self, freight_id):
        parser.add_argument('price')
        args = parser.parse_args()
        if freight_id not in FREIGHTS:
            return "Record not found", 404
        else:
            freight = FREIGHTS[freight_id]
            freight['price'] = args['price'] if args['price'] is not None else freight['price']
            return freight
    # delete a specific
    def delete (self, freight_id):
        if freight_id not in FREIGHTS:
            return "Not found", 404
        else:
            del FREIGHTS[freight_id]
            return 'Item deleted!', 204


# add new route
api.add_resource(Freight, '/freights/<freight_id>')


# function to consult viaCep Api
def consult_via_cep (args):
    response = requests.get(f'https://viacep.com.br/ws/{args}/json/')
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)