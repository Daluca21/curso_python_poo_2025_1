class Usuario:
    def __init__(self, nombre, tareas = []):
        self.nombre = nombre
        self.tareas = tareas

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

    def eliminarTarea(self, tarea):
        for t in self.tareas:
            if(t == tarea):
                self.tareas.remove(t)
                break