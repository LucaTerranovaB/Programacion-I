from flask_restful import Resource
from flask import request

#Datos de prueba en JSON
ALUMNOS = {
    1: {'nombre':'Pepe', 'edad':'55', 'esatado':'activo', 'Planificacion':'1'},
    2: {'nombre':'Peter', 'edad':'20', 'esatado':'suspendido', 'Planificacion':'2'},
    3: {'nombre':'Ortencia', 'edad':'95', 'esatado':'activo', 'Planificacion':'3'}
}

#Defino el recurso Alumnos
class Alumno(Resource): #A la clase alumno le indico que va a ser del tipo recurso(Resource)
    #obtener recurso
    def get(self, id):
        #Verifico que exista el alumno
        if int(id) in ALUMNOS:
            #retorno animal
            return ALUMNOS[int(id)]
        #Si no existe 404
        return '', 201
    #eliminar recurso
    def delete(self, id):
        #Verifico que exista el animal
        if int(id) in ALUMNOS:
            #elimino alumno
            del ALUMNOS[int(id)]
            return '', 204
        #Si no existe 404
        return '', 404
    #Modificar el recurso alumno / aca puedo cabiar el estado de un alumno a activo 0 suspendido, luego cuando programe hago una restrigcion para quesi no esta activo no vea su planificacion
    def put(self, id):
        if int(id) in ALUMNOS:
            alumno = ALUMNOS[int(id)]
            data = request.get_json()
            alumno.update(data)
            return '', 201
        return '', 404


class Alumnos(Resource):
    #Obtenemos la coleccion de alumnos
    def get(self):
        return ALUMNOS
    
    #Agregamos un nuevo alumno
    def post(self):
        #Traemos el JSON (Body)
        alumno = request.get_json()
        #Obtenemos el ultimo ID
        id = max(ALUMNOS.keys()) + 1
        #Agregamos el nuevo alumno
        ALUMNOS[id] = alumno
        #Retornamos el nuevo alumno
        return ALUMNOS[id], 201