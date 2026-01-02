# Quickstart Guide: Phase I – In-Memory Console-Based Todo App

**Date**: 2026-01-01
**Feature**: 001-todo-app

## Getting Started

This guide will help you set up and run the in-memory console-based todo application.

### Prerequisites

- Python 3.8 or higher
- No additional dependencies required

### Setup

1. Clone or create the project directory structure:
   ```
   todo_app/
   ├── domain/
   │   └── todo.py
   ├── store/
   │   └── todo_store.py
   ├── commands/
   │   ├── add.py
   │   ├── view.py
   │   ├── update.py
   │   ├── delete.py
   │   └── complete.py
   ├── cli/
   │   └── console.py
   ├── main.py
   └── README.md
   ```

2. Install dependencies (none required for this application)

### Running the Application

```bash
cd todo_app
python main.py
```

### Basic Usage

Once the application starts, you'll see a menu with the following options:

1. **Add Todo**: Create a new todo with title, description, and optional priority
2. **View Todos**: See all todos or filter by status (all, completed, incomplete)
3. **Update Todo**: Modify an existing todo's title, description, or priority
4. **Delete Todo**: Remove a todo permanently (with confirmation)
5. **Mark Complete**: Change a todo's status to complete
6. **Exit**: Quit the application

### Example Workflow

1. Start the application: `python main.py`
2. Choose "Add Todo" and enter:
   - Title: "Buy groceries"
   - Description: "Milk, bread, eggs, fruits"
   - Priority: "high"
3. Choose "View Todos" to see your todo list
4. Choose "Mark Complete" to mark the todo as done
5. Choose "View Completed Todos" to see completed items
6. Choose "Exit" to quit

### Common Commands

- Add a new todo with title "Learn Python" and description "Complete tutorial"
- View all todos to see your current list
- Update a todo by ID to change its details
- Delete a todo by ID (with confirmation)
- Mark a todo complete/incomplete by ID

### Troubleshooting

- If you get a "command not found" error, ensure you're in the correct directory
- If the application crashes, check that you're entering valid inputs
- If todos aren't saving, remember that this is an in-memory application - todos are lost when the application exits