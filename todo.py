"""
Core Todo Application Logic
Phase I: In-Memory Console Application
Following the constitution principles for simplicity, clear separation of concerns,
and production-grade practices.
"""

from typing import List, Optional, Dict, Any
from dataclasses import dataclass, asdict
from datetime import datetime
import uuid


@dataclass
class Todo:
    """
    Represents a todo item with required and optional attributes.
    Following the constitution's requirement for explicit state management.
    """
    id: str  # Using UUID string for better uniqueness
    title: str
    description: str
    status: str  # 'incomplete' or 'complete'
    priority: str  # 'low', 'medium', 'high'
    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        """Validate the todo after initialization."""
        self.validate()

    def validate(self):
        """Validate the todo attributes according to business rules."""
        # Validate id
        if not isinstance(self.id, str) or not self.id.strip():
            raise ValueError(f"ID must be a non-empty string, got {self.id}")

        # Validate title
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError(f"Title must be a non-empty string, got {self.title}")
        if len(self.title) < 1 or len(self.title) > 200:
            raise ValueError(f"Title must be 1-200 characters, got {len(self.title)} characters")

        # Validate description
        if not isinstance(self.description, str):
            raise ValueError(f"Description must be a string, got {self.description}")
        if len(self.description) > 1000:
            raise ValueError(f"Description must be under 1000 characters, got {len(self.description)} characters")

        # Validate status
        if self.status not in ["incomplete", "complete"]:
            raise ValueError(f"Status must be 'incomplete' or 'complete', got {self.status}")

        # Validate priority
        if self.priority not in ["low", "medium", "high"]:
            raise ValueError(f"Priority must be 'low', 'medium', or 'high', got {self.priority}")

    def mark_complete(self):
        """Mark the todo as complete."""
        self.status = "complete"
        self.updated_at = datetime.now()

    def mark_incomplete(self):
        """Mark the todo as incomplete."""
        self.status = "incomplete"
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """Convert todo to dictionary representation."""
        result = asdict(self)
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result


class TodoService:
    """
    Core business logic for todo operations.
    Following the constitution's principle of clear separation of concerns.
    All data stored in memory with no external persistence.
    """

    def __init__(self):
        """Initialize the todo service with empty storage."""
        self._todos: Dict[str, Todo] = {}

    def add_todo(self, title: str, description: str = "", priority: str = "medium") -> Todo:
        """
        Add a new todo item.

        Args:
            title: The title of the todo item (required)
            description: The description of the todo item (optional, defaults to empty string)
            priority: The priority level (optional, defaults to 'medium')

        Returns:
            The created Todo object

        Raises:
            ValueError: If title is invalid or other parameters don't meet requirements
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        # Generate a unique ID
        todo_id = str(uuid.uuid4())

        # Create the new todo
        new_todo = Todo(
            id=todo_id,
            title=title.strip(),
            description=description.strip(),
            status="incomplete",
            priority=priority,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        # Store the todo
        self._todos[todo_id] = new_todo

        return new_todo

    def get_todo(self, todo_id: str) -> Optional[Todo]:
        """
        Retrieve a specific todo by ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The Todo object if found, None otherwise
        """
        return self._todos.get(todo_id)

    def get_all_todos(self) -> List[Todo]:
        """
        Retrieve all todos.

        Returns:
            List of all Todo objects
        """
        return list(self._todos.values())

    def get_todos_by_status(self, status: str) -> List[Todo]:
        """
        Retrieve todos filtered by status.

        Args:
            status: The status to filter by ('incomplete' or 'complete')

        Returns:
            List of Todo objects with the specified status
        """
        if status not in ["incomplete", "complete"]:
            raise ValueError(f"Status must be 'incomplete' or 'complete', got {status}")

        return [todo for todo in self._todos.values() if todo.status == status]

    def get_todos_by_priority(self, priority: str) -> List[Todo]:
        """
        Retrieve todos filtered by priority.

        Args:
            priority: The priority to filter by ('low', 'medium', 'high')

        Returns:
            List of Todo objects with the specified priority
        """
        if priority not in ["low", "medium", "high"]:
            raise ValueError(f"Priority must be 'low', 'medium', or 'high', got {priority}")

        return [todo for todo in self._todos.values() if todo.priority == priority]

    def update_todo(self, todo_id: str, title: Optional[str] = None,
                   description: Optional[str] = None, priority: Optional[str] = None) -> Optional[Todo]:
        """
        Update an existing todo.

        Args:
            todo_id: The ID of the todo to update
            title: New title (optional)
            description: New description (optional)
            priority: New priority (optional)

        Returns:
            The updated Todo object if found, None if not found

        Raises:
            ValueError: If provided parameters don't meet requirements
        """
        todo = self._todos.get(todo_id)
        if not todo:
            return None

        # Validate and update fields if provided
        if title is not None:
            if not title.strip():
                raise ValueError("Title cannot be empty")
            if len(title) < 1 or len(title) > 200:
                raise ValueError(f"Title must be 1-200 characters, got {len(title)} characters")
            todo.title = title.strip()

        if description is not None:
            if len(description) > 1000:
                raise ValueError(f"Description must be under 1000 characters, got {len(description)} characters")
            todo.description = description.strip()

        if priority is not None:
            if priority not in ["low", "medium", "high"]:
                raise ValueError(f"Priority must be 'low', 'medium', or 'high', got {priority}")
            todo.priority = priority

        # Update timestamp
        todo.updated_at = datetime.now()

        return todo

    def mark_todo_complete(self, todo_id: str) -> bool:
        """
        Mark a todo as complete.

        Args:
            todo_id: The ID of the todo to mark complete

        Returns:
            True if the todo was found and updated, False otherwise
        """
        todo = self._todos.get(todo_id)
        if not todo:
            return False

        todo.mark_complete()
        return True

    def mark_todo_incomplete(self, todo_id: str) -> bool:
        """
        Mark a todo as incomplete.

        Args:
            todo_id: The ID of the todo to mark incomplete

        Returns:
            True if the todo was found and updated, False otherwise
        """
        todo = self._todos.get(todo_id)
        if not todo:
            return False

        todo.mark_incomplete()
        return True

    def delete_todo(self, todo_id: str) -> bool:
        """
        Delete a todo by ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was found and deleted, False otherwise
        """
        if todo_id in self._todos:
            del self._todos[todo_id]
            return True
        return False

    def clear_all_todos(self):
        """
        Clear all todos from memory.
        """
        self._todos.clear()

    def get_stats(self) -> Dict[str, int]:
        """
        Get statistics about todos.

        Returns:
            Dictionary with counts for different statuses and priorities
        """
        stats = {
            'total': len(self._todos),
            'complete': 0,
            'incomplete': 0,
            'low_priority': 0,
            'medium_priority': 0,
            'high_priority': 0
        }

        for todo in self._todos.values():
            if todo.status == 'complete':
                stats['complete'] += 1
            else:
                stats['incomplete'] += 1

            if todo.priority == 'low':
                stats['low_priority'] += 1
            elif todo.priority == 'medium':
                stats['medium_priority'] += 1
            elif todo.priority == 'high':
                stats['high_priority'] += 1

        return stats


def main():
    """
    Example usage of the TodoService.
    Demonstrates all core functionality.
    """
    # Create a todo service instance
    service = TodoService()

    # Add some todos
    print("Adding todos...")
    todo1 = service.add_todo("Buy groceries", "Milk, eggs, bread", "high")
    todo2 = service.add_todo("Finish report", "Complete the quarterly report", "medium")
    todo3 = service.add_todo("Call dentist", "Schedule appointment", "low")

    print(f"Added todo: {todo1.title}")
    print(f"Added todo: {todo2.title}")
    print(f"Added todo: {todo3.title}")

    # List all todos
    print("\nAll todos:")
    for todo in service.get_all_todos():
        print(f"- {todo.title} [{todo.status}] ({todo.priority})")

    # Mark one as complete
    print(f"\nMarking '{todo1.title}' as complete...")
    service.mark_todo_complete(todo1.id)

    # List incomplete todos
    print("\nIncomplete todos:")
    for todo in service.get_todos_by_status("incomplete"):
        print(f"- {todo.title} [{todo.status}] ({todo.priority})")

    # Update a todo
    print(f"\nUpdating '{todo2.title}'...")
    service.update_todo(todo2.id, title="Finish important report", priority="high")

    # Show stats
    print("\nStatistics:")
    stats = service.get_stats()
    for key, value in stats.items():
        print(f"- {key}: {value}")


if __name__ == "__main__":
    main()