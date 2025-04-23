# Sistema de Registro de Tareas

Proyecto de clase para demostrar operaciones de entrada/salida con archivos de texto plano.

## Funcionalidades

* Cargar tareas desde un archivo de texto
* Agregar nuevas tareas
* Mostrar listado de tareas en consola
* Guardar tareas en archivo

## Conceptos implementados

* Función `open()` y modos de apertura
* Escritura línea por línea con `.write()`
* Lectura con `.readlines()`
* Uso del bloque `with` para manejo automático de cierre
* Manejo de excepciones para casos como archivo no encontrado

## Ejecución

Para ejecutar el programa:
1. Abrir la terminal en la ruta del proyecto
2. Ejecutar el comando:

```
python task_registry.py
```

El programa creará un archivo "tasks.txt" en el mismo directorio cuando guarde las tareas. 