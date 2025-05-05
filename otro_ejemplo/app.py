import tkinter as tk
from views.main_window import MainWindow
from controllers.usuario_controller import UsuarioController

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestor de Usuario")
    usuario_controller = UsuarioController()
    app = MainWindow(root, usuario_controller)
    root.mainloop()