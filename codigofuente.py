def mostrar_catalogo(catalogo):
    """Muestra los productos disponibles con su precio."""
    print("\nCatálogo de productos:")
    print("Código | Producto | Precio")
    print("--------------------------")
    for codigo, producto in catalogo.items():
        print(f"{codigo:>6} | {producto['nombre']:<12} | ${producto['precio']:.2f}")

def validar_numero_entero(mensaje, minimo=0, permitir_cero=False):
    """Solicita un número entero y valida que cumpla con el rango pedido."""
    while True:
        try:
            valor = int(input(mensaje).strip())
            if permitir_cero and valor == 0:
                return valor
            if valor >= minimo:
                return valor
            print(f"Error: el valor debe ser mayor o igual a {minimo}.")
        except ValueError:
            print("Error: ingrese un número entero válido.")

def registrar_compra(catalogo):
    """Permite cargar productos al carrito hasta que el usuario finalice."""
    carrito = []

    while True:
        mostrar_catalogo(catalogo)
        print("\n0. Finalizar compra")

        codigo = validar_numero_entero("Ingrese el código del producto: ", minimo=0, permitir_cero=True)

        if codigo == 0:
            break

        if codigo not in catalogo:
            print("Error: código inexistente. Intente nuevamente.")
            continue

        cantidad = validar_numero_entero("Ingrese la cantidad: ", minimo=1)

        producto = catalogo[codigo]
        subtotal_linea = producto["precio"] * cantidad

        descuento_linea = 0
        if cantidad >= 3:
            descuento_linea = subtotal_linea * 0.10

        total_linea = subtotal_linea - descuento_linea

        carrito.append({
            "codigo": codigo,
            "nombre": producto["nombre"],
            "precio": producto["precio"],
            "cantidad": cantidad,
            "subtotal": subtotal_linea,
            "descuento": descuento_linea,
            "total": total_linea
        })

        print(f"Agregado: {cantidad} x {producto['nombre']}")
        if cantidad >= 3:
            print("¡Promo aplicada! Se otorgó un 10% de descuento por cantidad.")

    return carrito

def calcular_total(carrito):
    """Calcula el total general del carrito y aplica un descuento por monto."""
    subtotal_general = sum(item["subtotal"] for item in carrito)

    descuento_general = 0.0
    if subtotal_general > 5000:
        descuento_general = subtotal_general * 0.05

    total_general = subtotal_general - descuento_general
    return subtotal_general, descuento_general, total_general

def generar_ticket(carrito, subtotal_general, descuento_general, total_general, estadisticas):
    """Imprime el ticket y actualiza las estadísticas del sistema."""
    print("\n=== TICKET DE COMPRA ===")
    print("Producto | Cantidad | Precio unit. | Total")
    print("--------------------------------------------")

    for item in carrito:
        print(f"{item['nombre']} | {item['cantidad']} | ${item['precio']:.2f} | ${item['total']:.2f}")

    print(f"Subtotal: ${subtotal_general:.2f}")
    print(f"Descuento aplicado: ${descuento_general:.2f}")
    print(f"Total a pagar: ${total_general:.2f}")

    estadisticas["ventas_realizadas"] += 1
    estadisticas["monto_total"] += total_general

    for item in carrito:
        estadisticas["productos_vendidos"] += item["cantidad"]
        estadisticas["ventas_por_producto"][item["nombre"]] = (
            estadisticas["ventas_por_producto"].get(item["nombre"], 0) + item["cantidad"]
        )

    if estadisticas["ventas_por_producto"]:
        producto_mas_vendido = max(
            estadisticas["ventas_por_producto"],
            key=estadisticas["ventas_por_producto"].get
        )
        estadisticas["producto_mas_vendido"] = producto_mas_vendido

def mostrar_estadisticas(estadisticas):
    """Muestra las estadísticas generales del supermercado."""
    print("\n=== ESTADÍSTICAS ===")
    print(f"Ventas realizadas: {estadisticas['ventas_realizadas']}")
    print(f"Productos vendidos: {estadisticas['productos_vendidos']}")
    print(f"Monto total facturado: ${estadisticas['monto_total']:.2f}")
    print(f"Producto más vendido: {estadisticas['producto_mas_vendido']}")

def mostrar_resumen_compra(nombre, carrito, total_general):
    """Muestra un resumen final de la compra del cliente."""
    productos_totales = sum(item['cantidad'] for item in carrito)
    producto_mas_comprado = 'Ninguno'
    if carrito:
        producto_mas_comprado = max(carrito, key=lambda item: item['cantidad'])['nombre']

    print(f"\nGracias por su compra, {nombre}.")
    print("=== RESUMEN DE SU COMPRA ===")
    print(f"Productos comprados: {productos_totales}")
    print(f"Producto más comprado: {producto_mas_comprado}")
    print(f"Valor total a pagar: ${total_general:.2f}")

def mostrar_menu():
    """Imprime el menú principal del sistema."""
    print("\n=== SUPERMERCADO ===")
    print("1. Ver catálogo")
    print("2. Iniciar compra")
    print("3. Ver estadísticas")
    print("4. Salir")

def solicitar_nombre():
    """Solicita el nombre del usuario antes de iniciar el sistema."""
    print("Bienvenido al supermercado La Selección.")
    while True:
        nombre = input("Por favor, ingrese su nombre: ").strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío. Intente nuevamente.")


def main():
    catalogo = {
        1: {"nombre": "Leche", "precio": 1200},
        2: {"nombre": "Pan", "precio": 800},
        3: {"nombre": "Arroz", "precio": 1500},
        4: {"nombre": "Yogur", "precio": 1000},
        5: {"nombre": "Galletitas", "precio": 900}
    }

    estadisticas = {
        "ventas_realizadas": 0,
        "productos_vendidos": 0,
        "monto_total": 0.0,
        "producto_mas_vendido": "Ninguno",
        "ventas_por_producto": {}
    }

    nombre_usuario = solicitar_nombre()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_catalogo(catalogo)
        elif opcion == "2":
            carrito = registrar_compra(catalogo)
            subtotal_general, descuento_general, total_general = calcular_total(carrito)
            if carrito:
                generar_ticket(carrito, subtotal_general, descuento_general, total_general, estadisticas)
            else:
                print("No se registraron productos.")
            mostrar_resumen_compra(nombre_usuario, carrito, total_general)
            break
        elif opcion == "3":
            mostrar_estadisticas(estadisticas)
        elif opcion == "4":
            print(f"Gracias por usar el sistema, {nombre_usuario}.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSistema detenido por el usuario.")
    except EOFError:
        print("\nSe cerró la entrada de datos.")
