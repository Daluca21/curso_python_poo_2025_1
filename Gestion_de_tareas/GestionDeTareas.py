import models.Tarea as t
import models.Usuario as u
usuario = u.Usuario("Juan")
tarea = t.Tarea()
usuario.agregarTarea(tarea)

for i in range(0, 10):
    tareat = t.Tarea()
    print(tareat)
    usuario.agregarTarea(tareat)
print(len(usuario.tareas))
usuario.eliminarTarea(tarea)
print(len(usuario.tareas))
