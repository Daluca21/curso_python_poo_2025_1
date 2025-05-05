class NotasController:
    def __init__(self, usuario):
        self.usuario = usuario

    def obtener_notas(self):
        return self.usuario.notas

    def agregar_nota(self, nota):
        self.usuario.notas.append(nota)

    def eliminar_nota(self, nota):
        self.usuario.notas.remove(nota)
