import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import simpledialog, messagebox
from models.tarea import Tarea

class TareasView(tk.Toplevel):
    def __init__(self, root, tareas_controller, usuario_controller):
        super().__init__(root)
        self.title("Tareas")
        self.tareas_controller = tareas_controller
        self.usuario_controller = usuario_controller

        self.frame = ttk.Frame(self, padding=20)
        self.frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("titulo", "vencimiento", "prioridad"), show="headings")
        self.tree.heading("titulo", text="Título")
        self.tree.heading("vencimiento", text="Vence")
        self.tree.heading("prioridad", text="Prioridad")
        self.tree.pack(fill="both", expand=True)

        self.refrescar_tareas()

        ttk.Button(self.frame, text="Agregar Tarea", command=self.agregar_tarea).pack(pady=10)
        ttk.Button(self.frame, text="Editar Tarea", command=self.editar_tarea).pack(pady=5)
        ttk.Button(self.frame, text="Eliminar Tarea", command=self.eliminar_tarea).pack(pady=5)

    def refrescar_tareas(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for tarea in self.tareas_controller.obtener_tareas():
            self.tree.insert("", "end", values=(
                tarea.titulo,
                tarea.fecha_de_vencimiento.strftime("%Y-%m-%d"),
                tarea.prioridad
            ))

    def agregar_tarea(self):
        titulo = simpledialog.askstring("Título", "Ingrese el título de la tarea:")
        if not titulo:
            return
        descripcion = simpledialog.askstring("Descripción", "Ingrese la descripción:")
        prioridad = simpledialog.askstring("Prioridad", "Ingrese la prioridad (1-5):")
        fecha_str = simpledialog.askstring("Vencimiento", "Ingrese la fecha de vencimiento (YYYY-MM-DD):")

        try:
            fecha = datetime.fromisoformat(fecha_str)
            nueva_tarea = Tarea(titulo, descripcion, fecha, "#FF0000", int(prioridad))
            self.tareas_controller.agregar_tarea(nueva_tarea)
            self.usuario_controller.guardar_usuario()
            self.refrescar_tareas()
        except Exception as e:
            print("Error al agregar tarea:", e)

    def editar_tarea(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleccionar Tarea", "Por favor, seleccione una tarea para editar.")
            return

        tarea_seleccionada = self.tareas_controller.obtener_tareas()[self.tree.index(selected_item)]
        titulo = simpledialog.askstring("Título", "Editar título de la tarea:", initialvalue=tarea_seleccionada.titulo)
        if not titulo:
            return
        descripcion = simpledialog.askstring("Descripción", "Editar descripción:", initialvalue=tarea_seleccionada.descripcion)
        prioridad = simpledialog.askstring("Prioridad", "Editar prioridad (1-5):", initialvalue=str(tarea_seleccionada.prioridad))
        fecha_str = simpledialog.askstring("Vencimiento", "Editar fecha de vencimiento (YYYY-MM-DD):", initialvalue=tarea_seleccionada.fecha_de_vencimiento.strftime("%Y-%m-%d"))

        try:
            fecha = datetime.fromisoformat(fecha_str)
            tarea_seleccionada.titulo = titulo
            tarea_seleccionada.descripcion = descripcion
            tarea_seleccionada.prioridad = int(prioridad)
            tarea_seleccionada.fecha_de_vencimiento = fecha
            self.usuario_controller.guardar_usuario()
            self.refrescar_tareas()
        except Exception as e:
            print("Error al editar tarea:", e)

    def eliminar_tarea(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleccionar Tarea", "Por favor, seleccione una tarea para eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmar Eliminación", "¿Estás seguro de eliminar esta tarea?")
        if confirmacion:
            tarea_seleccionada = self.tareas_controller.obtener_tareas()[self.tree.index(selected_item)]
            self.tareas_controller.eliminar_tarea(tarea_seleccionada)
            self.usuario_controller.guardar_usuario()
            self.refrescar_tareas()
