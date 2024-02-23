"""Define una clase base Animal con atributos comunes como nombre y edad.
Luego, crea dos clases derivadas, por ejemplo, Mamifero y Ave. 
Cada clase derivada debe tener al menos un atributo y un método específicos. 
Finalmente, crea instancias de las clases derivadas y muestra algunas características de cada animal."""

class Animal:
    def __init__ (self, nombreanimal, edadanimal,):
        self.nombreanimal=nombreanimal
        self.edadanimal=edadanimal

    def info_animal(self):
            print(f"El animal es {self.nombreanimal} y tiene {self.edadanimal} años")

class Mamifero(Animal):
    def __init__(self, nombreanimal, edadanimal, alimentacion):
        super().__init__(nombreanimal, edadanimal)
        self.alimentacion = alimentacion

    def alimentacion(self):
        self.info_animal()
        print(f"Alimentación: {self.alimentacion}")


class Ave(Animal):
    def __init__(self, nombreanimal, edadanimal, tipopico):
        super().__init__(nombreanimal, edadanimal)
        self.tipopico = tipopico

    def tipopico(self):
        self.info_animal()
        print(f"Tipo pico: {self.tipopico}")

nombre_mamifero = input("Ingrese el nombre del mamifero: ")
edad_mamifero = int(input("Ingrese la edad del mamifero: "))
alimentacion_mamifero = input("Ingrese la alimentación del mamifero: ")

nombre_ave = input("Ingrese el nombre del ave: ")
edad_ave = int(input("Ingrese la edad del ave: "))
tipopico_ave = input("Ingrese el tipo de pico del ave: ")

# Crear instancias de las clases derivadas
mamifero1 = Mamifero(nombre_mamifero, edad_mamifero, alimentacion_mamifero)
ave1 = Ave(nombre_ave, edad_ave, tipopico_ave)

# Mostrar información de los productos
print("Información del mamifero:")
mamifero1.alimentacion()

print("Información del ave:")
ave1.tipopico()