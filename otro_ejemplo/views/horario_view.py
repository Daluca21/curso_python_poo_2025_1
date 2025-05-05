import tkinter as tk
from tkinter import ttk
from models.bloque_horario import BloqueDeHorario
from models.materia import Materia
from datetime import datetime

class HorarioView(tk.Toplevel):
    def __init__(self, root, usuario_controller):
        super().__init__(root)
        self.title("Horario de Clases")
        self.usuario_controller = usuario_controller
        self.frame = ttk.Frame(self, padding=20)
        self.frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("materia", "dia", "hora_inicio", "hora_fin"), show="headings")
        self.tree.heading("materia", text="Materia")
        self.tree.heading("dia", text="Día")
        self.tree.heading("hora_inicio", text="Hora de Inicio")
        self.tree.heading("hora_fin", text="Hora de Fin")
        self.tree.pack(fill="both", expand=True)

        self.refrescar_horario()

    def refrescar_horario(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for materia in self.usuario_controller.obtener_materias():
            for bloque in materia.bloquesDeHorario:
                self.tree.insert("", "end", values=(
                    materia.titulo,
                    bloque.dia_semana,
                    bloque.hora_inicio.strftime("%H:%M"),
                    bloque.hora_fin.strftime("%H:%M")
                ))
