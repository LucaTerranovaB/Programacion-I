import os
from flask import Flask
from dotenv import load_dotenv


#Agregamos la clase API
from flask_restful import Api

#Importo directorio de recursos
import main.resources as resources

#Inicio Restful API
api = Api()

#Metodo que inicializara la app y sus modulos
def create_app():

    #Iniciamos Flask
    app = Flask(__name__)

    #Cargamos variables de entorno
    load_dotenv()

    #Cargar a la API el Recurso PROFESORES y especificamos la ruta
    api.add_resource(resources.ProfesorResource, '/profesor/<id>')
    
    #Cargar a la API el Recurso Profesor Y especificamos la ruta
    api.add_resource(resources.ProfesoresResource, '/profesores')
    
    #Cargar a la API el Recurso Planificacion Y especificamos la ruta
    api.add_resource(resources.PlanificacionResource, '/planificacion/<id>')
    
    #Cargar a la API el Recurso Planificaciones Y especificamos la ruta
    api.add_resource(resources.PlanificacionesResource, '/planificaciones')
    
    #Cargar a la API el Recurso Alumno Y especificamos la ruta
    api.add_resource(resources.AlumnoResource, '/alumno/<id>')
    
    #Cargar a la API el Recurso Alumnos Y especificamos la ruta
    api.add_resource(resources.AlumnosResource, '/alumnos')
    
    #Cargar a la API el Recurso PlanificacionA Y especificamos la ruta
    api.add_resource(resources.PlanificacionAResource, '/planificacionA/<id>')
    
    #Cargar a la API el Recurso PlanificacionesA Y especificamos la ruta
    api.add_resource(resources.PlanificacionesAResource, '/planificacionesA')
    
  
    
    #Cargar la APLICACION en la API  de Flask Restful (Para que la API pueda usar la applicacion)
    api.init_app(app)

    #Retornamos la app inicializada
    return app

