
class Tarea :
    def __init__ ( self , titulo , descripcion , fecha_vencimiento ):
        self . titulo = titulo
        self . descripcion = descripcion
        self . fecha_vencimiento = fecha_vencimiento
        self . completada = False

    def marcar_completada ( self ):
        self . completada = True

class TareaPrioritaria ( Tarea ):
    def __init__ ( self , titulo , descripcion , fecha_vencimiento ,prioridad ) :
        super () . __init__ ( titulo , descripcion , fecha_vencimiento )
        self . prioridad = prioridad

    def es_urgente ( self ):
        return self . prioridad == 1
    
class TareaRecurrente ( Tarea ):
    def __init__ ( self , titulo , descripcion , fecha_vencimiento , frecuencia) :
        super () . __init__ ( titulo , descripcion , fecha_vencimiento )
        self.frecuencia = frecuencia

    def siguiente_fecha ( self ):
        return f"La tarea se repetirá { self.frecuencia }."

class Persona :
    def __init__ ( self , nombre , edad ):
        self . nombre = nombre
        self . edad = edad

    def presentarse ( self ):
        return f"Hola , soy { self.nombre } y tengo { self.edad } años ."

class Estudiante ( Persona ):
    def __init__ ( self , nombre , edad , universidad, tarea):
        super().__init__ ( nombre , edad )
        self.universidad = universidad
        self.tarea = tarea
    
    def presentarse(self):
        return "?"


    def presentarse(self,):
        return f"Hola , soy { self.nombre } y tengo { self.edad } años, estudio en {self.universidad}."
    

tarea1 = Tarea("Estudiar", "Revisar concepto producto cartesiano", "28-03")
est = Estudiante (" Ana ", 20 , "Nacional", tarea1)
#print(est.presentarse())

tareaDelEstudiante = est.tarea

print(tareaDelEstudiante == tarea1)
tareaDelEstudiante.titulo = "Cambio"
print(tarea1.titulo, tareaDelEstudiante.titulo, est.tarea.titulo)

tarea2 = TareaPrioritaria("Buscar", "Buscar algo?", "28-03", 1)
tarea3 = TareaPrioritaria("Preparar", "Preparar comida?", "29-03", 2)

tarea1.marcar_completada()
print("Tarea completada" if tarea1.completada else "Tarea no completada")
print("Tarea 2 es de urgente", "SI" if tarea2.es_urgente() else "NO")
print("Tarea 3 es de urgente", "SI" if tarea3.es_urgente() else "NO")
tarea2.marcar_completada()
tarea3.marcar_completada()

tarea4 = TareaRecurrente("Dormir", "Dormir a las 10 pm", "28-12", "diaria")

print(tarea4.siguiente_fecha())