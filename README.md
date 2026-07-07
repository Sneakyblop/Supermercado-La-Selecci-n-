# Sistema de Gestión de Supermercado: "La Selección"

Este proyecto es una aplicación de consola desarrollada en Python que simula el funcionamiento estructurado de una caja de supermercado. Permite gestionar una compra básica, aplicar promociones específicas y procesar diferentes métodos de pago.

Comisión
* **Comisión:** Com C
* **Cátedra:** Algoritmos y Estructuras de Datos (AED 2026)
* **Grupo:** 20

### Integrantes:
* Galarza, Karla
* Martinez, Araceli Nazareth
* Ovelar, Eliana Anahí
* Pedretti, Maria Teresa


## Descripción General 
El sistema simula la experiencia de una línea de cajas mediante un menú interactivo en consola. Sus principales características son:

* **Gestión de Catálogo:** Soporta productos tanto por unidad como por peso (kilogramos/gramos) para la compra de carnes como pollo o chancho.
* **Sistema de Descuentos:** * Aplica un 10% de descuento automático en líneas de productos con 3 o más unidades.
  * Integra descuentos personalizados por el club de fútbol del cliente (ej. 15% en productos seleccionados para hinchas de Boca y River, o 5% general para Independiente).
  * Aplica un 5% de descuento general en compras mayores a $90000, con un tope de reintegro de 15 mil.
* **Procesamiento de Pagos:** Permite seleccionar pago con tarjeta (crédito/débito) o efectivo, otorgando un 10% de descuento adicional por pago en efectivo y calculando automáticamente el vuelto exacto del cliente.
* **Estadísticas:** Registra el total de ventas del usuario, su compra acumulada, el total de unidades vendidas y calcula cuál fue el producto más vendido.

## Instrucciones

### Requisitos Previos
* Tener instalado **Python 3.10** o superior en el sistema.
* No se requieren librerías externas (utilizamos únicamente módulos nativos de Python).

### Pasos para Ejecutar
1. Descargue o copie este repositorio en su computadora.
2. Con el archivo llamado "codigofuente" ejecute el archivo con el comando `codigofuente.py` o también puede correr el código desde la parte derecha con el símbolo de run y pone la opción "Run python file".
