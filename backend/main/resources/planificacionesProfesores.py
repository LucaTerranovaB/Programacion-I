from flask_restful import Resource
from flask import request

#Datos de prueba JSON

PLANIFICACIONES= {
    1 : { 'dni':'39999998','planificacion':'Pilates','dia':'Lunes','hora':'10:00','espacio':'1','estado':'Activo' },
    2 : { 'dni':'39523789','planificacion':'Funcional','dia':'Martes','hora':'9:00','espacio':'1','estado':'Activo' },
    3 : { 'dni':'39254110','planificacion':'Calistenia','dia':'Miercoles','hora':'11:00','espacio':'1','estado':'Activo' },
    4 : { 'dni':'39254111','planificacion':'Runnin','dia':'Lunes','hora':'10:00','espacio':'2','estado':'Activo' },
    5 : { 'dni':'39254112','planificacion':'Gimnasio','dia':'Martes','hora':'9:00','espacio':'2','estado':'Activo' },
    6 : { 'dni':'39254113','planificacion':'Pilates','dia':'Miercoles','hora':'11:00','espacio':'3','estado':'Activo' },
    7 : { 'dni':'39254254','planificacion':'Funcional','dia':'Jueves','hora':'10:00','espacio':'3','estado':'Activo' },
    8 : { 'dni':'39254915','planificacion':'Calistenia','dia':'Viernes','hora':'9:00','espacio':'4','estado':'Activo' },
    9 : { 'dni':'39254316','planificacion':'Runnin','dia':'Viernes','hora':'11:00','espacio':'1','estado':'Activo' },
    10 : {'dni':'39254127','planificacion':'Gimnasio','dia':'Sabado','hora':'10:00','espacio':'2','estado':'Activo'}
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