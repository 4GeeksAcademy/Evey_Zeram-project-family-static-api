"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
# Importo la estructura de datos:
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

"""
members GET - devuelve TODOS los integrantes
members POST - Crea UNO integrante
members/<int:id_member> GET - devuelve UNO integrante
members/<int:id_member> PUT - modifica UNO integrante
members/<int:id_member> DELETE - borra UNO integrante
"""

@app.route('/members', methods=['GET', 'POST'])
def handle_members():
    # this is how you can use the Family datastructure by calling its methods
    if request.method == 'GET':
        members = jackson_family.get_all_members()
        response_body = {
            "hello": "world",
            "family": members}
        return response_body, 200 #este código 200 lo ves en el objeto del response (en Postman)
    if request.method == 'POST':
        data = request.json
        response_body = {}
        print(data)
        jackson_family.add_member(data)
        members = jackson_family.get_all_members()
        response_body['message'] = 'Recibido'
        response_body['results'] = members
        return response_body, 200

@app.route('/members/<int:id_member>', methods=['GET', 'PUT', 'DELETE'])
def handle_member(id_member):
    response_body = {}
    if request.method == 'GET':
        member = jackson_family.get_member(id_member)
        if member:
            response_body['message'] = 'Encontrado'
            response_body['results'] = member
            return response_body, 200
        response_body['message'] = 'No encontrado'
        response_body['results'] = []
        return response_body, 404
    if request.method == 'DELETE':
        member = jackson_family.delete_member(id_member)
        if member: 
            response_body['message'] = 'Eliminado'
            return response_body, 200
        response_body['message'] = 'No existe el usuario'
        return response_body, 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
