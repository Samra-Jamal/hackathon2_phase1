"""
Unit tests for the list todos functionality.
"""
import pytest
import json
from src.services.todo_service import TodoService


class TestListTodos:
    """Tests for the list todos functionality."""
    
    def test_list_empty_todos_returns_empty_array(self):
        """Test that listing todos when none exist returns an empty array."""
        service = TodoService()
        result = service.list_todos()
        
        parsed_result = json.loads(result)
        assert parsed_result == []
    
    def test_list_single_todo_returns_array_with_one_item(self):
        """Test that listing todos with one item returns an array with that item."""
        service = TodoService()
        # Add a todo first
        add_result = service.add_todo("Test todo")
        added_todo = json.loads(add_result)
        
        # List todos
        list_result = service.list_todos()
        parsed_list = json.loads(list_result)
        
        # Verify the list contains one item
        assert len(parsed_list) == 1
        assert parsed_list[0]['id'] == added_todo['id']
        assert parsed_list[0]['title'] == added_todo['title']
        assert parsed_list[0]['completed'] == added_todo['completed']
    
    def test_list_multiple_todos_returns_correct_array(self):
        """Test that listing todos with multiple items returns the correct array."""
        service = TodoService()
        
        # Add multiple todos
        result1 = service.add_todo("First todo")
        result2 = service.add_todo("Second todo")
        result3 = service.add_todo("Third todo")
        
        added_todo1 = json.loads(result1)
        added_todo2 = json.loads(result2)
        added_todo3 = json.loads(result3)
        
        # List todos
        list_result = service.list_todos()
        parsed_list = json.loads(list_result)
        
        # Verify the list contains all items
        assert len(parsed_list) == 3
        
        # Check that all added todos are in the list
        ids_in_list = [todo['id'] for todo in parsed_list]
        assert added_todo1['id'] in ids_in_list
        assert added_todo2['id'] in ids_in_list
        assert added_todo3['id'] in ids_in_list
        
        # Check titles
        titles_in_list = [todo['title'] for todo in parsed_list]
        assert "First todo" in titles_in_list
        assert "Second todo" in titles_in_list
        assert "Third todo" in titles_in_list
    
    def test_list_todos_preserves_completion_status(self):
        """Test that listing todos preserves the completion status."""
        service = TodoService()
        
        # Add a todo and mark it as complete
        add_result = service.add_todo("Test todo")
        added_todo = json.loads(add_result)
        
        # Mark as complete
        service.complete_todo(added_todo['id'])
        
        # List todos
        list_result = service.list_todos()
        parsed_list = json.loads(list_result)
        
        # Verify the completion status is preserved
        assert len(parsed_list) == 1
        assert parsed_list[0]['id'] == added_todo['id']
        assert parsed_list[0]['completed'] is True
    
    def test_list_todos_does_not_include_deleted_todos(self):
        """Test that listing todos does not include deleted todos."""
        service = TodoService()
        
        # Add two todos
        result1 = service.add_todo("First todo")
        result2 = service.add_todo("Second todo")
        
        added_todo1 = json.loads(result1)
        added_todo2 = json.loads(result2)
        
        # Delete the first todo
        service.delete_todo(added_todo1['id'])
        
        # List todos
        list_result = service.list_todos()
        parsed_list = json.loads(list_result)
        
        # Verify only the second todo is in the list
        assert len(parsed_list) == 1
        assert parsed_list[0]['id'] == added_todo2['id']
        assert parsed_list[0]['title'] == "Second todo"
    
    def test_list_todos_returns_json_array(self):
        """Test that the list todos function returns a valid JSON array."""
        service = TodoService()
        
        # Add a few todos
        service.add_todo("First todo")
        service.add_todo("Second todo")
        
        # List todos
        result = service.list_todos()
        
        # Verify it's valid JSON and an array
        parsed_result = json.loads(result)
        assert isinstance(parsed_result, list)
        
        # Verify each item in the array has the correct structure
        for todo in parsed_result:
            assert 'id' in todo
            assert 'title' in todo
            assert 'completed' in todo
            assert isinstance(todo['id'], int)
            assert isinstance(todo['title'], str)
            assert isinstance(todo['completed'], bool)