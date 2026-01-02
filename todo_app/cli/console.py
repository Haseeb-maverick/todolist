from typing import Optional
from todo_app.commands.add import AddCommand
from todo_app.commands.view import ViewCommand
from todo_app.commands.update import UpdateCommand
from todo_app.commands.complete import CompleteCommand
from todo_app.commands.delete import DeleteCommand
from todo_app.store.todo_store import TodoStore


class TodoConsoleInterface:
    """
    Console interface for the todo application.
    """

    def __init__(self, store: TodoStore):
        """
        Initialize the console interface with a todo store.

        Args:
            store: The todo store to interact with
        """
        self.store = store
        self.add_command = AddCommand(store)
        self.view_command = ViewCommand(store)
        self.update_command = UpdateCommand(store)
        self.complete_command = CompleteCommand(store)
        self.delete_command = DeleteCommand(store)

    def run(self):
        """
        Start the main application loop.
        """
        print("Welcome to the Todo Application!")
        print("Type 'help' for available commands or 'exit' to quit.")

        while True:
            command = input("\nEnter command: ").strip().lower()

            if command == 'exit':
                print("Goodbye!")
                break
            elif command == 'help':
                self.show_help()
            elif command == 'add':
                self.handle_add()
            elif command == 'view':
                self.handle_view()
            elif command == 'update':
                self.handle_update()
            elif command == 'complete':
                self.handle_complete()
            elif command == 'delete':
                self.handle_delete()
            else:
                print(f"Unknown command: {command}")
                print("Type 'help' for available commands.")

    def show_help(self):
        """
        Display help information for available commands.
        """
        print("\nAvailable commands:")
        print("  add      - Add a new todo")
        print("  view     - View todos (all, completed, incomplete)")
        print("  update   - Update an existing todo")
        print("  complete - Mark a todo as complete/incomplete")
        print("  delete   - Delete a todo")
        print("  exit     - Exit the application")
        print("  help     - Show this help message")

    def handle_add(self):
        """
        Handle the add command by prompting user for input.
        """
        print("\nAdding a new todo...")

        title = input("Enter title: ").strip()
        if not title:
            print("Error: Title cannot be empty")
            return

        description = input("Enter description: ").strip()
        if not description:
            print("Error: Description cannot be empty")
            return

        priority_input = input("Enter priority (low/medium/high, default: medium): ").strip().lower()
        priority = priority_input if priority_input in ["low", "high"] else "medium"

        # Execute the add command
        result = self.add_command.execute(title, description, priority)

        if result["success"]:
            todo = result["todo"]
            print(f"Successfully added todo with ID: {todo.id}")
            print(f"Title: {todo.title}")
            print(f"Description: {todo.description}")
            print(f"Priority: {todo.priority}")
        else:
            print(f"Error: {result['error']}")

    def handle_view(self):
        """
        Handle the view command by prompting user for view type.
        """
        print("\nViewing todos...")
        view_type = input("Enter view type (all/completed/incomplete, default: all): ").strip().lower()

        if view_type not in ["all", "completed", "incomplete"]:
            if view_type == "":
                view_type = "all"
            else:
                print(f"Error: Invalid view type '{view_type}'. Using 'all' instead.")
                view_type = "all"

        # Execute the view command
        result = self.view_command.execute(view_type)

        if result["success"]:
            todos = result["todos"]
            if todos:
                print(f"\n{len(todos)} todo(s) found:")
                for todo in todos:
                    status_symbol = "✓" if todo.status == "complete" else "○"
                    print(f"  {status_symbol} [{todo.id}] {todo.title} ({todo.priority})")
                    print(f"      {todo.description}")
                    if todo.created_at:
                        print(f"      Created: {todo.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
                    if todo.updated_at and todo.updated_at != todo.created_at:
                        print(f"      Updated: {todo.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
                    print()
            else:
                print(f"No {view_type} todos found.")
        else:
            print(f"Error: {result['error']}")

    def handle_update(self):
        """
        Handle the update command by prompting user for input.
        """
        print("\nUpdating a todo...")

        try:
            todo_id_input = input("Enter todo ID: ").strip()
            todo_id = int(todo_id_input)
        except ValueError:
            print(f"Error: Todo ID must be a number, got '{todo_id_input}'")
            return

        # Get current todo to show existing values
        current_todo = self.store.get(todo_id)
        if current_todo is None:
            print(f"Error: Todo with ID {todo_id} not found")
            return

        print(f"Current values for todo {todo_id}:")
        print(f"  Title: {current_todo.title}")
        print(f"  Description: {current_todo.description}")
        print(f"  Priority: {current_todo.priority}")

        title = input(f"Enter new title (leave blank to keep '{current_todo.title}'): ").strip()
        title = title if title else None

        description = input(f"Enter new description (leave blank to keep current): ").strip()
        description = description if description else None

        priority_input = input(f"Enter new priority (low/medium/high, leave blank to keep '{current_todo.priority}'): ").strip().lower()
        priority = priority_input if priority_input in ["low", "medium", "high"] else None

        # Execute the update command
        result = self.update_command.execute(todo_id, title, description, priority)

        if result["success"]:
            todo = result["todo"]
            print(f"Successfully updated todo with ID: {todo.id}")
            print(f"Title: {todo.title}")
            print(f"Description: {todo.description}")
            print(f"Priority: {todo.priority}")
        else:
            print(f"Error: {result['error']}")

    def handle_complete(self):
        """
        Handle the complete command by prompting user for input.
        """
        print("\nMarking a todo as complete/incomplete...")

        try:
            todo_id_input = input("Enter todo ID: ").strip()
            todo_id = int(todo_id_input)
        except ValueError:
            print(f"Error: Todo ID must be a number, got '{todo_id_input}'")
            return

        # Get current todo to show existing status
        current_todo = self.store.get(todo_id)
        if current_todo is None:
            print(f"Error: Todo with ID {todo_id} not found")
            return

        print(f"Current status for todo {todo_id}: {current_todo.status}")

        status_input = input(f"Enter new status (complete/incomplete, default: complete): ").strip().lower()
        if status_input == "":
            status_input = "complete"
        elif status_input not in ["complete", "incomplete"]:
            print(f"Error: Invalid status '{status_input}'. Using 'complete' instead.")
            status_input = "complete"

        # Execute the complete command
        result = self.complete_command.execute(todo_id, status_input)

        if result["success"]:
            todo = result["todo"]
            print(f"Successfully updated todo with ID: {todo.id}")
            print(f"Status: {todo.status}")
        else:
            print(f"Error: {result['error']}")

    def handle_delete(self):
        """
        Handle the delete command by prompting user for input and confirmation.
        """
        print("\nDeleting a todo...")

        try:
            todo_id_input = input("Enter todo ID: ").strip()
            todo_id = int(todo_id_input)
        except ValueError:
            print(f"Error: Todo ID must be a number, got '{todo_id_input}'")
            return

        # Get current todo to show details before deletion
        current_todo = self.store.get(todo_id)
        if current_todo is None:
            print(f"Error: Todo with ID {todo_id} not found")
            return

        print(f"Todo to delete: [{todo_id}] {current_todo.title}")
        print(f"  Description: {current_todo.description}")
        print(f"  Status: {current_todo.status}")
        print(f"  Priority: {current_todo.priority}")

        # Ask for confirmation
        confirm = input(f"\nAre you sure you want to delete todo {todo_id}? (yes/no): ").strip().lower()
        if confirm not in ['yes', 'y']:
            print("Deletion cancelled.")
            return

        # Execute the delete command
        result = self.delete_command.execute(todo_id, confirmed=True)

        if result["success"]:
            print(f"Successfully deleted todo with ID: {todo_id}")
        else:
            print(f"Error: {result['error']}")