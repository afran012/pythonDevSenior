"""
Punto de entrada principal para el Sistema de Registro de Tareas.
"""
from src.ui.cli import TaskCLI


def main():
    """Función principal que inicia la aplicación."""
    cli = TaskCLI()
    cli.run()


if __name__ == "__main__":
    main()