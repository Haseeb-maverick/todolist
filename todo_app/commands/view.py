from typing import Dict, Any, List
from todo_app.store.todo_store import TodoStore
from todo_app.domain.todo import Todo


class ViewCommand:
    """
    Command handler for viewing todos.
    """

    def __init__(self, store: TodoStore):
        """
        Initialize the command with a store reference.

        Args:
            store: The todo store to view todos from
        """
        self.store = store

    def execute(self, view_type: str = "all") -> Dict[str, Any]:
        """
        Execute the view command to retrieve todos based on the view type.

        Args:
            view_type: Type of view ("all", "completed", "incomplete")

        Returns:
            Dictionary with result of the operation
        """
        # Validate view_type
        if view_type not in ["all", "completed", "incomplete"]:
            return {
                "success": False,
                "error": f"View type must be 'all', 'completed', or 'incomplete', got '{view_type}'",
                "todos": []
            }

        try:
            if view_type == "all":
                todos = self.store.list_all()
            elif view_type == "completed":
                todos = self.store.list_by_status("complete")
            elif view_type == "incomplete":
                todos = self.store.list_by_status("incomplete")

            return {
                "success": True,
                "error": None,
                "todos": todos,
                "view_type": view_type
            }
        except ValueError as e:
            return {
                "success": False,
                "error": f"Validation error: {str(e)}",
                "todos": []
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Unexpected error occurred: {str(e)}",
                "todos": []
            }

    def get_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about todos in the store.

        Returns:
            Dictionary with statistics about todos
        """
        try:
            all_todos = self.store.list_all()
            completed_todos = self.store.list_by_status("complete")
            incomplete_todos = self.store.list_by_status("incomplete")

            # Count by priority
            priority_counts = {"low": 0, "medium": 0, "high": 0}
            for todo in all_todos:
                priority_counts[todo.priority] += 1

            return {
                "success": True,
                "error": None,
                "total": len(all_todos),
                "completed": len(completed_todos),
                "incomplete": len(incomplete_todos),
                "priorities": priority_counts
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Error getting statistics: {str(e)}",
                "total": 0,
                "completed": 0,
                "incomplete": 0,
                "priorities": {"low": 0, "medium": 0, "high": 0}
            }