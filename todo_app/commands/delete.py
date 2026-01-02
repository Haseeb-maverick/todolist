from typing import Dict, Any
from todo_app.store.todo_store import TodoStore


class DeleteCommand:
    """
    Command handler for deleting todos.
    """

    def __init__(self, store: TodoStore):
        """
        Initialize the command with a store reference.

        Args:
            store: The todo store to delete todos from
        """
        self.store = store

    def execute(self, todo_id: int, confirmed: bool = False) -> Dict[str, Any]:
        """
        Execute the delete command to remove an existing todo.

        Args:
            todo_id: The ID of the todo to delete
            confirmed: Whether the user has confirmed the deletion (for safety)

        Returns:
            Dictionary with result of the operation
        """
        # Validate inputs
        if not isinstance(todo_id, int) or todo_id <= 0:
            return {
                "success": False,
                "error": f"Todo ID must be a positive integer, got {todo_id}",
                "deleted": False
            }

        if not confirmed:
            return {
                "success": False,
                "error": "Deletion must be confirmed",
                "deleted": False
            }

        try:
            # Delete the todo from the store
            deleted = self.store.delete(todo_id)

            if not deleted:
                return {
                    "success": False,
                    "error": f"Todo with ID {todo_id} not found",
                    "deleted": False
                }

            return {
                "success": True,
                "error": None,
                "deleted": True
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Unexpected error occurred: {str(e)}",
                "deleted": False
            }