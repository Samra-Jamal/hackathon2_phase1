"""
Unit tests for the delete todo functionality.
"""
import pytest
import json
from src.services.todo_service import TodoService


class TestDeleteTodo:
    """Tests for the delete todo functionality."""
    
    def test_delete_existing_todo_succeeds(self):
        """Test that deleting an existing todo succeeds."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Test todo")
        added_todo = json.loads(add_result)
        original_id = added_todo['id']
        
        # Delete the todo
        delete_result = service.delete_todo(original_id)
        
        # Verify the result is a confirmation message
        assert "deleted successfully" in delete_result
        
        # Verify the todo no longer exists
        list_result = service.list_todos()
        parsed_list = json.loads(list_result)
        assert len(parsed_list) == 0
        
        # Verify the todo cannot be retrieved individually
        list_all = service.list_todos()
        parsed_all = json.loads(list_all)
        found_todo = next((t for t in parsed_all if t['id'] == original_id), None)
        assert found_todo is None
    
    def test_delete_nonexistent_todo_raises_error(self):
        """Test that deleting a nonexistent todo raises an error."""
        service = TodoService()
        
        with pytest.raises(ValueError, match="Todo with ID 999 does not exist"):
            service.delete_todo(999)
    
    def test_delete_todo_removes_only_that_todo(self):
        """Test that deleting a todo only removes that specific todo."""
        service = TodoService()
        
        # Add multiple todos
        add_result1 = service.add_todo("First todo")
        add_result2 = service.add_todo("Second todo")
        add_result3 = service.add_todo("Third todo")
        
        added_todo1 = json.loads(add_result1)
        added_todo2 = json.loads(add_result2)
        added_todo3 = json.loads(add_result3)
        
        original_id1 = added_todo1['id']
        original_id2 = added_todo2['id']
        original_id3 = added_todo3['id']
        
        # Delete the second todo
        delete_result = service.delete_todo(original_id2)
        assert "deleted successfully" in delete_result
        
        # Verify the other todos still exist
        list_result = service.list_todos()
        parsed_list = json.loads(list_result)
        
        assert len(parsed_list) == 2
        
        # Verify the first and third todos are still there
        ids_in_list = [todo['id'] for todo in parsed_list]
        assert original_id1 in ids_in_list
        assert original_id3 in ids_in_list
        
        # Verify the second todo is gone
        assert original_id2 not in ids_in_list
    
    def test_delete_todo_then_add_new_todo_has_different_id(self):
        """Test that after deleting a todo, new todos don't reuse the deleted ID."""
        service = TodoService()
        
        # Add a todo and note its ID
        add_result1 = service.add_todo("First todo")
        added_todo1 = json.loads(add_result1)
        original_id = added_todo1['id']
        
        # Delete the todo
        delete_result = service.delete_todo(original_id)
        assert "deleted successfully" in delete_result
        
        # Add a new todo
        add_result2 = service.add_todo("Second todo")
        added_todo2 = json.loads(add_result2)
        
        # The new todo should have a different ID
        assert added_todo2['id'] != original_id
    
    def test_delete_all_todos_results_in_empty_list(self):
        """Test that deleting all todos results in an empty list."""
        service = TodoService()
        
        # Add multiple todos
        add_result1 = service.add_todo("First todo")
        add_result2 = service.add_todo("Second todo")
        add_result3 = service.add_todo("Third todo")
        
        added_todo1 = json.loads(add_result1)
        added_todo2 = json.loads(add_result2)
        added_todo3 = json.loads(add_result3)
        
        original_id1 = added_todo1['id']
        original_id2 = added_todo2['id']
        original_id3 = added_todo3['id']
        
        # Delete all todos
        service.delete_todo(original_id1)
        service.delete_todo(original_id2)
        service.delete_todo(original_id3)
        
        # Verify the list is now empty
        list_result = service.list_todos()
        parsed_list = json.loads(list_result)
        assert len(parsed_list) == 0
    
    def test_delete_todo_prevents_other_operations_on_that_todo(self):
        """Test that after deleting a todo, other operations on it fail."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Test todo")
        added_todo = json.loads(add_result)
        original_id = added_todo['id']
        
        # Delete the todo
        delete_result = service.delete_todo(original_id)
        assert "deleted successfully" in delete_result
        
        # Verify that trying to update the deleted todo fails
        with pytest.raises(ValueError, match=f"Todo with ID {original_id} does not exist"):
            service.update_todo(original_id, "Updated title")
        
        # Verify that trying to mark the deleted todo as complete fails
        with pytest.raises(ValueError, match=f"Todo with ID {original_id} does not exist"):
            service.complete_todo(original_id)
        
        # Verify that trying to delete the deleted todo again fails
        with pytest.raises(ValueError, match=f"Todo with ID {original_id} does not exist"):
            service.delete_todo(original_id)