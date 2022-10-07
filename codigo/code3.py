class Producto():
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print("El producto se ha creado con éxito. ")

    def __str__(self):
        return

    def tipo_producto(producto1, producto2):
        producto1 = Producto(13, "Secador", 20, "Belleza")
        producto2 = Producto(13, "Plancha", 30, "Belleza")
        

