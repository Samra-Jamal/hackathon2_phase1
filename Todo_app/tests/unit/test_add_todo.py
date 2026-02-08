"""
Unit tests for the add todo functionality.
"""
import pytest
import json
from src.services.todo_service import TodoService
from src.models.todo import Todo


class TestAddTodo:
    """Tests for the add todo functionality."""
    
    def test_add_valid_todo_returns_json(self):
        """Test that adding a valid todo returns the correct JSON representation."""
        service = TodoService()
        result = service.add_todo("Test todo")
        
        # Parse the result to verify it's valid JSON
        parsed_result = json.loads(result)
        
        # Verify the structure of the returned todo
        assert 'id' in parsed_result
        assert parsed_result['title'] == "Test todo"
        assert parsed_result['completed'] is False  # Default value
        
        # Verify the ID is positive
        assert isinstance(parsed_result['id'], int)
        assert parsed_result['id'] > 0
    
    def test_add_todo_creates_unique_ids(self):
        """Test that adding multiple todos creates unique IDs."""
        service = TodoService()
        
        result1 = service.add_todo("First todo")
        result2 = service.add_todo("Second todo")
        
        parsed_result1 = json.loads(result1)
        parsed_result2 = json.loads(result2)
        
        # Verify IDs are different
        assert parsed_result1['id'] != parsed_result2['id']
        
        # Verify both IDs are positive
        assert parsed_result1['id'] > 0
        assert parsed_result2['id'] > 0
        
        # Verify IDs are sequential
        assert parsed_result2['id'] == parsed_result1['id'] + 1
    
    def test_add_todo_with_empty_title_raises_error(self):
        """Test that adding a todo with an empty title raises an error."""
        service = TodoService()
        
        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.add_todo("")
    
    def test_add_todo_with_whitespace_only_title_raises_error(self):
        """Test that adding a todo with whitespace-only title raises an error."""
        service = TodoService()
        
        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.add_todo("   ")
    
    def test_add_todo_strips_whitespace_from_title(self):
        """Test that adding a todo strips leading/trailing whitespace from the title."""
        service = TodoService()
        result = service.add_todo("  Test todo with spaces  ")
        
        parsed_result = json.loads(result)
        assert parsed_result['title'] == "Test todo with spaces"
    
    def test_added_todo_is_retrievable(self):
        """Test that an added todo can be retrieved."""
        service = TodoService()
        result = service.add_todo("Test todo")
        parsed_result = json.loads(result)
        new_id = parsed_result['id']
        
        # Verify the todo exists in the collection
        list_result = service.list_todos()
        parsed_list = json.loads(list_result)
        
        # Find the todo with the new ID
        found_todo = None
        for todo in parsed_list:
            if todo['id'] == new_id:
                found_todo = todo
                break
        
        assert found_todo is not None
        assert found_todo['title'] == "Test todo"
        assert found_todo['completed'] is False
    
    def test_add_todo_default_completed_status_false(self):
        """Test that added todos have completed status set to False by default."""
        service = TodoService()
        result = service.add_todo("Test todo")
        
        parsed_result = json.loads(result)
        assert parsed_result['completed'] is False