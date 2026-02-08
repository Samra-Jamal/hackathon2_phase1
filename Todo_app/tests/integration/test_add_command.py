"""
Integration tests for the add command in the Todo application.
"""
import subprocess
import sys
import json
import os


def run_todo_command(args):
    """Helper function to run the todo command with given arguments."""
    cmd = [sys.executable, "src/todo_app.py"] + args
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result


class TestAddCommandIntegration:
    """Integration tests for the add command."""
    
    def test_add_valid_todo_succeeds(self):
        """Test that adding a valid todo succeeds and returns correct JSON."""
        result = run_todo_command(["add", "Test todo"])
        
        # Verify the command succeeded
        assert result.returncode == 0
        
        # Parse the output to verify it's valid JSON
        parsed_result = json.loads(result.stdout.strip())
        
        # Verify the structure of the returned todo
        assert 'id' in parsed_result
        assert parsed_result['title'] == "Test todo"
        assert parsed_result['completed'] is False  # Default value
        
        # Verify the ID is positive
        assert isinstance(parsed_result['id'], int)
        assert parsed_result['id'] > 0
    
    def test_add_multiple_todos_have_unique_ids(self):
        """Test that adding multiple todos creates unique IDs."""
        # Add first todo
        result1 = run_todo_command(["add", "First todo"])
        assert result1.returncode == 0
        parsed_result1 = json.loads(result1.stdout.strip())
        
        # Add second todo
        result2 = run_todo_command(["add", "Second todo"])
        assert result2.returncode == 0
        parsed_result2 = json.loads(result2.stdout.strip())
        
        # Verify IDs are different
        assert parsed_result1['id'] != parsed_result2['id']
        
        # Verify both IDs are positive
        assert parsed_result1['id'] > 0
        assert parsed_result2['id'] > 0
    
    def test_add_todo_with_empty_title_fails(self):
        """Test that adding a todo with an empty title fails."""
        result = run_todo_command(["add", ""])
        
        # Verify the command failed
        assert result.returncode == 1
        
        # Verify the error message
        assert "Error:" in result.stderr
        assert "Title cannot be empty" in result.stderr
    
    def test_add_todo_with_whitespace_only_title_fails(self):
        """Test that adding a todo with whitespace-only title fails."""
        result = run_todo_command(["add", "   "])
        
        # Verify the command failed
        assert result.returncode == 1
        
        # Verify the error message
        assert "Error:" in result.stderr
        assert "Title cannot be empty" in result.stderr
    
    def test_added_todo_appears_in_list(self):
        """Test that an added todo appears in the list command."""
        # Add a todo
        add_result = run_todo_command(["add", "Test todo for listing"])
        assert add_result.returncode == 0
        parsed_add_result = json.loads(add_result.stdout.strip())
        new_id = parsed_add_result['id']
        
        # List all todos
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        parsed_list = json.loads(list_result.stdout.strip())
        
        # Find the todo with the new ID
        found_todo = None
        for todo in parsed_list:
            if todo['id'] == new_id:
                found_todo = todo
                break
        
        assert found_todo is not None
        assert found_todo['title'] == "Test todo for listing"
        assert found_todo['completed'] is False
    
    def test_add_todo_with_special_characters(self):
        """Test that adding a todo with special characters works correctly."""
        special_title = "Test todo with special chars: !@#$%^&*()"
        result = run_todo_command(["add", special_title])
        
        # Verify the command succeeded
        assert result.returncode == 0
        
        # Parse the output to verify it's valid JSON
        parsed_result = json.loads(result.stdout.strip())
        
        # Verify the title is preserved
        assert parsed_result['title'] == special_title
        assert parsed_result['completed'] is False