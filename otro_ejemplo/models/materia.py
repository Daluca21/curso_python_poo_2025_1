from models.bloque_horario import BloqueDeHorario

class Materia:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.bloquesDeHorario = []

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "bloquesDeHorario": [b.to_dict() for b in self.bloquesDeHorario]
        }

    @classmethod
    def from_dict(cls, data):
        m = cls(data["titulo"], data["descripcion"])
        m.bloquesDeHorario = [BloqueDeHorario.from_dict(b) for b in data.get("bloquesDeHorario", [])]
        return m

