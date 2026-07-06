# Sistema de Gestión de Supermercado: "La Selección"

Este proyecto es una aplicación de consola desarrollada en Python que simula el funcionamiento estructurado de una caja de supermercado. Permite gestionar de forma dinámica una compra, aplicar promociones específicas y procesar diferentes métodos de pago.

--------------------------------------------------------------------------------------------

## 👥 Integrantes y Comisión
* **Comisión:** Com C
* **Cátedra:** Algoritmos y Estructuras de Datos (AED 2026)
* **Grupo:** 20

### Integrantes:
* Galarza, Karla
* Martinez, Araceli Nazareth
* Ovelar, Eliana Anahí
* Pedretti, Maria Teresa

-------------------------------------------

## 📝 Descripción General 
El sistema simula la experiencia completa de una línea de cajas mediante un menú interactivo en consola. Sus principales características son:

* **Gestión de Catálogo:** Soporta productos tanto por unidad como por peso (kilogramos/gramos) con un formateo limpio en pantalla.
* **Sistema de Descuentos:** * Aplica un 10% de descuento automático en líneas de productos con 3 o más unidades.
  * Integra descuentos personalizados por el club de fútbol del cliente (ej. 15% en productos seleccionados para hinchas de Boca y River, o 5% general para Independiente).
  * Aplica un 5% de descuento general en compras mayores a $5000.
* **Procesamiento de Pagos:** Permite seleccionar pago con tarjeta (crédito/débito) o efectivo, otorgando un 10% de descuento adicional por pago en efectivo y calculando automáticamente el vuelto exacto del cliente.
* **Estadísticas:** Registra el total de ventas, la facturación acumulada, el total de unidades vendidas y calcula cuál fue el producto más vendido de la jornada.
* **Entrada de Datos:** Cuenta con funciones de validación para evitar que el programa falle ante ingresos vacíos, letras o números fuera de rango.

---

## 🚀 Instrucciones

### Requisitos Previos
* Tener instalado **Python 3.10** o superior en el sistema.
* No se requieren librerías externas (utiliza únicamente módulos nativos de Python).

### Pasos para Ejecutar
1. Descargá o cloná este repositorio en tu computadora.
2. Navegá hasta la carpeta donde se encuentran los archivos.
4. Ejecutá el archivo `codigofuente.py`.