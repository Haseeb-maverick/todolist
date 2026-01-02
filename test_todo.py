"""
Tests for the Todo application logic.
"""

from todo import TodoService
import datetime


def test_todo_creation():
    """Test creating todos."""
    service = TodoService()

    # Test adding a basic todo
    todo = service.add_todo("Test task", "Test description", "high")

    assert todo.title == "Test task"
    assert todo.description == "Test description"
    assert todo.status == "incomplete"
    assert todo.priority == "high"
    assert todo.created_at <= datetime.datetime.now()
    assert todo.updated_at <= datetime.datetime.now()

    print("PASS: Todo creation test passed")


def test_todo_retrieval():
    """Test retrieving todos."""
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Test task", "Test description", "medium")

    # Retrieve by ID
    retrieved = service.get_todo(todo.id)
    assert retrieved is not None
    assert retrieved.id == todo.id
    assert retrieved.title == "Test task"

    # Try to retrieve non-existent todo
    not_found = service.get_todo("non-existent-id")
    assert not_found is None

    print("PASS: Todo retrieval test passed")


def test_todo_update():
    """Test updating todos."""
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Original task", "Original description", "low")

    # Update the todo
    updated = service.update_todo(todo.id, title="Updated task", priority="high")
    assert updated is not None
    assert updated.title == "Updated task"
    assert updated.priority == "high"
    assert updated.description == "Original description"  # Should remain unchanged

    # Try to update non-existent todo
    not_found = service.update_todo("non-existent-id", title="New title")
    assert not_found is None

    print("PASS: Todo update test passed")


def test_todo_status_management():
    """Test marking todos as complete/incomplete."""
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Test task", "Test description", "medium")

    # Mark as complete
    result = service.mark_todo_complete(todo.id)
    assert result is True
    assert todo.status == "complete"

    # Mark as incomplete
    result = service.mark_todo_incomplete(todo.id)
    assert result is True
    assert todo.status == "incomplete"

    # Try to mark non-existent todo
    result = service.mark_todo_complete("non-existent-id")
    assert result is False

    print("PASS: Todo status management test passed")


def test_todo_deletion():
    """Test deleting todos."""
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Test task", "Test description", "medium")

    # Verify it exists
    assert service.get_todo(todo.id) is not None

    # Delete it
    result = service.delete_todo(todo.id)
    assert result is True

    # Verify it's gone
    assert service.get_todo(todo.id) is None

    # Try to delete non-existent todo
    result = service.delete_todo("non-existent-id")
    assert result is False

    print("PASS: Todo deletion test passed")


def test_filters():
    """Test filtering todos by status and priority."""
    service = TodoService()

    # Add todos with different statuses and priorities
    todo1 = service.add_todo("Task 1", "Description 1", "high")
    todo2 = service.add_todo("Task 2", "Description 2", "medium")
    todo3 = service.add_todo("Task 3", "Description 3", "low")

    # Mark one as complete
    service.mark_todo_complete(todo1.id)

    # Test status filters
    completed = service.get_todos_by_status("complete")
    incomplete = service.get_todos_by_status("incomplete")

    assert len(completed) == 1
    assert len(incomplete) == 2
    assert completed[0].id == todo1.id
    assert all(t.id in [todo2.id, todo3.id] for t in incomplete)

    # Test priority filters
    high_priority = service.get_todos_by_priority("high")
    medium_priority = service.get_todos_by_priority("medium")
    low_priority = service.get_todos_by_priority("low")

    assert len(high_priority) == 1
    assert len(medium_priority) == 1
    assert len(low_priority) == 1
    assert high_priority[0].id == todo1.id
    assert medium_priority[0].id == todo2.id
    assert low_priority[0].id == todo3.id

    print("PASS: Filter tests passed")


def test_statistics():
    """Test statistics functionality."""
    service = TodoService()

    # Add todos with different statuses and priorities
    todo1 = service.add_todo("Task 1", "Description 1", "high")
    todo2 = service.add_todo("Task 2", "Description 2", "medium")
    todo3 = service.add_todo("Task 3", "Description 3", "low")

    # Mark one as complete
    service.mark_todo_complete(todo1.id)

    # Get stats
    stats = service.get_stats()

    assert stats['total'] == 3
    assert stats['complete'] == 1
    assert stats['incomplete'] == 2
    assert stats['high_priority'] == 1
    assert stats['medium_priority'] == 1
    assert stats['low_priority'] == 1

    print("PASS: Statistics test passed")


def test_validation():
    """Test input validation."""
    service = TodoService()

    # Test empty title validation
    try:
        service.add_todo("")
        assert False, "Should have raised ValueError for empty title"
    except ValueError:
        pass  # Expected

    # Test title length validation
    try:
        service.add_todo("A" * 201)  # Too long
        assert False, "Should have raised ValueError for title too long"
    except ValueError:
        pass  # Expected

    # Test description length validation
    try:
        service.add_todo("Valid title", "A" * 1001)  # Too long
        assert False, "Should have raised ValueError for description too long"
    except ValueError:
        pass  # Expected

    # Test invalid status validation
    try:
        service.add_todo("Valid title", "Valid description", "invalid_priority")
        assert False, "Should have raised ValueError for invalid priority"
    except ValueError:
        pass  # Expected

    print("PASS: Validation tests passed")


if __name__ == "__main__":
    print("Running tests...")

    test_todo_creation()
    test_todo_retrieval()
    test_todo_update()
    test_todo_status_management()
    test_todo_deletion()
    test_filters()
    test_statistics()
    test_validation()

    print("\nAll tests passed!")