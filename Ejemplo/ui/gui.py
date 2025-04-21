import tkinter as tk
from tkinter import simpledialog, messagebox
from models.task_manager import TaskManager

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.manager = TaskManager()

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(padx=10, pady=10)

        self.load_tasks()

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Agregar", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Completar", command=self.complete_task).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self.delete_task).grid(row=0, column=2, padx=5)

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.manager.get_tasks():
            status = "✓" if task.completed else "✗"
            self.task_listbox.insert(tk.END, f"[{status}] {task.title} - {task.description}")

    def add_task(self):
        title = simpledialog.askstring("Nueva tarea", "Título:")
        if title:
            desc = simpledialog.askstring("Descripción", "Descripción (opcional):")
            fecha = simpledialog.askstring("Fecha de vencimiento", "Fecha:")
            self.manager.add_task(title, desc or '')
            self.load_tasks()

    def complete_task(self):
        index = self.task_listbox.curselection()
        if index:
            self.manager.complete_task(index[0])
            self.load_tasks()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea primero.")

    def delete_task(self):
        index = self.task_listbox.curselection()
        if index:
            self.manager.delete_task(index[0])
            self.load_tasks()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea primero.")
