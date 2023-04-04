from flask_restful import Resource
from flask import request

#Datos de prueba JSON

ANIMALES = {
    1: { 'nombre':'boby','raza':'pastor aleman'},
    2: { 'nombre':'luna','raza':'caniche'}    
}

#Defino el recurso Animal

class Animal(Resource):
    def get(self, id):
        
        if int(id) in ANIMALES:
            return ANIMALES[int(id)]
        
        return {'error': 'Animal no encontrado'}, 404
    
    def delete(self, id):
        if int(id) in ANIMALES:
            del ANIMALES[int(id)]
            return '', 204
        
        return {'error': 'Animal no encontrado'}, 404
    
    def put(self, id):
        
        if int(id) in ANIMALES:
            animal = ANIMALES[int(id)]
            data = request.get_json()
            animal.update(data)
            return '', 201
        
        return {'error': 'Animal no encontrado'}, 404
    
    
class Animales(Resource):
    def get(self):
        return ANIMALES
    
    def post(self):
        animal = request.get_json()
        id = int(max(ANIMALES.keys())) + 1
        ANIMALES[id] = animal
        return ANIMALES[id], 201