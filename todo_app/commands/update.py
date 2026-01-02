from typing import Dict, Any, Optional
from todo_app.store.todo_store import TodoStore


class UpdateCommand:
    """
    Command handler for updating todos.
    """

    def __init__(self, store: TodoStore):
        """
        Initialize the command with a store reference.

        Args:
            store: The todo store to update todos in
        """
        self.store = store

    def execute(self, todo_id: int, title: Optional[str] = None,
                description: Optional[str] = None, priority: Optional[str] = None) -> Dict[str, Any]:
        """
        Execute the update command to modify an existing todo.

        Args:
            todo_id: The ID of the todo to update
            title: New title (optional)
            description: New description (optional)
            priority: New priority (optional)

        Returns:
            Dictionary with result of the operation
        """
        # Validate inputs
        if not isinstance(todo_id, int) or todo_id <= 0:
            return {
                "success": False,
                "error": f"Todo ID must be a positive integer, got {todo_id}",
                "todo": None
            }

        # Validate title if provided
        if title is not None:
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

        # Validate description if provided
        if description is not None:
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

        # Validate priority if provided
        if priority is not None:
            if priority not in ["low", "medium", "high"]:
                return {
                    "success": False,
                    "error": f"Priority must be 'low', 'medium', or 'high', got '{priority}'",
                    "todo": None
                }

        try:
            # Prepare updates dictionary
            updates = {}
            if title is not None:
                updates['title'] = title.strip()
            if description is not None:
                updates['description'] = description.strip()
            if priority is not None:
                updates['priority'] = priority

            # If no updates were provided, return an error
            if not updates:
                return {
                    "success": False,
                    "error": "No updates provided",
                    "todo": None
                }

            # Update the todo in the store
            updated_todo = self.store.update(todo_id, updates)

            if updated_todo is None:
                return {
                    "success": False,
                    "error": f"Todo with ID {todo_id} not found",
                    "todo": None
                }

            return {
                "success": True,
                "error": None,
                "todo": updated_todo
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