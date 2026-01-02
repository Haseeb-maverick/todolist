from typing import List, Optional, Dict
from todo_app.domain.todo import Todo


class TodoStore:
    """
    In-memory storage for todos with CRUD operations and status management.
    """

    def __init__(self):
        """Initialize the store with empty collections."""
        self._todos_by_id: Dict[int, Todo] = {}
        self._all_todos: List[Todo] = []
        self._next_id = 1

    def add(self, todo: Todo) -> Todo:
        """
        Add a new todo to the store, assigning a unique ID if not already assigned.

        Args:
            todo: The todo to add

        Returns:
            The added todo with assigned ID
        """
        # If the todo doesn't have an ID, assign the next available one
        if todo.id is None or todo.id <= 0:
            todo.id = self._next_id
            self._next_id += 1
        elif todo.id >= self._next_id:
            # If a higher ID was provided, update the next ID to avoid conflicts
            self._next_id = todo.id + 1

        # Check if a todo with this ID already exists
        if todo.id in self._todos_by_id:
            raise ValueError(f"Todo with ID {todo.id} already exists")

        # Add the todo to both collections
        self._todos_by_id[todo.id] = todo
        self._all_todos.append(todo)

        return todo

    def get(self, todo_id: int) -> Optional[Todo]:
        """
        Retrieve a todo by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The todo with the given ID, or None if not found
        """
        return self._todos_by_id.get(todo_id)

    def update(self, todo_id: int, updates: Dict) -> Optional[Todo]:
        """
        Update a todo's attributes.

        Args:
            todo_id: The ID of the todo to update
            updates: Dictionary of attributes to update

        Returns:
            The updated todo, or None if not found
        """
        todo = self.get(todo_id)
        if todo is None:
            return None

        # Validate updates before applying them
        if 'title' in updates:
            todo.title = updates['title']
        if 'description' in updates:
            todo.description = updates['description']
        if 'status' in updates:
            if updates['status'] not in ['incomplete', 'complete']:
                raise ValueError(f"Status must be 'incomplete' or 'complete', got {updates['status']}")
            todo.status = updates['status']
        if 'priority' in updates:
            if updates['priority'] not in ['low', 'medium', 'high']:
                raise ValueError(f"Priority must be 'low', 'medium', or 'high', got {updates['priority']}")
            todo.priority = updates['priority']

        return todo

    def delete(self, todo_id: int) -> bool:
        """
        Remove a todo from the store.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was deleted, False if not found
        """
        if todo_id not in self._todos_by_id:
            return False

        todo = self._todos_by_id[todo_id]
        del self._todos_by_id[todo_id]
        self._all_todos.remove(todo)
        return True

    def list_all(self) -> List[Todo]:
        """
        Return all todos.

        Returns:
            List of all todos in the store
        """
        return self._all_todos.copy()  # Return a copy to prevent external modification

    def list_by_status(self, status: str) -> List[Todo]:
        """
        Return todos with a specific status.

        Args:
            status: The status to filter by ('incomplete' or 'complete')

        Returns:
            List of todos with the specified status
        """
        if status not in ['incomplete', 'complete']:
            raise ValueError(f"Status must be 'incomplete' or 'complete', got {status}")

        return [todo for todo in self._all_todos if todo.status == status]

    def mark_complete(self, todo_id: int) -> Optional[Todo]:
        """
        Mark a todo as complete.

        Args:
            todo_id: The ID of the todo to mark complete

        Returns:
            The updated todo, or None if not found
        """
        todo = self.get(todo_id)
        if todo is None:
            return None

        todo.mark_complete()
        return todo

    def mark_incomplete(self, todo_id: int) -> Optional[Todo]:
        """
        Mark a todo as incomplete.

        Args:
            todo_id: The ID of the todo to mark incomplete

        Returns:
            The updated todo, or None if not found
        """
        todo = self.get(todo_id)
        if todo is None:
            return None

        todo.mark_incomplete()
        return todo