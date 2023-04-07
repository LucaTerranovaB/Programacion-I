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
    
    
    #Planificacion alumno
    #api.add_resource(resources.AlumnoResource, '/alumnos')
    
    
    
    #Cargar la APLICACION en la API  de Flask Restful (Para que la API pueda usar la applicacion)
    api.init_app(app)

    #Retornamos la app inicializada
    return app

