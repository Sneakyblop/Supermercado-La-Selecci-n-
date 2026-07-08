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
    """Calcula el descuento por equipo según el equipo del cliente y la etiqueta del producto."""
    tags = producto.get("tags", [])
    if equipo == "Boca" and "boca" in tags:
        return 0.15
    if equipo == "River" and "river" in tags:
        return 0.15
    if equipo == "Independiente" and "independiente" in tags:
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
    if total_lineas > 90000:
        descuento_general = min(total_lineas * 0.05, 15000)

    total_general = total_lineas - descuento_general
    return subtotal_general, descuento_general, total_general

def generar_ticket(carrito, subtotal_general, descuento_general, total_general, total_pagado, estadisticas, descuento_efectivo=0.0, interes_credito=0.0, cuotas_credito=1, descuento_jubilado=0.0):
    """Imprime el ticket y actualiza las estadísticas del sistema."""
    print("\n=== TICKET DE COMPRA ===")
    print("Producto | Cantidad | Precio unit. | Total")
    print("--------------------------------------------")

    for item in carrito:
        print(f"{item['nombre']} | {item['cantidad']} | ${item['precio']:.2f} | ${item['total']:.2f}")

    # El descuento_general que se recibe corresponde únicamente al
    # descuento adicional por monto (5% si corresponde). Los descuentos
    # aplicados por producto ya fueron restados en los totales por línea.
    total_descuentos = subtotal_general - total_general

    print(f"Subtotal: ${subtotal_general:.2f}")
    print(f"Subtotal: ${subtotal_general:.2f}")
    print(f"Descuentos aplicados (total): ${total_descuentos:.2f}")
    if descuento_general > 0:
        print("Descuento por compra mayor a $90.000 aplicado (tope $15.000).")
    if descuento_jubilado > 0: #NUEVAS LÍNEA
        print(f"Beneficio Jubilados (15%): -${descuento_jubilado:.2f}")
    if descuento_efectivo > 0:
        print(f"Descuento por pago en efectivo: ${descuento_efectivo:.2f}.")
    if interes_credito > 0:
        print(f"Pago en {cuotas_credito} cuotas con interés: {int(interes_credito * 100)}%.")
    print(f"Total a pagar: ${total_pagado:.2f}")

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
    if estadisticas['ventas_realizadas'] == 0:
        print("No se han registrado ventas aún.")
        print(f"Ventas realizadas: {estadisticas['ventas_realizadas']}")
        print(f"Productos vendidos: {estadisticas['productos_vendidos']}")
        print(f"Monto total facturado: ${estadisticas['monto_total']:.2f}")
        return
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

    print("\nGracias por su compra, vuelva pronto.")
    print("=== RESUMEN DE SU COMPRA ===")
    print(f"Productos comprados: {productos_totales:.2f}" if any(item.get('unidad') == 'kg' for item in carrito) else f"Productos comprados: {int(productos_totales)}")
    print(f"Producto más comprado: {producto_mas_comprado}")
    print(f"Valor total a pagar: ${total_general:.2f}")

def mostrar_menu(es_gerente=False):
    """Imprime el menú principal del sistema."""
    print("\n=== SUPERMERCADO ===")
    print("1. Ver catálogo")
    if es_gerente:
        print("2. Cargar producto nuevo")
        print("3. Ver estadísticas")
        print("4. Salir")
    else:
        print("2. Iniciar compra")
        print("3. Ver estadísticas")
        print("4. Salir")


def preguntar_si_gerente():
    """Pregunta si el usuario es gerente."""
    while True:
        respuesta = input("¿Es usted gerente? (s/n): ").strip().lower()
        if respuesta in ("s", "si"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Responda con 's' o 'n'.")


def solicitar_nombre_gerente():
    """Solicita el nombre del gerente."""
    while True:
        nombre = input("Por favor, ingrese su nombre de gerente: ").strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío. Intente nuevamente.")


def generar_codigo_nuevo(catalogo):
    """Genera un nuevo código para un producto añadido."""
    return max(catalogo.keys(), default=0) + 1


def cargar_producto(catalogo):
    """Permite a un gerente cargar un producto nuevo al catálogo."""
    print("\n=== CARGA DE PRODUCTO NUEVO ===")
    nombre = input("Nombre del producto: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre del producto: ").strip()

    precio = validar_numero_real("Precio unitario: ", minimo=1)

    while True:
        unidad = input("Unidad del producto (unidad/kg): ").strip().lower()
        if unidad in ("unidad", "kg"):
            break
        print("Ingrese 'unidad' o 'kg'.")

    tags = []
    print("¿El producto debe recibir descuentos por equipo?")
    print("1. Boca")
    print("2. River")
    print("3. Independiente")
    print("4. Racing")
    print("5. Ninguno")
    while True:
        opcion = input("Seleccione opción de descuento de equipo (1-5): ").strip()
        if opcion == "1":
            tags = ["boca"]
            break
        if opcion == "2":
            tags = ["river"]
            break
        if opcion == "3":
            tags = ["independiente"]
            break
        if opcion == "4":
            tags = ["racing"]
            break
        if opcion == "5":
            tags = []
            break
        print("Opción inválida. Ingrese un número entre 1 y 5.")

    codigo = generar_codigo_nuevo(catalogo)
    catalogo[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "unidad": unidad,
        "tags": tags
    }
    print(f"Producto agregado: {codigo} - {nombre} (${precio:.2f}/{unidad})")

def solicitar_edad():
    """Solicita la edad del usuario para verificar si aplica descuento de jubilado."""
    # Reutilizamos la función validar_numero_entero que ya programaron
    edad = validar_numero_entero("Por favor, ingrese su edad: ", minimo=1)
    if edad >= 70:
        print("¡Beneficio jubilado activo! Se le otorgará un 15% de descuento en el total de su compra.")
    else :
        print("No sabemos si es bueno o malo, pero por el momento no tienes acceso al beneficio de jubilados.")
    return edad

def solicitar_dni():
    """Solicita el DNI del usuario antes de iniciar el sistema."""
    print("Bienvenido al supermercado La Selección.")
    while True:
        dni = input("Por favor, ingrese su DNI (8 números): ").strip()
        if not dni:
            print("El DNI no puede estar vacío. Intente nuevamente.")
            continue
        if not dni.isdigit():
            print("El DNI debe contener solo números. Intente nuevamente.")
            continue
        if len(dni) != 8:
            print("El DNI debe tener exactamente 8 dígitos. Intente nuevamente.")
            continue
        return dni


def obtener_descuentos_equipo(equipo):
    """Devuelve el mensaje de descuentos según el equipo."""
    if equipo == "Boca":
        return "Con Boca tenés 15% de descuento en productos promocionados para Boca."
    if equipo == "River":
        return "Con River tenés 15% de descuento en productos promocionados para River."
    if equipo == "Independiente":
        return "Con Independiente tenés 5% de descuento en productos promocionados para Independiente."
    if equipo == "Racing":
        return "Lo lamentamos, no hay descuentos para Racing por el momento."
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

def procesar_pago(total_a_pagar):
    """Gestiona el método de pago, aplica descuento por efectivo y calcula el vuelto o interés."""
    print(f"\nMonto final a abonar: ${total_a_pagar:.2f}")
    print("Seleccione método de pago:")
    print("1. Efectivo (10% de descuento adicional)")
    print("2. Tarjeta de Débito")
    print("3. Tarjeta de Crédito")
    
    while True:
        opcion = input("Opción: ").strip()
        if opcion == "1":
            descuento_efectivo = total_a_pagar * 0.10
            total_con_descuento = total_a_pagar - descuento_efectivo
            print(f"¡Descuento por efectivo aplicado! Nuevo total: ${total_con_descuento:.2f}")
            
            while True:
                pago = validar_numero_real("¿Con cuánto va a pagar? (Monto del billete): ")
                if pago >= total_con_descuento:
                    vuelto = pago - total_con_descuento
                    print(f"Su vuelto es: ${vuelto:.2f}")
                    return total_con_descuento, descuento_efectivo, 0.0, 1
                print("Error: El monto ingresado es menor al total a pagar.")
                
        elif opcion == "2":
            print("Pago con tarjeta aprobado.")
            return total_a_pagar, 0.0, 0.0, 1

        elif opcion == "3":
            cuotas = validar_numero_entero("¿En cuántas cuotas desea pagar? (1, 2, 3 o 6): ", minimo=1)
            if cuotas not in (1, 2, 3, 6):
                print("Seleccione 1, 2, 3 o 6 cuotas.")
                continue
            interes_porcentaje = {1: 0.0, 2: 0.07, 3: 0.12, 6: 0.15}[cuotas]
            total_con_interes = total_a_pagar * (1 + interes_porcentaje)
            print(f"Pago en {cuotas} cuotas con interés del {int(interes_porcentaje * 100)}%. Total: ${total_con_interes:.2f}")
            return total_con_interes, 0.0, interes_porcentaje, cuotas
            
        print("Opción inválida. Intente nuevamente.")

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

    es_gerente = preguntar_si_gerente()
    nombre_gerente = None
    dni_usuario = None
    edad_usuario = 0
    equipo_usuario = None

    if es_gerente:
        nombre_gerente = solicitar_nombre_gerente()
        print(f"Bienvenido, {nombre_gerente}. Como gerente tiene permitida la carga de productos nuevos.")
    else:
        dni_usuario = solicitar_dni()
        edad_usuario = solicitar_edad()  # NUEVA LÍNEA
        equipo_usuario = seleccionar_equipo()

    while True:
        mostrar_menu(es_gerente)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_catalogo(catalogo)
        elif es_gerente and opcion == "2":
            cargar_producto(catalogo)
        elif es_gerente and opcion == "3":
            mostrar_estadisticas(estadisticas)
        elif es_gerente and opcion == "4":
            print("Gracias por comprar en La Selección, tu super de confianza.")
            print("Grupo 20, Com C, AED 2026")
            break
        elif not es_gerente and opcion == "2":
            carrito = registrar_compra(catalogo, equipo_usuario)
            if carrito:
                # 1. Calculamos los totales iniciales de la compra
                subtotal_general, descuento_general, total_general = calcular_total(carrito)
                
                # DESCUENTO POR JUBILADO
                descuento_jubilado = 0.0
                if edad_usuario >= 70:
                    descuento_jubilado = total_general * 0.15
                    total_general -= descuento_jubilado
                
                # 2. LLAMAMOS A LA FUNCIÓN: Le pasamos el total_general ya modificado
                total_final_pagado, descuento_efectivo, interes_credito, cuotas_credito = procesar_pago(total_general)
                
                # 3. Imprimimos el ticket pasando el nuevo parámetro descuento_jubilado
                generar_ticket(carrito, subtotal_general, descuento_general, total_general, total_final_pagado, estadisticas, 
                               descuento_efectivo=descuento_efectivo, interes_credito=interes_credito, cuotas_credito=cuotas_credito,
                               descuento_jubilado=descuento_jubilado) # <- MODIFICADO
                
                mostrar_resumen_compra(dni_usuario, carrito, total_final_pagado)
                print("\nLa compra finalizó correctamente. Puede volver al menú para ver estadísticas o salir con la opción 4.")
            else:
                print("No se registraron productos.")
            continue
        elif not es_gerente and opcion == "3":
            mostrar_estadisticas(estadisticas)
        elif not es_gerente and opcion == "4":
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