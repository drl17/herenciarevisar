"""Crea una clase base Producto con atributos como nombre, precio, y cantidad_en_stock. 
Luego, crea dos clases derivadas, por ejemplo, Electronico y Ropa.
Cada clase derivada debe tener atributos y métodos específicos.
Crea instancias de las clases derivadas y muestra información sobre los productos en una tienda."""

class Producto:
    def __init__(self, nombreproducto, precioproducto, cantidadstock):
        self.nombreproducto = nombreproducto
        self.precioproducto = precioproducto
        self.cantidadstock = cantidadstock

    def info_producto(self):
        print(f"El producto es {self.nombreproducto}, tiene un precio de {self.precioproducto} y existen {self.cantidadstock} unidades en stock")


class Electronico(Producto):
    def __init__(self, nombreproducto, precioproducto, cantidadstock, fabricanteproducto):
        super().__init__(nombreproducto, precioproducto, cantidadstock)
        self.fabricanteproducto = fabricanteproducto

    def mostrar_info(self):
        self.info_producto()
        print(f"Fabricante: {self.fabricanteproducto}")


class Ropa(Producto):
    def __init__(self, nombreproducto, precioproducto, cantidadstock, marcaprenda):
        super().__init__(nombreproducto, precioproducto, cantidadstock)
        self.marcaprenda = marcaprenda

    def mostrar_info(self):
        self.info_producto()
        print(f"Marca de la prenda: {self.marcaprenda}")


nombre_electronico = "nevera"
precio_electronico = "$4,320,000"
cantidadstock_electronico = 3
fabricante_electronico = "LG"

nombre_ropa = "camiseta"
precio_ropa = "$150,000"
cantidadstock_ropa = "65"
marcaprenda_ropa = "Arturo Calle"

# Crear instancias de las clases derivadas
Electronico1 = Electronico(nombre_electronico, precio_electronico, cantidadstock_electronico, fabricante_electronico)
Ropa1 = Ropa(nombre_ropa, precio_ropa, cantidadstock_ropa, marcaprenda_ropa)

# Mostrar información de los productos
print("Información del producto electrónico es:")
Electronico1.mostrar_info()

print("Información de la prenda de ropa es:")
Ropa1.mostrar_info()