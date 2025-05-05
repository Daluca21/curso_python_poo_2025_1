import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from models.materia import Materia
from datetime import datetime

class MateriasView(tk.Toplevel):
    def __init__(self, root, materias_controller, usuario_controller):
        super().__init__(root)
        self.title("Materias")
        self.materias_controller = materias_controller
        self.usuario_controller = usuario_controller

        self.frame = ttk.Frame(self, padding=20)
        self.frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("titulo", "descripcion"), show="headings")
        self.tree.heading("titulo", text="Título")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.pack(fill="both", expand=True)

        self.refrescar_materias()

        ttk.Button(self.frame, text="Agregar Materia", command=self.agregar_materia).pack(pady=10)
        ttk.Button(self.frame, text="Editar Materia", command=self.editar_materia).pack(pady=5)
        ttk.Button(self.frame, text="Eliminar Materia", command=self.eliminar_materia).pack(pady=5)

    def refrescar_materias(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for materia in self.materias_controller.obtener_materias():
            self.tree.insert("", "end", values=(
                materia.titulo,
                materia.descripcion
            ))

    def agregar_materia(self):
        titulo = simpledialog.askstring("Título", "Ingrese el título de la materia:")
        if not titulo:
            return
        descripcion = simpledialog.askstring("Descripción", "Ingrese la descripción:")
        nueva_materia = Materia(titulo, descripcion)
        self.materias_controller.agregar_materia(nueva_materia)
        self.usuario_controller.guardar_usuario()
        self.refrescar_materias()

    def editar_materia(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleccionar Materia", "Por favor, seleccione una materia para editar.")
            return

        materia_seleccionada = self.materias_controller.obtener_materias()[self.tree.index(selected_item)]
        titulo = simpledialog.askstring("Título", "Editar título de la materia:", initialvalue=materia_seleccionada.titulo)
        if not titulo:
            return
        descripcion = simpledialog.askstring("Descripción", "Editar descripción:", initialvalue=materia_seleccionada.descripcion)

        materia_seleccionada.titulo = titulo
        materia_seleccionada.descripcion = descripcion
        self.usuario_controller.guardar_usuario()
        self.refrescar_materias()

    def eliminar_materia(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleccionar Materia", "Por favor, seleccione una materia para eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmar Eliminación", "¿Estás seguro de eliminar esta materia?")
        if confirmacion:
            materia_seleccionada = self.materias_controller.obtener_materias()[self.tree.index(selected_item)]
            self.materias_controller.eliminar_materia(materia_seleccionada)
            self.usuario_controller.guardar_usuario()
            self.refrescar_materias()
