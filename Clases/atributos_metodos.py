class Usuario:
    # Atributo de clase, compartido por todas las instancias
    universidad = "UFPS"

    def __init__(self, nombre="", edad=18):
        # Atributo privado (__nombre) y protegido (_edad)
        self.__nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        # Getter para obtener el nombre
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        # Setter con validación de longitud
        if len(nuevo_nombre) > 3:
            self.__nombre = nuevo_nombre
        else:
            print("nombre muy corto")

    def __str__(self):
        # Método especial para representar el objeto como string
        return f" Nombre : {self.__nombre} ( Edad : {self._edad} )"

    def __eq__(self, otra):
        # Método especial para comparar dos objetos basándose en el nombre
        return self.__nombre == otra.__nombre

    def __secret(self):
        # Método privado, no accesible directamente
        print("Ultra secreto")
    
    def _lessSecret(self):
        # Método protegido, accesible pero indica que es de uso interno
        print("No tan secreto")

# Creación de un objeto de la clase Usuario
user = Usuario("Juan", 17)

# Llamada a un método protegido (es accesible pero no se recomienda)
user._lessSecret()

# Acceso a un método privado usando name mangling (no recomendado pero posible)
user._Usuario__secret()

# Uso del getter para obtener el nombre
print(user.nombre)

# Acceso directo al atributo protegido _edad (posible pero no recomendado)
print(user._edad)

# Modificación del atributo protegido (permitido pero debe evitarse en código real)
user._edad = 19

# Uso del setter para modificar el nombre con validación
user.nombre = "Dan"

# Impresión de los valores actualizados
print(user._edad)
print(user.nombre)

# Uso de dir() para ver los atributos y métodos del objeto
print(dir(Usuario()))

# Creación de más objetos Usuario
usuario1 = Usuario("Maria", 20)
usuario2 = Usuario("Carlos", 21)
usuario3 = Usuario("Maria", 20)

# Impresión de los objetos (usa __str__)
print(usuario1)
print(usuario3)

# Comparación de objetos usando __eq__
print(usuario1 == usuario3)  # Devolverá True ya que los nombres son iguales
