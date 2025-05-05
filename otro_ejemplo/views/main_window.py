# Importación de módulos necesarios de Tkinter
import tkinter as tk
from tkinter import ttk, messagebox

# Importación de vistas específicas desde el paquete de vistas
from views.tareas_view import TareasView
from views.notas_view import NotasView
from views.materias_view import MateriasView

# Definición de la clase principal de la ventana principal
class MainWindow:
    def __init__(self, root, usuario_controller):
        self.root = root  # Referencia a la ventana principal de Tkinter
        self.usuario_controller = usuario_controller  # Controlador que gestiona al usuario y sus datos

        # Creación del frame principal con un padding de 20 pixeles
        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack()  # Agrega el frame al layout

        # Etiqueta de bienvenida que muestra el nombre del usuario
        ttk.Label(self.frame, text=f"Bienvenido {self.usuario_controller.usuario.nombre}", font=("Arial", 14)).pack(pady=10)

        # Botón para acceder a la vista de tareas
        ttk.Button(self.frame, text="Ver Tareas", command=self.ver_tareas).pack(fill="x", pady=5)

        # Botón para acceder a la vista de notas
        ttk.Button(self.frame, text="Ver Notas", command=self.ver_notas).pack(fill="x", pady=5)

        # Botón para acceder a la vista de materias
        ttk.Button(self.frame, text="Ver Materias", command=self.ver_materias).pack(fill="x", pady=5)

        # Botón para guardar los cambios del usuario
        ttk.Button(self.frame, text="Guardar Cambios", command=self.guardar).pack(fill="x", pady=20)

    # Método que abre la vista de tareas
    def ver_tareas(self):
        TareasView(self.root, self.usuario_controller.get_tareas_controller(), self.usuario_controller)

    # Método que abre la vista de notas
    def ver_notas(self):
        NotasView(self.root, self.usuario_controller.get_notas_controller(), self.usuario_controller)

    # Método que abre la vista de materias
    def ver_materias(self):
        MateriasView(self.root, self.usuario_controller.get_materias_controller(), self.usuario_controller)

    # Método que guarda los datos del usuario y muestra un mensaje de confirmación
    def guardar(self):
        self.usuario_controller.guardar_usuario()
        messagebox.showinfo("Guardado", "Usuario guardado correctamente")
