"""
Módulo que define el modelo de datos para una tarea.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """Clase que representa una tarea en el sistema."""
    
    description: str
    created_at: datetime = None
    completed: bool = False
    priority: str = "normal"  # "low", "normal", "high"
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
    
    @staticmethod
    def from_string(task_str: str) -> 'Task':
        """Crea una tarea a partir de una cadena de texto."""
        parts = task_str.split("|")
        if len(parts) >= 4:
            return Task(
                description=parts[0],
                created_at=datetime.fromisoformat(parts[1]) if parts[1] else datetime.now(),
                completed=parts[2].lower() == "true",
                priority=parts[3]
            )
        return Task(description=task_str)
    
    def to_string(self) -> str:
        """Convierte la tarea a una cadena de texto para su almacenamiento."""
        return f"{self.description}|{self.created_at.isoformat()}|{self.completed}|{self.priority}"
    
    def __str__(self) -> str:
        """Representación legible de la tarea."""
        status = "[✓]" if self.completed else "[ ]"
        priority_indicator = ""
        if self.priority == "high":
            priority_indicator = "🔴 "
        elif self.priority == "low":
            priority_indicator = "🔵 "
            
        return f"{status} {priority_indicator}{self.description}"