from typing import Dict, Any
from todo_app.domain.todo import Todo


class AddCommand:
    """
    Command handler for adding new todos.
    """

    def __init__(self, store):
        """
        Initialize the command with a store reference.

        Args:
            store: The todo store to add todos to
        """
        self.store = store

    def execute(self, title: str, description: str, priority: str = "medium") -> Dict[str, Any]:
        """
        Execute the add command to create a new todo.

        Args:
            title: The title of the new todo
            description: The description of the new todo
            priority: The priority of the new todo (optional, defaults to "medium")

        Returns:
            Dictionary with result of the operation
        """
        # Validate inputs according to data model requirements
        if not title or not title.strip():
            return {
                "success": False,
                "error": "Title cannot be empty",
                "todo": None
            }

        if len(title) > 200:
            return {
                "success": False,
                "error": f"Title must be 200 characters or less, got {len(title)}",
                "todo": None
            }

        if not description or not description.strip():
            return {
                "success": False,
                "error": "Description cannot be empty",
                "todo": None
            }

        if len(description) > 1000:
            return {
                "success": False,
                "error": f"Description must be 1000 characters or less, got {len(description)}",
                "todo": None
            }

        if priority not in ["low", "medium", "high"]:
            return {
                "success": False,
                "error": f"Priority must be 'low', 'medium', or 'high', got '{priority}'",
                "todo": None
            }

        try:
            # Create a new todo with the next available ID
            # We'll let the store handle ID assignment
            todo = Todo(
                id=None,  # Will be assigned by the store
                title=title.strip(),
                description=description.strip(),
                priority=priority
            )

            # Add the todo to the store
            added_todo = self.store.add(todo)

            return {
                "success": True,
                "error": None,
                "todo": added_todo
            }
        except ValueError as e:
            return {
                "success": False,
                "error": f"Validation error: {str(e)}",
                "todo": None
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Unexpected error occurred: {str(e)}",
                "todo": None
            }