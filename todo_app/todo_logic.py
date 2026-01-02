"""
Todo application business logic module.
Handles all core todo operations with in-memory storage.
"""

from typing import List, Dict, Optional
from datetime import datetime


class TodoItem:
    """Represents a single todo item."""

    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id}: {self.title} - {self.description}"

    def to_dict(self) -> Dict:
        """Convert todo item to dictionary representation."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class TodoManager:
    """Manages all todo operations with in-memory storage."""

    def __init__(self):
        self.todos: List[TodoItem] = []
        self.next_id = 1

    def add_todo(self, title: str, description: str = "") -> TodoItem:
        """
        Add a new todo item.

        Args:
            title: The title of the todo item
            description: Optional description of the todo item

        Returns:
            The created TodoItem
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        todo = TodoItem(
            id=self.next_id,
            title=title.strip(),
            description=description.strip()
        )
        self.todos.append(todo)
        self.next_id += 1
        return todo

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo item by ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was deleted, False if not found
        """
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                return True
        return False

    def update_todo(self, todo_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[TodoItem]:
        """
        Update a todo item by ID.

        Args:
            todo_id: The ID of the todo to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            The updated TodoItem if found, None if not found
        """
        for todo in self.todos:
            if todo.id == todo_id:
                if title is not None:
                    if not title.strip():
                        raise ValueError("Title cannot be empty")
                    todo.title = title.strip()
                if description is not None:
                    todo.description = description.strip()
                todo.updated_at = datetime.now()
                return todo
        return None

    def mark_complete(self, todo_id: int, completed: bool = True) -> bool:
        """
        Mark a todo item as complete or incomplete.

        Args:
            todo_id: The ID of the todo to update
            completed: Whether the todo is completed (default True)

        Returns:
            True if the todo was found and updated, False if not found
        """
        for todo in self.todos:
            if todo.id == todo_id:
                todo.completed = completed
                todo.updated_at = datetime.now()
                return True
        return False

    def get_todo(self, todo_id: int) -> Optional[TodoItem]:
        """
        Get a specific todo item by ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The TodoItem if found, None if not found
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def get_all_todos(self) -> List[TodoItem]:
        """
        Get all todo items.

        Returns:
            List of all TodoItems
        """
        return self.todos[:]

    def get_completed_todos(self) -> List[TodoItem]:
        """
        Get all completed todo items.

        Returns:
            List of completed TodoItems
        """
        return [todo for todo in self.todos if todo.completed]

    def get_pending_todos(self) -> List[TodoItem]:
        """
        Get all pending (not completed) todo items.

        Returns:
            List of pending TodoItems
        """
        return [todo for todo in self.todos if not todo.completed]

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new todo.

        Returns:
            The next available ID
        """
        return self.next_id