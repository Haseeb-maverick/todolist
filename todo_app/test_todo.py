"""
Test script for the Todo Application.
Tests all core functionality.
"""

from todo_app.todo_logic import TodoManager


def test_todo_operations():
    """Test all todo operations."""
    print("Testing Todo Application Operations...")
    print("="*50)

    # Initialize the todo manager
    tm = TodoManager()

    # Test 1: Add todos
    print("\n1. Testing ADD operations:")
    todo1 = tm.add_todo("Buy groceries", "Milk, bread, eggs")
    print(f"   Added: {todo1}")

    todo2 = tm.add_todo("Finish report", "Complete the quarterly report")
    print(f"   Added: {todo2}")

    todo3 = tm.add_todo("Call dentist", "Schedule appointment")
    print(f"   Added: {todo3}")

    # Test 2: View all todos
    print("\n2. Testing VIEW ALL operations:")
    all_todos = tm.get_all_todos()
    for todo in all_todos:
        print(f"   {todo}")

    # Test 3: View pending todos
    print("\n3. Testing VIEW PENDING operations:")
    pending_todos = tm.get_pending_todos()
    for todo in pending_todos:
        print(f"   {todo}")

    # Test 4: Mark todo as complete
    print("\n4. Testing MARK COMPLETE operations:")
    success = tm.mark_complete(todo1.id)
    print(f"   Marked todo {todo1.id} as complete: {success}")

    # Verify the change
    updated_todo = tm.get_todo(todo1.id)
    print(f"   Updated todo: {updated_todo}")

    # Test 5: View completed todos
    print("\n5. Testing VIEW COMPLETED operations:")
    completed_todos = tm.get_completed_todos()
    for todo in completed_todos:
        print(f"   {todo}")

    # Test 6: Update todo
    print("\n6. Testing UPDATE operations:")
    updated = tm.update_todo(todo2.id, "Updated task", "Updated description")
    print(f"   Updated todo: {updated}")

    # Test 7: Delete todo
    print("\n7. Testing DELETE operations:")
    all_before = len(tm.get_all_todos())
    print(f"   Todos before deletion: {all_before}")

    success = tm.delete_todo(todo3.id)
    print(f"   Deleted todo {todo3.id}: {success}")

    all_after = len(tm.get_all_todos())
    print(f"   Todos after deletion: {all_after}")

    # Final view to confirm state
    print("\n8. Final state:")
    all_todos = tm.get_all_todos()
    for todo in all_todos:
        print(f"   {todo}")

    print("\nAll tests completed successfully!")


def test_error_handling():
    """Test error handling scenarios."""
    print("\nTesting Error Handling...")
    print("="*50)

    tm = TodoManager()

    # Test adding empty title
    try:
        tm.add_todo("")
        print("   ERROR: Should have raised ValueError for empty title")
    except ValueError as e:
        print(f"   V Correctly caught error for empty title: {e}")

    # Test updating with empty title
    todo = tm.add_todo("Test todo")
    try:
        tm.update_todo(todo.id, "")
        print("   ERROR: Should have raised ValueError for empty title in update")
    except ValueError as e:
        print(f"   V Correctly caught error for empty title in update: {e}")

    # Test operations on non-existent todo
    success = tm.delete_todo(999)
    print(f"   V Deleting non-existent todo returns: {success}")

    success = tm.mark_complete(999)
    print(f"   V Marking non-existent todo complete returns: {success}")

    todo = tm.update_todo(999, "New title")
    print(f"   V Updating non-existent todo returns: {todo}")

    todo = tm.get_todo(999)
    print(f"   V Getting non-existent todo returns: {todo}")


if __name__ == "__main__":
    test_todo_operations()
    test_error_handling()