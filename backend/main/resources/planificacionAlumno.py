from flask_restful import Resource
from flask import request


# Datos de prueba en JSON
ALUMNOS = {
    1: {'nombre': 'Pepe','Planificacion': '1', 'estado': 'activo'},
    2: {'nombre': 'Peter',  'Planificacion': '2', 'estado': 'activo'},
    3: {'nombre': 'Ortencia','Planificacion': '3', 'estado': 'activo'},
}

# Definimos el recurso Planificacion
class PlanificacionA(Resource):
    # Obtener planificaciones por alumno
    def get(self, id):
        planificacion = {}
        # Verificamos que exista el alumno
        if int(id) in ALUMNOS:
            alumno = ALUMNOS[int(id)]
            # Si el estado del alumno es 'activo', retornamos su planificación
            if alumno['estado'] == 'activo':
                planificacion_id = alumno['Planificacion']
                # Obtenemos la planificación por su ID
                planificacion = {'Planificacion': planificacion_id}
                return planificacion
            # Si el alumno no está activo, se devuelve un mensaje de error
            else:
                return {'error': 'El alumno no está activo'}, 403
        # Si no existe el alumno, se devuelve un mensaje de error
        return {'error': 'El alumno no existe'}, 404
    
    
class PlanificacionesA(Resource):
    # Obtener todas las planificaciones de los PALUMNOS
    def get(self):
        
        planificaciones = {}
        # Verificamos que exista el alumno
        for id in ALUMNOS:
            alumno = ALUMNOS[id]
            # Si el estado del alumno es 'activo', retornamos su planificación
            if alumno['estado'] == 'activo':
                planificacion_id = alumno['Planificacion']
                # Obtenemos la planificación por su ID
                planificacion = {'Planificacion': planificacion_id, 'Alumno': id, 'Nombre': alumno['nombre']}
                planificaciones[id] = planificacion
        return planificaciones

   
   