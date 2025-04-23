"""
Módulo que implementa la interfaz de línea de comandos para el sistema de tareas.
"""
from typing import List
from src.models.task import Task
from src.services.task_service import TaskService


class TaskCLI:
    """Clase que implementa la interfaz de línea de comandos."""
    
    def __init__(self, service: TaskService = None):
        """
        Inicializa la interfaz CLI.
        
        Args:
            service: Servicio para manejar la lógica de negocio.
        """
        self.service = service or TaskService()
    
    def run(self) -> None:
        """Ejecuta la interfaz de línea de comandos."""
        print("\n¡Bienvenido al Sistema de Registro de Tareas!\n")
        
        while True:
            self._show_menu()
            option = input("\nSeleccione una opción (1-6): ")
            
            if option == "1":
                self._show_tasks()
            elif option == "2":
                self._add_task()
            elif option == "3":
                self._delete_task()
            elif option == "4":
                self._toggle_task_completion()
            elif option == "5":
                self._change_task_priority()
            elif option == "6":
                print("\n¡Gracias por usar el Sistema de Registro de Tareas!")
                break
            else:
                print("\nOpción no válida. Intente de nuevo.")
    
    def _show_menu(self) -> None:
        """Muestra el menú principal de la aplicación."""
        print("\n=== SISTEMA DE REGISTRO DE TAREAS ===")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Marcar tarea como completada/pendiente")
        print("5. Cambiar prioridad de una tarea")
        print("6. Salir")
    
    def _show_tasks(self) -> None:
        """Muestra el listado de tareas."""
        tasks = self.service.get_all_tasks()
        
        if not tasks:
            print("\nNo hay tareas registradas.")
            return
        
        print("\n=== LISTA DE TAREAS ===")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        print("=====================")
    
    def _add_task(self) -> None:
        """Agrega una nueva tarea."""
        description = input("\nIngrese la descripción de la nueva tarea: ")
        
        if not description:
            print("La descripción no puede estar vacía.")
            return
        
        print("\nSeleccione la prioridad:")
        print("1. Baja")
        print("2. Normal")
        print("3. Alta")
        
        priority_option = input("Opción (1-3, por defecto 2): ")
        
        priority = "normal"
        if priority_option == "1":
            priority = "low"
        elif priority_option == "3":
            priority = "high"
        
        try:
            task = self.service.add_task(description, priority)
            print(f"\nTarea '{description}' agregada correctamente con prioridad {priority}.")
        except ValueError as e:
            print(f"\nError: {str(e)}")
    
    def _delete_task(self) -> None:
        """Elimina una tarea existente."""
        tasks = self.service.get_all_tasks()
        
        if not tasks:
            print("\nNo hay tareas para eliminar.")
            return
        
        self._show_tasks()
        
        try:
            index = int(input("\nIngrese el número de la tarea a eliminar: ")) - 1
            task = self.service.delete_task(index)
            
            if task:
                print(f"\nTarea '{task.description}' eliminada correctamente.")
            else:
                print("\nNúmero de tarea inválido.")
        except ValueError:
            print("\nPor favor, ingrese un número válido.")
    
    def _toggle_task_completion(self) -> None:
        """Cambia el estado de completado de una tarea."""
        tasks = self.service.get_all_tasks()
        
        if not tasks:
            print("\nNo hay tareas para modificar.")
            return
        
        self._show_tasks()
        
        try:
            index = int(input("\nIngrese el número de la tarea a marcar/desmarcar: ")) - 1
            task = self.service.toggle_task_completion(index)
            
            if task:
                status = "completada" if task.completed else "pendiente"
                print(f"\nTarea '{task.description}' marcada como {status}.")
            else:
                print("\nNúmero de tarea inválido.")
        except ValueError:
            print("\nPor favor, ingrese un número válido.")
    
    def _change_task_priority(self) -> None:
        """Cambia la prioridad de una tarea."""
        tasks = self.service.get_all_tasks()
        
        if not tasks:
            print("\nNo hay tareas para modificar.")
            return
        
        self._show_tasks()
        
        try:
            index = int(input("\nIngrese el número de la tarea a modificar: ")) - 1
            
            if not (0 <= index < len(tasks)):
                print("\nNúmero de tarea inválido.")
                return
                
            print("\nSeleccione la nueva prioridad:")
            print("1. Baja")
            print("2. Normal")
            print("3. Alta")
            
            priority_option = input("Opción (1-3): ")
            
            priority = None
            if priority_option == "1":
                priority = "low"
            elif priority_option == "2":
                priority = "normal"
            elif priority_option == "3":
                priority = "high"
            else:
                print("\nOpción de prioridad inválida.")
                return
            
            task = self.service.update_task_priority(index, priority)
            
            if task:
                print(f"\nPrioridad de la tarea '{task.description}' actualizada a {priority}.")
            else:
                print("\nError al actualizar la prioridad.")
        except ValueError:
            print("\nPor favor, ingrese un número válido.")