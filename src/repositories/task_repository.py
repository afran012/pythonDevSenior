"""
Módulo para manejar la persistencia de las tareas.
"""
import os
from typing import List
from src.models.task import Task


class TaskRepository:
    """Clase que maneja la persistencia de tareas."""
    
    def __init__(self, file_path: str = "data/tasks.txt"):
        """
        Inicializa el repositorio de tareas.
        
        Args:
            file_path: Ruta al archivo donde se guardan las tareas.
        """
        self.file_path = file_path
        # Asegurar que el directorio data existe
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    def load(self) -> List[Task]:
        """Carga las tareas desde el archivo."""
        tasks = []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        tasks.append(Task.from_string(line))
        except FileNotFoundError:
            # Si el archivo no existe, retornamos una lista vacía
            pass
        
        return tasks
    
    def save(self, tasks: List[Task]) -> None:
        """
        Guarda las tareas en el archivo.
        
        Args:
            tasks: Lista de tareas a guardar.
        """
        with open(self.file_path, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(f"{task.to_string()}\n")