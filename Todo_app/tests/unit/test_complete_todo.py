"""
Unit tests for the complete todo functionality.
"""
import pytest
import json
from src.services.todo_service import TodoService


class TestCompleteTodo:
    """Tests for the complete todo functionality."""
    
    def test_complete_existing_todo_succeeds(self):
        """Test that marking an existing todo as complete succeeds."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Test todo")
        added_todo = json.loads(add_result)
        
        # Verify it starts as incomplete
        assert added_todo['completed'] is False
        
        # Mark as complete
        complete_result = service.complete_todo(added_todo['id'])
        completed_todo = json.loads(complete_result)
        
        # Verify it's now complete
        assert completed_todo['id'] == added_todo['id']
        assert completed_todo['title'] == added_todo['title']
        assert completed_todo['completed'] is True
    
    def test_complete_already_completed_todo_succeeds(self):
        """Test that marking an already completed todo as complete succeeds."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Test todo")
        added_todo = json.loads(add_result)
        
        # Mark as complete first time
        complete_result1 = service.complete_todo(added_todo['id'])
        completed_todo1 = json.loads(complete_result1)
        assert completed_todo1['completed'] is True
        
        # Mark as complete second time
        complete_result2 = service.complete_todo(added_todo['id'])
        completed_todo2 = json.loads(complete_result2)
        
        # Verify it's still complete
        assert completed_todo2['id'] == added_todo['id']
        assert completed_todo2['title'] == added_todo['title']
        assert completed_todo2['completed'] is True
    
    def test_complete_nonexistent_todo_raises_error(self):
        """Test that marking a nonexistent todo as complete raises an error."""
        service = TodoService()
        
        with pytest.raises(ValueError, match="Todo with ID 999 does not exist"):
            service.complete_todo(999)
    
    def test_completed_todo_is_persisted(self):
        """Test that a completed todo is persisted and can be retrieved with the new status."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Test todo")
        added_todo = json.loads(add_result)
        
        # Mark as complete
        complete_result = service.complete_todo(added_todo['id'])
        completed_todo = json.loads(complete_result)
        
        # Verify the completion is reflected when listing todos
        list_result = service.list_todos()
        parsed_list = json.loads(list_result)
        
        # Find the completed todo
        found_todo = next((t for t in parsed_list if t['id'] == completed_todo['id']), None)
        assert found_todo is not None
        assert found_todo['completed'] is True
    
    def test_complete_todo_only_changes_completion_status(self):
        """Test that completing a todo only changes the completion status."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Original title")
        added_todo = json.loads(add_result)
        
        # Mark as complete
        complete_result = service.complete_todo(added_todo['id'])
        completed_todo = json.loads(complete_result)
        
        # Verify only the completion status changed
        assert completed_todo['id'] == added_todo['id']
        assert completed_todo['title'] == added_todo['title']
        assert completed_todo['completed'] is True  # Changed from False
    
    def test_complete_todo_preserves_other_attributes(self):
        """Test that completing a todo preserves all other attributes."""
        service = TodoService()
        
        # Add a todo first
        add_result = service.add_todo("Test todo")
        added_todo = json.loads(add_result)
        original_id = added_todo['id']
        original_title = added_todo['title']
        
        # Mark as complete
        complete_result = service.complete_todo(original_id)
        completed_todo = json.loads(complete_result)
        
        # Verify the ID and title are preserved
        assert completed_todo['id'] == original_id
        assert completed_todo['title'] == original_title
        assert completed_todo['completed'] is True
    
    def test_can_list_completed_and_incomplete_todos(self):
        """Test that completed and incomplete todos can be distinguished when listed."""
        service = TodoService()
        
        # Add two todos
        add_result1 = service.add_todo("Incomplete todo")
        add_result2 = service.add_todo("Complete me")
        
        added_todo1 = json.loads(add_result1)
        added_todo2 = json.loads(add_result2)
        
        # Mark one as complete
        service.complete_todo(added_todo2['id'])
        
        # List todos
        list_result = service.list_todos()
        parsed_list = json.loads(list_result)
        
        # Find both todos
        todo1 = next((t for t in parsed_list if t['id'] == added_todo1['id']), None)
        todo2 = next((t for t in parsed_list if t['id'] == added_todo2['id']), None)
        
        assert todo1 is not None
        assert todo2 is not None
        assert todo1['completed'] is False
        assert todo2['completed'] is True