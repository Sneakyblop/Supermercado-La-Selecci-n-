def mostrar_catalogo(catalogo):
    """Muestra los productos disponibles con su precio."""
    print("\nCatálogo de productos:")
    print("Código | Producto     | Precio")
    print("-----------------------------------")
    for codigo, producto in catalogo.items():
        precio = producto['precio']
        if producto.get('unidad') == 'kg':
            precio_text = f"${precio:.2f}/kg"
        else:
            precio_text = f"${precio:.2f}"
        print(f"{codigo:>6} | {producto['nombre']:<12} | {precio_text:<10}")

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


def validar_numero_real(mensaje, minimo=0.0):
    """Solicita un número real y valida que sea mayor o igual al mínimo."""
    while True:
        try:
            valor = float(input(mensaje).strip().replace(',', '.'))
            if valor >= minimo:
                return valor
            print(f"Error: el valor debe ser mayor o igual a {minimo}.")
        except ValueError:
            print("Error: ingrese un número válido.")


def seleccionar_peso():
    """Solicita una cantidad en kilos o gramos y devuelve el valor en kilos."""
    while True:
        unidad = input("¿Desea ingresar la cantidad en kilos (k) o gramos (g)? ").strip().lower()
        if unidad in ("k", "kg", "kilo", "kilos"):
            return validar_numero_real("Ingrese la cantidad en kilos: ", minimo=0.01)
        if unidad in ("g", "gr", "gramo", "gramos"):
            gramos = validar_numero_real("Ingrese la cantidad en gramos: ", minimo=1)
            return gramos / 1000
        print("Error: ingrese 'k' para kilos o 'g' para gramos.")


def calcular_descuento_por_equipo(producto, equipo):
    """Calcula el descuento por equipo según el producto."""
    tags = producto.get("tags", [])
    if equipo == "Boca" and any(tag in tags for tag in ("polenta", "chancho")):
        return 0.15
    if equipo == "River" and any(tag in tags for tag in ("pollo", "fideos")):
        return 0.15
    if equipo == "Independiente":
        return 0.05
    return 0.0


def registrar_compra(catalogo, equipo):
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

        producto = catalogo[codigo]
        if producto.get("unidad") == "kg":
            cantidad = seleccionar_peso()
        else:
            cantidad = validar_numero_entero("Ingrese la cantidad: ", minimo=1)

        subtotal_linea = producto["precio"] * cantidad

        descuento_cantidad = 0.0
        if cantidad >= 3:
            descuento_cantidad = subtotal_linea * 0.10

        descuento_equipo = calcular_descuento_por_equipo(producto, equipo)
        descuento_equipo_monto = subtotal_linea * descuento_equipo

        total_descuento_linea = descuento_cantidad + descuento_equipo_monto
        total_linea = subtotal_linea - total_descuento_linea

        carrito.append({
            "codigo": codigo,
            "nombre": producto["nombre"],
            "precio": producto["precio"],
            "cantidad": cantidad,
            "unidad": producto.get("unidad", "unidad"),
            "subtotal": subtotal_linea,
            "descuento": total_descuento_linea,
            "descuento_cantidad": descuento_cantidad,
            "descuento_equipo": descuento_equipo_monto,
            "total": total_linea
        })

        formato_cantidad = f"{cantidad:.2f} kg" if producto.get("unidad") == "kg" else str(int(cantidad))
        print(f"Agregado: {formato_cantidad} de {producto['nombre']}")
        if descuento_cantidad > 0:
            print("¡Promo aplicada! Se otorgó un 10% de descuento por cantidad.")
        if descuento_equipo > 0:
            print(f"Descuento de equipo aplicado: {int(descuento_equipo * 100)}% en este producto.")

    return carrito

def calcular_total(carrito):
    """Calcula el total general del carrito y aplica un descuento por monto."""
    subtotal_general = sum(item["subtotal"] for item in carrito)
    total_lineas = sum(item["total"] for item in carrito)

    descuento_general = 0.0
    if total_lineas > 5000:
        descuento_general = total_lineas * 0.05

    total_general = total_lineas - descuento_general
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
    print(f"Productos comprados: {productos_totales:.2f}" if any(item.get('unidad') == 'kg' for item in carrito) else f"Productos comprados: {int(productos_totales)}")
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


def obtener_descuentos_equipo(equipo):
    """Devuelve el mensaje de descuentos según el equipo."""
    if equipo == "Boca":
        return "Con Boca tenés 15% de descuento en Polenta y Chancho."
    if equipo == "River":
        return "Con River tenés 15% de descuento en Pollo y Fideos."
    if equipo == "Independiente":
        return "Con Independiente tenés 5% de descuento en cualquier producto."
    if equipo == "Racing":
        return "Lo lamentamos, no pensábamos que todavía existían hinchas de este equipo. No hay descuentos especiales definidos."
    return "No hay descuentos de equipo para tu selección."


def seleccionar_equipo():
    """Solicita el equipo de fútbol al que pertenece el usuario."""
    equipos = {
        "boca": "Boca",
        "river": "River",
        "racing": "Racing",
        "independiente": "Independiente",
        "otro": "Otro"
    }
    while True:
        equipo = input("¿De qué equipo sos? (Boca/River/Racing/Independiente/Otro): ").strip().lower()
        if equipo in equipos:
            equipo_normalizado = equipos[equipo]
            mensaje_descuento = obtener_descuentos_equipo(equipo_normalizado)
            print(mensaje_descuento)
            return equipo_normalizado
        print("Equipo inválido. Ingrese Boca, River, Racing, Independiente u Otro.")


def main():
    catalogo = {
        1: {"nombre": "Leche", "precio": 1200, "unidad": "unidad"},
        2: {"nombre": "Pan", "precio": 800, "unidad": "unidad"},
        3: {"nombre": "Arroz", "precio": 1500, "unidad": "unidad"},
        4: {"nombre": "Yogur", "precio": 1000, "unidad": "unidad"},
        5: {"nombre": "Galletitas", "precio": 900, "unidad": "unidad"},
        6: {"nombre": "Polenta", "precio": 2500, "unidad": "unidad", "tags": ["polenta"]},
        7: {"nombre": "Chancho", "precio": 2000, "unidad": "kg", "tags": ["chancho"]},
        8: {"nombre": "Pollo", "precio": 1800, "unidad": "kg", "tags": ["pollo"]},
        9: {"nombre": "Fideos", "precio": 1400, "unidad": "unidad", "tags": ["fideos"]}
    }

    estadisticas = {
        "ventas_realizadas": 0,
        "productos_vendidos": 0,
        "monto_total": 0.0,
        "producto_mas_vendido": "Ninguno",
        "ventas_por_producto": {}
    }

    nombre_usuario = solicitar_nombre()
    equipo_usuario = seleccionar_equipo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_catalogo(catalogo)
        elif opcion == "2":
            carrito = registrar_compra(catalogo, equipo_usuario)
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
            print("Gracias por comprar en La Selección, tu super de confianza.")
            print("Grupo 20, Com C, AED 2026")
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
