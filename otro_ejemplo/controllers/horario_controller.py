class HorarioController:
    def __init__(self, usuario):
        self.usuario = usuario

    def obtener_bloques(self):
        # Recoge todos los bloques de horario de las materias del usuario
        bloques = []
        for materia in self.usuario.horarioDeClase:
            bloques.extend(materia.bloquesDeHorario)
        return bloques
