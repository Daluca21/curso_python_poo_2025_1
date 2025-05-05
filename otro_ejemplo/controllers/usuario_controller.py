import os
from models.usuario import Usuario
from services.json_storage import cargar_json, guardar_json
from controllers.tareas_controller import TareasController
from controllers.notas_controller import NotasController
from controllers.materias_controller import MateriasController
RUTA_ARCHIVO = os.path.join("data", "usuario.json")

class UsuarioController:
    def __init__(self):
        self.usuario = self.cargar_usuario()

    def cargar_usuario(self):
        data = cargar_json(RUTA_ARCHIVO)
        if data:
            return Usuario.from_dict(data)
        return Usuario("Usuario Ejemplo", "ejemplo@correo.com")

    def guardar_usuario(self):
        guardar_json(RUTA_ARCHIVO, self.usuario.to_dict())
    
    def get_tareas_controller(self):
        return TareasController(self.usuario)
    
    def get_notas_controller(self):
        return NotasController(self.usuario)

    def get_materias_controller(self):
        return MateriasController(self.usuario)

        

    def obtener_materias(self):
        return self.usuario.horarioDeClase

    def guardar_usuario(self):
        # Método para guardar el usuario a un archivo JSON
        pass