class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []  

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print(" El precio y la cantidad deben ser positivos.")
            return
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        self.productos.append(producto)
        print(f" Producto '{nombre}' agregado correctamente.")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                if cantidad <= 0:
                    print(" La cantidad a vender debe ser positiva.")
                    return
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print(f" Venta realizada: {cantidad} unidad(es) de '{nombre}'.")
                else:
                    print(f" Stock insuficiente. Disponible: {producto['cantidad']}")
                return
        print(" El producto no existe en el inventario.")

    def mostrar_inventario(self):
        if not self.productos:
            print(" El inventario está vacío.")
            return
        print(f"\n Inventario de {self.nombre_tienda}:")
        for producto in self.productos:
            print(f"- {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")

    def producto_mas_caro(self):
        if not self.productos:
            print(" No hay productos en el inventario.")
            return
        mas_caro = max(self.productos, key=lambda x: x["precio"])
        print(f" El producto más caro es '{mas_caro['nombre']}' con un precio de ${mas_caro['precio']}.")

def menu():
    tienda = InventarioTienda("Mi Tiendita")

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver inventario")
        print("4. Consultar producto más caro")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                tienda.agregar_producto(nombre, precio, cantidad)
            except ValueError:
                print(" Entrada inválida. Precio y cantidad deben ser números.")

        elif opcion == "2":
            nombre = input("Nombre del producto a vender: ")
            try:
                cantidad = int(input("Cantidad a vender: "))
                tienda.vender_producto(nombre, cantidad)
            except ValueError:
                print(" Entrada inválida. La cantidad debe ser un número entero.")

        elif opcion == "3":
            tienda.mostrar_inventario()

        elif opcion == "4":
            tienda.producto_mas_caro()

        elif opcion == "5":
            print("hasta la proxima :b")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
