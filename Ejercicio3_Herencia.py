"""Define una clase base Vehiculo con atributos comunes como marca y modelo.
Luego, crea dos clases derivadas, por ejemplo, Coche y Bicicleta.
Cada clase derivada debe tener atributos y métodos específicos.
Crea instancias de las clases derivadas y muestra algunas características de cada vehículo."""

class Vehiculo:
    def __init__(self, marcavehiculo, modelovehiculo):
        self.marcavehiculo = marcavehiculo
        self.modelovehiculo = modelovehiculo

    def info_Vehiculo(self):
        print(f"El vehículo es de marca {self.marcavehiculo} y es modelo {self.modelovehiculo}")


class Coche(Vehiculo):
    def __init__(self, marcavehiculo, modelovehiculo, combustible):
        super().__init__(marcavehiculo, modelovehiculo)
        self.combustible = combustible

    def mostrar_info(self):
        self.info_Vehiculo()
        print(f"Combustible: {self.combustible}")

class Bicicleta(Vehiculo):
    def __init__(self, marcavehiculo, modelovehiculo, tipobicicleta):
        super().__init__(marcavehiculo, modelovehiculo)
        self.tipobicicleta = tipobicicleta

    def mostrar_info(self):
        self.info_Vehiculo()
        print(f"El tipo de la bicicleta es: {self.tipobicicleta}")


marcacoche = "Audi"
modelovehiculo = "A7"
combustiblevehiculo = "Eléctrico"

marcabicicleta = "GW"
modelobicicleta = "Scorpion"
tipobicicleta = "Montaña MTB"

# Crear instancias de las clases derivadas
Coche1 = Coche(marcacoche, modelovehiculo, combustiblevehiculo)
Bicicleta1 = Bicicleta(marcabicicleta, modelobicicleta, tipobicicleta)

# Mostrar información de los productos
print("Información del coche es:")
Coche1.mostrar_info()

print("Información de la bicicleta es:")
Bicicleta1.mostrar_info()