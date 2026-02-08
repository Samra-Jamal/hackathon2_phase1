"""
Integration tests for the list command in the Todo application.
"""
import subprocess
import sys
import json


def run_todo_command(args):
    """Helper function to run the todo command with given arguments."""
    cmd = [sys.executable, "src/todo_app.py"] + args
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result


class TestListCommandIntegration:
    """Integration tests for the list command."""
    
    def test_list_empty_todos_returns_empty_array(self):
        """Test that listing todos when none exist returns an empty array."""
        result = run_todo_command(["list"])
        
        # Verify the command succeeded
        assert result.returncode == 0
        
        # Parse the output to verify it's valid JSON
        parsed_result = json.loads(result.stdout.strip())
        
        # Verify it's an empty array
        assert parsed_result == []
    
    def test_list_single_todo_returns_correct_json(self):
        """Test that listing todos with one item returns the correct JSON."""
        # Add a todo first
        add_result = run_todo_command(["add", "Test todo"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        
        # List todos
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        parsed_list = json.loads(list_result.stdout.strip())
        
        # Verify the list contains one item
        assert len(parsed_list) == 1
        assert parsed_list[0]['id'] == added_todo['id']
        assert parsed_list[0]['title'] == added_todo['title']
        assert parsed_list[0]['completed'] == added_todo['completed']
    
    def test_list_multiple_todos_returns_correct_json(self):
        """Test that listing multiple todos returns the correct JSON."""
        # Add multiple todos
        add_result1 = run_todo_command(["add", "First todo"])
        assert add_result1.returncode == 0
        add_result2 = run_todo_command(["add", "Second todo"])
        assert add_result2.returncode == 0
        add_result3 = run_todo_command(["add", "Third todo"])
        assert add_result3.returncode == 0
        
        added_todo1 = json.loads(add_result1.stdout.strip())
        added_todo2 = json.loads(add_result2.stdout.strip())
        added_todo3 = json.loads(add_result3.stdout.strip())
        
        # List todos
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        parsed_list = json.loads(list_result.stdout.strip())
        
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
    
    def test_list_command_preserves_completion_status(self):
        """Test that the list command preserves the completion status."""
        # Add a todo
        add_result = run_todo_command(["add", "Test todo"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        
        # Mark as complete
        complete_result = run_todo_command(["complete", str(added_todo['id'])])
        assert complete_result.returncode == 0
        
        # List todos
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        parsed_list = json.loads(list_result.stdout.strip())
        
        # Verify the completion status is preserved
        assert len(parsed_list) == 1
        assert parsed_list[0]['id'] == added_todo['id']
        assert parsed_list[0]['completed'] is True
    
    def test_list_command_does_not_show_deleted_todos(self):
        """Test that the list command does not show deleted todos."""
        # Add two todos
        add_result1 = run_todo_command(["add", "First todo"])
        assert add_result1.returncode == 0
        add_result2 = run_todo_command(["add", "Second todo"])
        assert add_result2.returncode == 0
        
        added_todo1 = json.loads(add_result1.stdout.strip())
        added_todo2 = json.loads(add_result2.stdout.strip())
        
        # Delete the first todo
        delete_result = run_todo_command(["delete", str(added_todo1['id'])])
        assert delete_result.returncode == 0
        
        # List todos
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        parsed_list = json.loads(list_result.stdout.strip())
        
        # Verify only the second todo is in the list
        assert len(parsed_list) == 1
        assert parsed_list[0]['id'] == added_todo2['id']
        assert parsed_list[0]['title'] == "Second todo"
    
    def test_list_command_output_format(self):
        """Test that the list command output is in the correct format."""
        # Add a todo
        add_result = run_todo_command(["add", "Test todo"])
        assert add_result.returncode == 0
        
        # List todos
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        
        # Verify it's valid JSON and an array
        parsed_result = json.loads(list_result.stdout.strip())
        assert isinstance(parsed_result, list)
        
        # Verify each item in the array has the correct structure
        for todo in parsed_result:
            assert 'id' in todo
            assert 'title' in todo
            assert 'completed' in todo
            assert isinstance(todo['id'], int)
            assert isinstance(todo['title'], str)
            assert isinstance(todo['completed'], bool)
    
    def test_list_command_works_after_other_operations(self):
        """Test that the list command works correctly after various operations."""
        # Add a few todos
        run_todo_command(["add", "Todo 1"])
        run_todo_command(["add", "Todo 2"])
        run_todo_command(["add", "Todo 3"])
        
        # Update one
        run_todo_command(["update", "1", "Updated Todo 1"])
        
        # Mark one as complete
        run_todo_command(["complete", "2"])
        
        # List todos
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        parsed_list = json.loads(list_result.stdout.strip())
        
        # Verify all operations are reflected in the list
        assert len(parsed_list) == 3
        
        # Find the updated todo
        updated_todo = next((t for t in parsed_list if t['id'] == 1), None)
        assert updated_todo is not None
        assert updated_todo['title'] == "Updated Todo 1"
        
        # Find the completed todo
        completed_todo = next((t for t in parsed_list if t['id'] == 2), None)
        assert completed_todo is not None
        assert completed_todo['completed'] is True