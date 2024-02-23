class Animal:
    def __init__(self, nombreanimal, edadanimal):
        self.nombreanimal = nombreanimal
        self.edadanimal = edadanimal

    def info_animal(self):
        print(f"El animal es {self.nombreanimal} y tiene {self.edadanimal} años")


class Mamifero(Animal):
    def __init__(self, nombreanimal, edadanimal, alimentacion):
        super().__init__(nombreanimal, edadanimal)
        self.tipo_alimentacion = alimentacion

    def mostrar_info(self):
        self.info_animal()
        print(f"Alimentación: {self.tipo_alimentacion}")


class Ave(Animal):
    def __init__(self, nombreanimal, edadanimal, tipopico):
        super().__init__(nombreanimal, edadanimal)
        self.tipo_pico = tipopico

    def mostrar_info(self):
        self.info_animal()
        print(f"Tipo de pico: {self.tipo_pico}")


nombre_mamifero = "perro"
edad_mamifero = 3
alimentacion_mamifero = "concentrado"

nombre_ave = "aguila"
edad_ave = 2
tipopico_ave = "tipo gancho"

# Crear instancias de las clases derivadas
mamifero1 = Mamifero(nombre_mamifero, edad_mamifero, alimentacion_mamifero)
ave1 = Ave(nombre_ave, edad_ave, tipopico_ave)

# Mostrar información de los productos
print("Información del mamífero:")
mamifero1.mostrar_info()

print("Información del ave:")
ave1.mostrar_info()