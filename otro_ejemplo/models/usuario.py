# models/usuario.py
from datetime import datetime
from models.tarea import Tarea
from models.nota import Nota
from models.materia import Materia

class Usuario:
    def __init__(self, nombre, correo, fecha_de_creacion=None):
        self.nombre = nombre
        self.correo = correo
        self.fecha_de_creacion = fecha_de_creacion or datetime.now()
        self.tareas = []
        self.notas = []
        self.horarioDeClase = []

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "correo": self.correo,
            "fecha_de_creacion": self.fecha_de_creacion.isoformat(),
            "tareas": [t.to_dict() for t in self.tareas],
            "notas": [n.to_dict() for n in self.notas],
            "materias": [m.to_dict() for m in self.horarioDeClase]
        }

    @classmethod
    def from_dict(cls, data):
        u = cls(data["nombre"], data["correo"], datetime.fromisoformat(data["fecha_de_creacion"]))
        u.tareas = [Tarea.from_dict(t) for t in data.get("tareas", [])]
        u.notas = [Nota.from_dict(n) for n in data.get("notas", [])]
        u.horarioDeClase = [Materia.from_dict(m) for m in data.get("materias", [])]
        return u
