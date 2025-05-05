from datetime import datetime

class Nota:
    def __init__(self, titulo, descripcion, fecha_de_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_de_creacion = fecha_de_creacion or datetime.now()

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "fecha_de_creacion": self.fecha_de_creacion.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["titulo"],
            data["descripcion"],
            datetime.fromisoformat(data["fecha_de_creacion"])
        )

