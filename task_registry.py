"""
Sistema de Registro de Tareas
- Guardar tareas en archivo
- Agregar nuevas tareas
- Mostrar listado en consola
"""

def cargar_tareas():
    """Carga las tareas desde el archivo tasks.txt."""
    tareas = []
    try:
        with open("tasks.txt", "r") as archivo:
            tareas = [linea.strip() for linea in archivo.readlines()]
        print(f"Se cargaron {len(tareas)} tareas del archivo.")
    except FileNotFoundError:
        print("No se encontró archivo de tareas. Se creará uno nuevo.")
    return tareas

def guardar_tareas(tareas):
    """Guarda las tareas en el archivo tasks.txt."""
    with open("tasks.txt", "w") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")
    print(f"Se guardaron {len(tareas)} tareas en el archivo.")

def mostrar_tareas(tareas):
    """Muestra la lista de tareas en la consola."""
    if not tareas:
        print("No hay tareas registradas.")
        return
    
    print("\n=== LISTA DE TAREAS ===")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea}")
    print("=====================\n")

def agregar_tarea(tareas):
    """Agrega una nueva tarea a la lista."""
    nueva_tarea = input("Ingrese la descripción de la nueva tarea: ")
    if nueva_tarea:
        tareas.append(nueva_tarea)
        print(f"Tarea '{nueva_tarea}' agregada correctamente.")
    else:
        print("La tarea no puede estar vacía.")
    return tareas

def eliminar_tarea(tareas):
    """Elimina una tarea de la lista."""
    if not tareas:
        print("No hay tareas para eliminar.")
        return tareas
    
    mostrar_tareas(tareas)
    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada}' eliminada correctamente.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
    
    return tareas

def menu_principal():
    """Muestra el menú principal y gestiona las opciones."""
    tareas = cargar_tareas()
    
    while True:
        print("\n=== SISTEMA DE REGISTRO DE TAREAS ===")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Guardar y salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            tareas = agregar_tarea(tareas)
        elif opcion == "3":
            tareas = eliminar_tarea(tareas)
        elif opcion == "4":
            guardar_tareas(tareas)
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()