"""
Integration tests for the delete command in the Todo application.
"""
import subprocess
import sys
import json


def run_todo_command(args):
    """Helper function to run the todo command with given arguments."""
    cmd = [sys.executable, "src/todo_app.py"] + args
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result


class TestDeleteCommandIntegration:
    """Integration tests for the delete command."""
    
    def test_delete_existing_todo_succeeds(self):
        """Test that deleting an existing todo succeeds."""
        # Add a todo first
        add_result = run_todo_command(["add", "Test todo"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        original_id = added_todo['id']
        
        # Delete the todo
        delete_result = run_todo_command(["delete", str(original_id)])
        assert delete_result.returncode == 0
        
        # Verify the result is a confirmation message
        assert "deleted successfully" in delete_result.stdout
        
        # Verify the todo no longer exists in the list
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        parsed_list = json.loads(list_result.stdout.strip())
        assert len(parsed_list) == 0
    
    def test_delete_nonexistent_todo_fails(self):
        """Test that deleting a nonexistent todo fails."""
        # Try to delete a todo with ID 999 (which shouldn't exist)
        delete_result = run_todo_command(["delete", "999"])
        
        # Verify the command failed
        assert delete_result.returncode == 1
        
        # Verify the error message
        assert "Error:" in delete_result.stderr
        assert "Todo with ID 999 does not exist" in delete_result.stderr
    
    def test_delete_todo_removes_only_that_todo(self):
        """Test that deleting a todo only removes that specific todo."""
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
        
        original_id1 = added_todo1['id']
        original_id2 = added_todo2['id']
        original_id3 = added_todo3['id']
        
        # Delete the second todo
        delete_result = run_todo_command(["delete", str(original_id2)])
        assert delete_result.returncode == 0
        assert "deleted successfully" in delete_result.stdout
        
        # Verify the other todos still exist
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        parsed_list = json.loads(list_result.stdout.strip())
        
        assert len(parsed_list) == 2
        
        # Verify the first and third todos are still there
        ids_in_list = [todo['id'] for todo in parsed_list]
        assert original_id1 in ids_in_list
        assert original_id3 in ids_in_list
        
        # Verify the second todo is gone
        assert original_id2 not in ids_in_list
    
    def test_delete_todo_then_add_new_todo_has_different_id(self):
        """Test that after deleting a todo, new todos don't reuse the deleted ID."""
        # Add a todo and note its ID
        add_result1 = run_todo_command(["add", "First todo"])
        assert add_result1.returncode == 0
        added_todo1 = json.loads(add_result1.stdout.strip())
        original_id = added_todo1['id']
        
        # Delete the todo
        delete_result = run_todo_command(["delete", str(original_id)])
        assert delete_result.returncode == 0
        assert "deleted successfully" in delete_result.stdout
        
        # Add a new todo
        add_result2 = run_todo_command(["add", "Second todo"])
        assert add_result2.returncode == 0
        added_todo2 = json.loads(add_result2.stdout.strip())
        
        # The new todo should have a different ID
        assert added_todo2['id'] != original_id
    
    def test_delete_all_todos_results_in_empty_list(self):
        """Test that deleting all todos results in an empty list."""
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
        
        original_id1 = added_todo1['id']
        original_id2 = added_todo2['id']
        original_id3 = added_todo3['id']
        
        # Delete all todos
        delete_result1 = run_todo_command(["delete", str(original_id1)])
        assert delete_result1.returncode == 0
        delete_result2 = run_todo_command(["delete", str(original_id2)])
        assert delete_result2.returncode == 0
        delete_result3 = run_todo_command(["delete", str(original_id3)])
        assert delete_result3.returncode == 0
        
        # Verify the list is now empty
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        parsed_list = json.loads(list_result.stdout.strip())
        assert len(parsed_list) == 0
    
    def test_delete_todo_prevents_other_operations_on_that_todo(self):
        """Test that after deleting a todo, other operations on it fail."""
        # Add a todo first
        add_result = run_todo_command(["add", "Test todo"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        original_id = added_todo['id']
        
        # Delete the todo
        delete_result = run_todo_command(["delete", str(original_id)])
        assert delete_result.returncode == 0
        assert "deleted successfully" in delete_result.stdout
        
        # Verify that trying to update the deleted todo fails
        update_result = run_todo_command(["update", str(original_id), "Updated title"])
        assert update_result.returncode == 1
        assert "Todo with ID 1 does not exist" in update_result.stderr
        
        # Verify that trying to mark the deleted todo as complete fails
        complete_result = run_todo_command(["complete", str(original_id)])
        assert complete_result.returncode == 1
        assert "Todo with ID 1 does not exist" in complete_result.stderr
        
        # Verify that trying to delete the deleted todo again fails
        delete_result2 = run_todo_command(["delete", str(original_id)])
        assert delete_result2.returncode == 1
        assert "Todo with ID 1 does not exist" in delete_result2.stderr
    
    def test_delete_command_works_after_other_operations(self):
        """Test that the delete command works correctly after other operations."""
        # Add a few todos
        add_result1 = run_todo_command(["add", "Todo 1"])
        assert add_result1.returncode == 0
        add_result2 = run_todo_command(["add", "Todo 2"])
        assert add_result2.returncode == 0
        
        added_todo1 = json.loads(add_result1.stdout.strip())
        added_todo2 = json.loads(add_result2.stdout.strip())
        
        # Update one of them
        update_result = run_todo_command(["update", str(added_todo1['id']), "Updated Todo 1"])
        assert update_result.returncode == 0
        
        # Mark the other as complete
        complete_result = run_todo_command(["complete", str(added_todo2['id'])])
        assert complete_result.returncode == 0
        
        # Now delete the updated one
        delete_result = run_todo_command(["delete", str(added_todo1['id'])])
        assert delete_result.returncode == 0
        assert "deleted successfully" in delete_result.stdout
        
        # Verify the other todo still exists and retains its completion status
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        parsed_list = json.loads(list_result.stdout.strip())
        
        assert len(parsed_list) == 1
        assert parsed_list[0]['id'] == added_todo2['id']
        assert parsed_list[0]['completed'] is True