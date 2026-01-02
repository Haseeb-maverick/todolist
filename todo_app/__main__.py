"""
Main entry point for the Todo Application.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from todo_logic import TodoManager
from console_interface import TodoConsoleInterface


def main():
    """Initialize and run the todo application."""
    # Create the todo manager with in-memory storage
    todo_manager = TodoManager()

    # Create the console interface
    console_interface = TodoConsoleInterface(todo_manager)

    # Run the application
    console_interface.run()


if __name__ == "__main__":
    main()