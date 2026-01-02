# Todo Application

A simple command-line todo application implemented in Python with in-memory storage.

## Features

- Add new todo items with title and description
- View all todos, pending todos, or completed todos
- Update existing todo items
- Mark todos as complete or incomplete
- Delete todo items
- In-memory storage (data is lost when the application exits)

## File Structure

```
todo_app/
├── __main__.py      # Main entry point for the application
├── todo_logic.py    # Core business logic and data models
├── console_interface.py  # Console UI and user interaction
└── test_todo.py     # Test script for functionality verification
```

## How to Run

To run the application:

```bash
python -m todo_app
```

To run tests:

```bash
python -m todo_app.test_todo
```

## Functionality

### Menu Options

1. **Add Todo**: Create a new todo item with title and optional description
2. **View All Todos**: Display all todo items
3. **View Pending Todos**: Display only incomplete todo items
4. **View Completed Todos**: Display only completed todo items
5. **Update Todo**: Modify the title or description of an existing todo
6. **Mark Todo Complete**: Change a todo's status to completed
7. **Mark Todo Incomplete**: Change a todo's status to incomplete
8. **Delete Todo**: Remove a todo item permanently
9. **Exit**: Close the application

### Data Model

Each todo item has:
- Unique ID
- Title (required)
- Description (optional)
- Completion status (boolean)
- Creation timestamp
- Last updated timestamp

## Validation and Error Handling

- Empty titles are not allowed when adding or updating todos
- Attempting to update/delete non-existent todos is handled gracefully
- Invalid input (like non-numeric IDs) is caught and handled
- All operations return appropriate success/failure indicators

## Architecture

The application follows a clean architecture pattern:
- **Business Logic Layer**: `todo_logic.py` contains the core TodoManager class
- **Presentation Layer**: `console_interface.py` handles user interaction
- **Main Module**: `__main__.py` orchestrates the application components