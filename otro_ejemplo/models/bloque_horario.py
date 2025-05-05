from datetime import time

class BloqueDeHorario:
    def __init__(self, hora_inicio, hora_fin, dia_semana):
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.dia_semana = dia_semana

    def to_dict(self):
        return {
            "hora_inicio": self.hora_inicio.strftime("%H:%M"),
            "hora_fin": self.hora_fin.strftime("%H:%M"),
            "dia_semana": self.dia_semana
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            time.fromisoformat(data["hora_inicio"]),
            time.fromisoformat(data["hora_fin"]),
            data["dia_semana"]
        )
