from flask_restful import Resource
from flask import request

#Datos de prueba JSON

PLANIFICACIONES= {

}
#Definos el recurso 

# Definimos la clase Profesor y le indicamos que va a ser de tipo Resource
class Planificacion(Resource):
    
    #Obtenemos el Recurso
    def get(self, id):
        
        #Verificacion que existe el Profesor
        if int(id) in PLANIFICACIONES:
            
            
            #Retornamos el Profesor
            return PLANIFICACIONES[int(id)]

        #Retornamos un mensaje de exito
        return '', 201
        
        
    
    #Eliminamos el Recurso
    def delete(self, id):
        
        #Verificacion que existe el Profesor
        if int(id) in PLANIFICACIONES:
            
            #Elimino el Profesor
            del PLANIFICACIONES[int(id)]
            
            #Retornamos un mensaje de exito
            return '', 204
        
        #Si no existe el Profesor retornamos un error 404
        return {'error': 'Profesor no encontrado'}, 404
    
    #Modificamos el Recurso PROFESOR
    def put(self, id):
        
         
        if int(id) in PLANIFICACIONES:
            
            #Guardamos el Profesor
            planificacion = PLANIFICACIONES[int(id)]
            #Traemos el JSON (Body)
            data = request.get_json()
            #Lo reemplazamos
            planificacion.update(data)
            
            #retornamos mensaje de exito
            return '', 201
        
        #Si no existe el Profesor retornamos un error 404
        return {'error': 'Profesor no encontrado'}, 404
    

#Coleccion de RECURSO PROFESORES    
class Planificaciones(Resource):
    
    #Obtenemos la coleccion de PROFESORES
    def get(self):
        return PLANIFICACIONES
    
    #Insertamos un nuevo Profesor
    def post(self):
        planificacion = request.get_json()
        id = int(max(PLANIFICACIONES.keys())) + 1
        PLANIFICACIONES[id] = planificacion
        return PLANIFICACIONES[id], 201