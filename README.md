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
"C:\Users\Mari\Documents\python supermercado 2026> git push --set-upstream origin master
remote: Permission to sisos3/Supermercado-La-Selecci-n-.git denied to Sneakyblop.
fatal: unable to access 'https://github.com/sisos3/Supermercado-La-Selecci-n-.git/': The requested URL returned error: 403"

Constantemente nos saltaba que la cuenta secundaria de una compañera no nos había dado la autorización para subir al repositorio, esto nos hizo tener que cambiar de repositorio 2 veces (aún así no se solucionó), y viendo algunos videos de ayuda todo lo que logramos es hacer más errores (imagen de prueba):
  ![image alt](https://github.com/Sneakyblop/Supermercado-La-Selecci-n-/blob/master/Captura%20de%20pantalla%202026-07-08%20012732.png?raw=true)

  Entonces decidimos usar a la IA como una herramienta de ayuda, más no como una de fin, la IA usada fue "COPILOT" y le decíamos qué comentarios poner y subir, tal cual estuviera el código en ese momento sin modificar nada, ni pidiendo mejoras. Esto la verdad nor ahorró muchísimo tiempo.
  
  * Al finalizar el código decidimos preguntarle a GEMINI qué pensaba de nuestro código, y le enviamos el siguiente PROMP:
  ## Actúa como un desarrollador senior de Python especializado en programación estructurada y algoritmos. Quiero que me ayudes a desarrollar y mejorar un proyecto ya existente, no a rehacerlo desde cero.
**Contexto del proyecto:**
Es un programa en Python que se ejecuta exclusivamente desde la consola.
No debe utilizar ninguna interfaz gráfica (Tkinter, PyQt, etc.).
El objetivo es simular el funcionamiento básico de una caja de supermercado.
El sistema puede incluir las siguientes funcionalidades:
•Carga y administración de productos.
•Venta de productos.
•Cálculo de subtotales y total de la compra.
•Aplicación de descuentos y promociones.
•Generación de un ticket de compra en formato texto.
•Estadísticas de ventas.
•Productos más vendidos.
•Cualquier otra mejora que sea coherente con el escenario de una caja de supermercado.
•Es muy importante que:

No cambies la estructura general del programa sin que yo lo pida.
No reescribas funciones que ya existen si no es necesario.
Respeta los nombres de variables y funciones siempre que sea posible.
Si necesitás modificar código existente, indicá exactamente qué líneas o qué función debo reemplazar.
Si agregás una funcionalidad nueva, indicá claramente dónde colocar el código.
Explicá brevemente por qué hacés cada cambio.
Si detectás errores, señalalos antes de proponer una solución.
Si una funcionalidad puede implementarse de varias formas, proponé la opción más simple y mantenible.
A partir de ahora te iré enviando partes de mi código y te indicaré qué funcionalidad quiero agregar o modificar. Antes de escribir código, analizá cómo está organizado el programa para mantener la coherencia con el proyecto existente.

* En resumen GEMINI nos respondió diciendo que el código estaba muy bien implementado, pero que agregaría más tipos de pago en la opción de tarjeta de crédito (distintos tipos de bancos con sus propias promociones), también nos sugirió agregar de alguna manera una base de datos para el gerente, porque al ingresar como gerente y querer ver la opción 3 del menú (estadísticas) queda como una opción "inútil", porque esas estadísticas únicamente se darán cuando el usuario realiza la compra.
Con todo esto le dimos la razon en algunos puntos (la parte de medio de pago nos pareció innecesaria), la parte del gerente nos hizo darnos cuenta de ese error que no habíamos visto, pero, primeramente decidimos dejarlo como constancia de que nuestro código tiene sus errores no previstos por el grupo, y además hacer uan base de datos para esas estadísticas se nos hacía imposible y no creíamos que estuviera alineado a este laboratorio.
Por lo cual, finalizando, decidimos dejar el código de la forma en que el grupo lo planteó, podemos tener errores y alguna cuestiones mejorables pero si seguíamos los consejos de la IA sería un producto mucho más complejo para el nivel que tenemos y no nos parecía correcto. 

* A COPILOT le preguntamos muy por encima si veía algún error grande en el código y nos respondío lo siguiente:
## Puntos concretos que vi en tu código
Hay una mezcla entre “subtotal”, “descuento” y “total final” que puede generar confusión al leer el resultado.
El resumen final podría quedar menos claro si el número de productos se muestra como decimal en todos los casos.

En resumen tu código está bastante bien estructurado para un laboratorio, pero los errores más frecuentes que suelen aparecer aquí son:
• entradas incorrectas,
• cálculos de descuentos mal aplicados,
• confusión entre cantidades y pesos,
• y problemas de consistencia al mostrar resultados.

Eso fue todo el uso que hicimos de la IA.
Desde ya muchas gracias por su atención, grupo 20, AED 2026, COM "C".
  
