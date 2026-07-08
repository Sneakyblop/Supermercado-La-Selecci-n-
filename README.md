# Sistema de Gestión de Supermercado: "La Selección"

Este proyecto es una aplicación de consola desarrollada en Python que simula el funcionamiento de una caja de supermercado. Permite gestionar una compra básica, aplicar promociones específicas y procesar diferentes métodos de pago, con una clara diferencia entre gerentes (tienen autorizacion de cargar productos nuevos) y clientes/usuarios.

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
El sistema simula la experiencia de una línea de cajas mediante un menú en consola. Sus principales características son:

* **Gestión de Catálogo:** Soporta productos tanto por unidad como por peso (kilogramos/gramos) para la compra de carnes como pollo o chancho.
* **Sistema de Descuentos:** * Aplica un 10% de descuento automático en líneas de productos con 3 o más unidades.
  * Integra descuentos personalizados por el club de fútbol del cliente (ej. 15% en productos seleccionados para hinchas de Boca y River, o 5% general para Independiente).
  * Aplica un 5% de descuento general en compras mayores a $90000, con un tope de reintegro de 15 mil.
* **Procesamiento de Pagos:** Permite seleccionar pago con tarjeta (crédito/débito) o efectivo, otorgando un 10% de descuento adicional por pago en efectivo y calculando automáticamente el vuelto exacto del cliente, agregando que las tarjetas de crédito tendran aumentos por cada cantidad de cuotas que elija el usuario.
* **Estadísticas:** Registra el total de ventas del usuario, su compra acumulada, el total de unidades vendidas y calcula cuál fue el producto más vendido.
* **•	Diferencia entre:
o	gerente (puede cargar productos nuevos).
o	cliente (realiza compras).

## Funciones principales
•	mostrar_catalogo: imprime los productos disponibles
•	registrar_compra: arma el carrito con cada producto elegido
•	procesar_pago: maneja los métodos de pago y descuentos adicionales
•	generar_ticket: imprime el ticket final y actualiza las estadísticas
•	mostrar_menu: muestra el menú según si es gerente o cliente
•	solicitar_dni: pide el DNI del cliente y lo valida
•	cargar_producto: permite al gerente agregar nuevos productos y sus descuentos


## Instrucciones

### Requisitos Previos
* Tener instalado **Python 3.10** o superior en el sistema.
* No se requieren librerías externas (utilizamos únicamente módulos nativos de Python).

### Pasos para Ejecutar
1. Descargue o copie este repositorio en su computadora.
2. Con el archivo llamado "codigofuente" ejecute el archivo con el comando `codigofuente.py` o también puede correr el código desde la parte derecha con el símbolo de run y pone la opción "Run python file".
3. Ver imágenes de referencia: 
   ![image alt](https://github.com/Sneakyblop/Supermercado-La-Selecci-n-/blob/master/Captura%20de%20pantalla%202026-07-08%20103912.png?raw=true)
   ![image alt](https://github.com/Sneakyblop/Supermercado-La-Selecci-n-/blob/master/Captura%20de%20pantalla%202026-07-08%20103933.png?raw=true)

## Utilización de la IA:
El principal uso que le dimos a la IA fue para que subiera los pequeños cambios que hacíamos en VS Code al repositorio, esto porque constantemente nos saltaba el siguiente error: 
C:\Users\Mari\Documents\python supermercado 2026> git push --set-upstream origin master
remote: Permission to sisos3/Supermercado-La-Selecci-n-.git denied to Sneakyblop.
fatal: unable to access 'https://github.com/sisos3/Supermercado-La-Selecci-n-.git/': The requested URL returned error: 403

Constantemente nos saltaba que la cuenta secundaria de una compañera no había dado la autorización para subir al repositorio, esto nos hizo tener que cambiar de repositorio (aún así no se solucionó), y viendo algunos videos de ayuda todo lo que logramos es hacer más errores (imagen de prueba):
