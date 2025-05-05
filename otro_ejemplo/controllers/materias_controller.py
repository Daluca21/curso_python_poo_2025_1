class MateriasController:
    def __init__(self, usuario):
        self.usuario = usuario

    def obtener_materias(self):
        return self.usuario.horarioDeClase

    def agregar_materia(self, materia):
        self.usuario.horarioDeClase.append(materia)

    def eliminar_materia(self, materia):
        self.usuario.horarioDeClase.remove(materia)
