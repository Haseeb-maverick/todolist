from typing import Dict, Any
from todo_app.store.todo_store import TodoStore


class CompleteCommand:
    """
    Command handler for marking todos as complete or incomplete.
    """

    def __init__(self, store: TodoStore):
        """
        Initialize the command with a store reference.

        Args:
            store: The todo store to update todos in
        """
        self.store = store

    def execute(self, todo_id: int, status: str = "complete") -> Dict[str, Any]:
        """
        Execute the complete/incomplete command to update a todo's status.

        Args:
            todo_id: The ID of the todo to update
            status: The status to set ("complete" or "incomplete")

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

        if status not in ["complete", "incomplete"]:
            return {
                "success": False,
                "error": f"Status must be 'complete' or 'incomplete', got '{status}'",
                "todo": None
            }

        try:
            # Update the todo status in the store
            if status == "complete":
                updated_todo = self.store.mark_complete(todo_id)
            else:
                updated_todo = self.store.mark_incomplete(todo_id)

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