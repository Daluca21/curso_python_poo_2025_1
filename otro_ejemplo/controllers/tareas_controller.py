class TareasController:
    def __init__(self, usuario):
        self.usuario = usuario

    def obtener_tareas(self):
        return self.usuario.tareas

    def agregar_tarea(self, tarea):
        self.usuario.tareas.append(tarea)

    def eliminar_tarea(self, tarea):
        self.usuario.tareas.remove(tarea)
