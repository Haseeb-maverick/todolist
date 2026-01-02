"""
Todo entity representing a task that needs to be completed.
"""
from typing import Optional
from dataclasses import dataclass


@dataclass
class Todo:
    """
    Represents a todo item with required and optional attributes.

    Attributes:
        id: Unique identifier for the todo item, auto-generated
        title: Title or name of the todo item (required)
        description: Detailed description of the todo item (required)
        status: Current status of the todo (required, values: "incomplete", "complete")
        priority: Priority level of the todo (optional, values: "low", "medium", "high", defaults to "medium")
    """
    id: int
    title: str
    description: str
    status: str = "incomplete"
    priority: str = "medium"

    def __post_init__(self):
        """Validate the todo after initialization."""
        self.validate()

    def validate(self):
        """Validate the todo attributes according to business rules."""
        # Validate id
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"ID must be a positive integer, got {self.id}")

        # Validate title
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError(f"Title must be a non-empty string, got {self.title}")
        if len(self.title) < 1 or len(self.title) > 200:
            raise ValueError(f"Title must be 1-200 characters, got {len(self.title)} characters")

        # Validate description
        if not isinstance(self.description, str) or not self.description.strip():
            raise ValueError(f"Description must be a non-empty string, got {self.description}")
        if len(self.description) < 1 or len(self.description) > 1000:
            raise ValueError(f"Description must be 1-1000 characters, got {len(self.description)} characters")

        # Validate status
        if self.status not in ["incomplete", "complete"]:
            raise ValueError(f"Status must be 'incomplete' or 'complete', got {self.status}")

        # Validate priority
        if self.priority not in ["low", "medium", "high"]:
            raise ValueError(f"Priority must be 'low', 'medium', or 'high', got {self.priority}")

    def mark_complete(self):
        """Mark the todo as complete."""
        self.status = "complete"

    def mark_incomplete(self):
        """Mark the todo as incomplete."""
        self.status = "incomplete"