# models/tarea.py
from datetime import datetime

class Tarea:
    def __init__(self, titulo, descripcion, fecha_de_vencimiento, color_hexa, prioridad, materia=None, fecha_de_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_de_creacion = fecha_de_creacion or datetime.now()
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.color_hexa = color_hexa
        self.prioridad = prioridad
        self.materia = materia  # Referencia por nombre

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "fecha_de_creacion": self.fecha_de_creacion.isoformat(),
            "fecha_de_vencimiento": self.fecha_de_vencimiento.isoformat(),
            "color_hexa": self.color_hexa,
            "prioridad": self.prioridad,
            "materia": self.materia
        }

    def esVencida(self):
        return datetime.today() > self.fecha_de_vencimiento

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["titulo"],
            data["descripcion"],
            datetime.fromisoformat(data["fecha_de_vencimiento"]),
            data["color_hexa"],
            data["prioridad"],
            data.get("materia"),
            datetime.fromisoformat(data["fecha_de_creacion"])
        )
