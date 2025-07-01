class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def Actualizar_stock(self, cantidad):
        if self.stock + cantidad < 0 or cantidad == 0:
            print("No se puede actualizar el stock a un valor negativo o cero.")
        else:
            self.stock += cantidad
            print(f"Stock actualiazado para {self.nombre}. Nuevo stock: {self.stock}")

def Agregar_producto (catalogo):
    codigo = input ("Ingrese el código del producto: ")
    if codigo in catalogo:
        print("El producto ya existe. Pruebe la opción de actualizar stock.")
    else:
        nombre= input("Ingrese nombre del producto: ")
        precio= float(input("Ingrese precio del producto: "))
        stock = int(input("Ingrese stock del producto: "))
        catalogo[codigo] = Producto(codigo, nombre, precio, stock)
        print(f"Producto {nombre} agregado con éxito.")

def Mostrar_productos(catalogo):
    if not catalogo:
        print("No hay productos en el registro.")
    else:
        print ("Productos registrados:")
        for producto in catalogo.values():
            print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}")

def main():
    catalogo = {}
    while True:
        print("\nMenú de opciones:")
        print("1.Agregar un nuevo producto")
        print("2.Actualizar stock de un producto")
        print("3.Mostar todos los productos")
        print("4.Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            Agregar_producto(catalogo)
        elif opcion == "2":
            codigo = input("Ingrese el código del producto que quiera actualizar: ")
            if codigo in catalogo:
                cantidad = int(input("Ingrese la cantidad que quiera actualizar (puede ser negativa): "))
                catalogo[codigo].Actualizar_stock(cantidad)
            else:
                print("Ese producto no existe. Pruebe la opción de agregar un producto.")
        elif opcion == "3":
            Mostrar_productos(catalogo)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

main()




