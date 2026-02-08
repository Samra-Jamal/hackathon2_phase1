"""
Unit tests for the update todo functionality.
"""
import pytest
import json
from src.services.todo_service import TodoService


class TestUpdateTodo:
    """Tests for the update todo functionality."""
    
    def test_update_existing_todo_succeeds(self):
        """Test that updating an existing todo succeeds."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Original title")
        added_todo = json.loads(add_result)
        
        # Update the todo
        update_result = service.update_todo(added_todo['id'], "Updated title")
        updated_todo = json.loads(update_result)
        
        # Verify the update worked
        assert updated_todo['id'] == added_todo['id']
        assert updated_todo['title'] == "Updated title"
        assert updated_todo['completed'] == added_todo['completed']  # Should remain unchanged
    
    def test_update_todo_changes_only_title(self):
        """Test that updating a todo only changes the title, leaving other fields unchanged."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Original title")
        added_todo = json.loads(add_result)
        
        # Mark as complete to change the completion status
        complete_result = service.complete_todo(added_todo['id'])
        completed_todo = json.loads(complete_result)
        assert completed_todo['completed'] is True
        
        # Update the todo
        update_result = service.update_todo(added_todo['id'], "Updated title")
        updated_todo = json.loads(update_result)
        
        # Verify only the title changed
        assert updated_todo['id'] == added_todo['id']
        assert updated_todo['title'] == "Updated title"
        assert updated_todo['completed'] is True  # Should remain completed
    
    def test_update_nonexistent_todo_raises_error(self):
        """Test that updating a nonexistent todo raises an error."""
        service = TodoService()
        
        with pytest.raises(ValueError, match="Todo with ID 999 does not exist"):
            service.update_todo(999, "Updated title")
    
    def test_update_todo_with_empty_title_raises_error(self):
        """Test that updating a todo with an empty title raises an error."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Original title")
        added_todo = json.loads(add_result)
        
        # Try to update with empty title
        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.update_todo(added_todo['id'], "")
    
    def test_update_todo_with_whitespace_only_title_raises_error(self):
        """Test that updating a todo with whitespace-only title raises an error."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Original title")
        added_todo = json.loads(add_result)
        
        # Try to update with whitespace-only title
        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.update_todo(added_todo['id'], "   ")
    
    def test_updated_todo_is_persisted(self):
        """Test that an updated todo is persisted and can be retrieved with the new title."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Original title")
        added_todo = json.loads(add_result)
        
        # Update the todo
        update_result = service.update_todo(added_todo['id'], "Updated title")
        updated_todo = json.loads(update_result)
        
        # Verify the update is reflected when listing todos
        list_result = service.list_todos()
        parsed_list = json.loads(list_result)
        
        # Find the updated todo
        found_todo = next((t for t in parsed_list if t['id'] == updated_todo['id']), None)
        assert found_todo is not None
        assert found_todo['title'] == "Updated title"
        assert found_todo['completed'] == updated_todo['completed']
    
    def test_update_todo_strips_whitespace_from_title(self):
        """Test that updating a todo strips leading/trailing whitespace from the title."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Original title")
        added_todo = json.loads(add_result)
        
        # Update the todo with whitespace around the title
        update_result = service.update_todo(added_todo['id'], "  Updated title with spaces  ")
        updated_todo = json.loads(update_result)
        
        # Verify the title is properly stripped
        assert updated_todo['title'] == "Updated title with spaces"
    
    def test_update_todo_preserves_id(self):
        """Test that updating a todo preserves its ID."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Original title")
        added_todo = json.loads(add_result)
        original_id = added_todo['id']
        
        # Update the todo
        update_result = service.update_todo(original_id, "Updated title")
        updated_todo = json.loads(update_result)
        
        # Verify the ID is preserved
        assert updated_todo['id'] == original_id