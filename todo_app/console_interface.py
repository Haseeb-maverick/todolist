"""
Todo application console interface module.
Handles user input and output operations.
"""

from todo_logic import TodoManager, TodoItem
from typing import Optional


class TodoConsoleInterface:
    """Handles console input/output for the todo application."""

    def __init__(self, todo_manager: TodoManager):
        self.todo_manager = todo_manager

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*50)
        print("TODO APPLICATION")
        print("="*50)
        print("1. Add Todo")
        print("2. View All Todos")
        print("3. View Pending Todos")
        print("4. View Completed Todos")
        print("5. Update Todo")
        print("6. Mark Todo Complete")
        print("7. Mark Todo Incomplete")
        print("8. Delete Todo")
        print("9. Exit")
        print("-"*50)

    def get_user_choice(self) -> str:
        """
        Get user's menu choice.

        Returns:
            User's choice as a string
        """
        return input("Enter your choice (1-9): ").strip()

    def add_todo(self):
        """Handle adding a new todo."""
        print("\n--- ADD TODO ---")
        title = input("Enter todo title: ").strip()

        if not title:
            print("Error: Title cannot be empty!")
            return

        description = input("Enter todo description (optional): ").strip()

        try:
            todo = self.todo_manager.add_todo(title, description)
            print(f"Successfully added todo: {todo}")
        except ValueError as e:
            print(f"Error: {e}")

    def view_todos(self, todos: list, title: str):
        """
        Display a list of todos.

        Args:
            todos: List of TodoItems to display
            title: Title for the section being displayed
        """
        print(f"\n--- {title} ---")
        if not todos:
            print("No todos found.")
            return

        for todo in todos:
            print(todo)

    def view_all_todos(self):
        """Display all todos."""
        todos = self.todo_manager.get_all_todos()
        self.view_todos(todos, "ALL TODOS")

    def view_pending_todos(self):
        """Display pending todos."""
        todos = self.todo_manager.get_pending_todos()
        self.view_todos(todos, "PENDING TODOS")

    def view_completed_todos(self):
        """Display completed todos."""
        todos = self.todo_manager.get_completed_todos()
        self.view_todos(todos, "COMPLETED TODOS")

    def update_todo(self):
        """Handle updating a todo."""
        print("\n--- UPDATE TODO ---")

        if not self.todo_manager.get_all_todos():
            print("No todos available to update.")
            return

        try:
            todo_id = int(input("Enter todo ID to update: "))
        except ValueError:
            print("Error: Please enter a valid number for the ID.")
            return

        existing_todo = self.todo_manager.get_todo(todo_id)
        if not existing_todo:
            print(f"Error: Todo with ID {todo_id} not found.")
            return

        print(f"Current todo: {existing_todo}")

        new_title = input(f"Enter new title (current: '{existing_todo.title}'): ").strip()
        new_description = input(f"Enter new description (current: '{existing_todo.description}'): ").strip()

        # Use existing values if new values are empty
        title = new_title if new_title else existing_todo.title
        description = new_description if new_description else existing_todo.description

        try:
            updated_todo = self.todo_manager.update_todo(todo_id, title, description)
            if updated_todo:
                print(f"Successfully updated todo: {updated_todo}")
            else:
                print(f"Error: Failed to update todo with ID {todo_id}")
        except ValueError as e:
            print(f"Error: {e}")

    def mark_todo_complete(self, completed: bool = True):
        """
        Handle marking a todo as complete or incomplete.

        Args:
            completed: Whether to mark as complete (True) or incomplete (False)
        """
        status = "complete" if completed else "incomplete"
        print(f"\n--- MARK TODO {status.upper()} ---")

        if not self.todo_manager.get_all_todos():
            print("No todos available.")
            return

        try:
            todo_id = int(input(f"Enter todo ID to mark as {status}: "))
        except ValueError:
            print("Error: Please enter a valid number for the ID.")
            return

        success = self.todo_manager.mark_complete(todo_id, completed)
        if success:
            action = "completed" if completed else "incomplete"
            print(f"Successfully marked todo with ID {todo_id} as {action}.")
        else:
            print(f"Error: Todo with ID {todo_id} not found.")

    def delete_todo(self):
        """Handle deleting a todo."""
        print("\n--- DELETE TODO ---")

        if not self.todo_manager.get_all_todos():
            print("No todos available to delete.")
            return

        try:
            todo_id = int(input("Enter todo ID to delete: "))
        except ValueError:
            print("Error: Please enter a valid number for the ID.")
            return

        success = self.todo_manager.delete_todo(todo_id)
        if success:
            print(f"Successfully deleted todo with ID {todo_id}.")
        else:
            print(f"Error: Todo with ID {todo_id} not found.")

    def run(self):
        """Run the main application loop."""
        print("Welcome to the Todo Application!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.add_todo()
            elif choice == "2":
                self.view_all_todos()
            elif choice == "3":
                self.view_pending_todos()
            elif choice == "4":
                self.view_completed_todos()
            elif choice == "5":
                self.update_todo()
            elif choice == "6":
                self.mark_todo_complete(completed=True)
            elif choice == "7":
                self.mark_todo_complete(completed=False)
            elif choice == "8":
                self.delete_todo()
            elif choice == "9":
                print("Thank you for using the Todo Application!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")

            input("\nPress Enter to continue...")