"""
Servicio para manejar la lógica de negocio relacionada con las tareas.
"""
from typing import List, Optional
from src.models.task import Task
from src.repositories.task_repository import TaskRepository


class TaskService:
    """Clase que implementa la lógica de negocio para las tareas."""
    
    def __init__(self, repository: Optional[TaskRepository] = None):
        """
        Inicializa el servicio de tareas.
        
        Args:
            repository: Repositorio para acceder a los datos de tareas.
        """
        self.repository = repository or TaskRepository()
        self.tasks = self.repository.load()
    
    def get_all_tasks(self) -> List[Task]:
        """Obtiene todas las tareas."""
        return self.tasks
    
    def add_task(self, description: str, priority: str = "normal") -> Task:
        """
        Agrega una nueva tarea.
        
        Args:
            description: Descripción de la tarea.
            priority: Prioridad de la tarea ("low", "normal", "high").
        
        Returns:
            La tarea creada.
            
        Raises:
            ValueError: Si la descripción está vacía.
        """
        if not description:
            raise ValueError("La descripción de la tarea no puede estar vacía")
            
        if priority not in ["low", "normal", "high"]:
            priority = "normal"
            
        task = Task(description=description, priority=priority)
        self.tasks.append(task)
        self._save_tasks()
        return task
    
    def delete_task(self, index: int) -> Optional[Task]:
        """
        Elimina una tarea por su índice.
        
        Args:
            index: Índice de la tarea a eliminar (0-based).
            
        Returns:
            La tarea eliminada o None si el índice no es válido.
        """
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            self._save_tasks()
            return task
        return None
    
    def toggle_task_completion(self, index: int) -> Optional[Task]:
        """
        Cambia el estado de completado de una tarea.
        
        Args:
            index: Índice de la tarea a modificar (0-based).
            
        Returns:
            La tarea modificada o None si el índice no es válido.
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = not self.tasks[index].completed
            self._save_tasks()
            return self.tasks[index]
        return None
    
    def update_task_priority(self, index: int, priority: str) -> Optional[Task]:
        """
        Actualiza la prioridad de una tarea.
        
        Args:
            index: Índice de la tarea a modificar (0-based).
            priority: Nueva prioridad ("low", "normal", "high").
            
        Returns:
            La tarea modificada o None si el índice no es válido.
        """
        if 0 <= index < len(self.tasks) and priority in ["low", "normal", "high"]:
            self.tasks[index].priority = priority
            self._save_tasks()
            return self.tasks[index]
        return None
    
    def _save_tasks(self) -> None:
        """Guarda las tareas utilizando el repositorio."""
        self.repository.save(self.tasks)