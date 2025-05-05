import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from models.nota import Nota
from datetime import datetime

class NotasView(tk.Toplevel):
    def __init__(self, root, notas_controller, usuario_controller):
        super().__init__(root)
        self.title("Notas")
        self.notas_controller = notas_controller
        self.usuario_controller = usuario_controller

        self.frame = ttk.Frame(self, padding=20)
        self.frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("titulo", "fecha"), show="headings")
        self.tree.heading("titulo", text="Título")
        self.tree.heading("fecha", text="Creación")
        self.tree.pack(fill="both", expand=True)

        self.refrescar_notas()

        ttk.Button(self.frame, text="Agregar Nota", command=self.agregar_nota).pack(pady=10)
        ttk.Button(self.frame, text="Editar Nota", command=self.editar_nota).pack(pady=5)
        ttk.Button(self.frame, text="Eliminar Nota", command=self.eliminar_nota).pack(pady=5)

    def refrescar_notas(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for nota in self.notas_controller.obtener_notas():
            self.tree.insert("", "end", values=(
                nota.titulo,
                nota.fecha_de_creacion.strftime("%Y-%m-%d")
            ))

    def agregar_nota(self):
        titulo = simpledialog.askstring("Título", "Ingrese el título de la nota:")
        if not titulo:
            return
        descripcion = simpledialog.askstring("Descripción", "Ingrese la descripción:")
        nueva_nota = Nota(titulo, descripcion, datetime.now())
        self.notas_controller.agregar_nota(nueva_nota)
        self.usuario_controller.guardar_usuario()
        self.refrescar_notas()

    def editar_nota(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleccionar Nota", "Por favor, seleccione una nota para editar.")
            return

        nota_seleccionada = self.notas_controller.obtener_notas()[self.tree.index(selected_item)]
        titulo = simpledialog.askstring("Título", "Editar título de la nota:", initialvalue=nota_seleccionada.titulo)
        if not titulo:
            return
        descripcion = simpledialog.askstring("Descripción", "Editar descripción:", initialvalue=nota_seleccionada.descripcion)

        nota_seleccionada.titulo = titulo
        nota_seleccionada.descripcion = descripcion
        self.usuario_controller.guardar_usuario()
        self.refrescar_notas()

    def eliminar_nota(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleccionar Nota", "Por favor, seleccione una nota para eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmar Eliminación", "¿Estás seguro de eliminar esta nota?")
        if confirmacion:
            nota_seleccionada = self.notas_controller.obtener_notas()[self.tree.index(selected_item)]
            self.notas_controller.eliminar_nota(nota_seleccionada)
            self.usuario_controller.guardar_usuario()
            self.refrescar_notas()
