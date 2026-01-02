# Data Model: Phase I – In-Memory Console-Based Todo App

**Date**: 2026-01-01
**Feature**: 001-todo-app

## Todo Entity

### Attributes

- **id** (int, required): Unique identifier for the todo item, auto-generated
- **title** (str, required): Title or name of the todo item
- **description** (str, required): Detailed description of the todo item
- **status** (str, required): Current status of the todo, values: "incomplete", "complete"
- **priority** (str, optional): Priority level of the todo, values: "low", "medium", "high", defaults to "medium"

### Validation Rules

- **id**: Must be a positive integer, unique across all todos
- **title**: Must be a non-empty string with 1-200 characters
- **description**: Must be a non-empty string with 1-1000 characters
- **status**: Must be one of the allowed values ("incomplete", "complete")
- **priority**: If provided, must be one of the allowed values ("low", "medium", "high")

### State Transitions

- **incomplete → complete**: When user marks todo as complete
- **complete → incomplete**: When user marks completed todo as incomplete (if supported)

## TodoStore

### Responsibilities

- Store all todos in memory
- Provide CRUD operations for todos
- Generate unique IDs for new todos
- Maintain data integrity and validation

### Operations

- **add(todo)**: Add a new todo to the store, return the added todo with ID
- **get(todo_id)**: Retrieve a todo by its ID
- **update(todo_id, updates)**: Update a todo's attributes
- **delete(todo_id)**: Remove a todo from the store
- **list_all()**: Return all todos
- **list_by_status(status)**: Return todos with specific status
- **mark_complete(todo_id)**: Mark a todo as complete
- **mark_incomplete(todo_id)**: Mark a todo as incomplete

### Data Structure

The store uses a dictionary (hash map) for O(1) lookup by ID and a list for maintaining all todos:

```python
store = {
    'todos_by_id': {id: todo_object},  # For O(1) lookup by ID
    'all_todos': [todo_object, ...]    # For listing operations
}
```

## Relationships

- TodoStore contains multiple Todo entities
- Each Todo has a unique ID within the TodoStore