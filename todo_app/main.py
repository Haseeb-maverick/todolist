#!/usr/bin/env python3
"""
Main entry point for the todo application.
"""

from todo_app.store.todo_store import TodoStore


def main():
    """
    Main application function that initializes the todo store and starts the CLI.
    """
    print("Initializing Todo Application...")

    # Initialize the todo store
    store = TodoStore()

    # For now, just show that the store is working
    print("Todo store initialized successfully!")
    print(f"Current todo count: {len(store.list_all())}")

    # In the future, this will start the CLI interface
    print("Starting CLI interface...")

    # Import and start the CLI
    from todo_app.cli.console import TodoConsoleInterface
    interface = TodoConsoleInterface(store)
    interface.run()


if __name__ == "__main__":
    main()