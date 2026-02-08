"""
Integration tests for the update command in the Todo application.
"""
import subprocess
import sys
import json


def run_todo_command(args):
    """Helper function to run the todo command with given arguments."""
    cmd = [sys.executable, "src/todo_app.py"] + args
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result


class TestUpdateCommandIntegration:
    """Integration tests for the update command."""
    
    def test_update_existing_todo_succeeds(self):
        """Test that updating an existing todo succeeds."""
        # Add a todo first
        add_result = run_todo_command(["add", "Original title"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        
        # Update the todo
        update_result = run_todo_command(["update", str(added_todo['id']), "Updated title"])
        assert update_result.returncode == 0
        updated_todo = json.loads(update_result.stdout.strip())
        
        # Verify the update worked
        assert updated_todo['id'] == added_todo['id']
        assert updated_todo['title'] == "Updated title"
        assert updated_todo['completed'] == added_todo['completed']  # Should remain unchanged
    
    def test_update_nonexistent_todo_fails(self):
        """Test that updating a nonexistent todo fails."""
        # Try to update a todo with ID 999 (which shouldn't exist)
        update_result = run_todo_command(["update", "999", "Updated title"])
        
        # Verify the command failed
        assert update_result.returncode == 1
        
        # Verify the error message
        assert "Error:" in update_result.stderr
        assert "Todo with ID 999 does not exist" in update_result.stderr
    
    def test_update_todo_with_empty_title_fails(self):
        """Test that updating a todo with an empty title fails."""
        # Add a todo first
        add_result = run_todo_command(["add", "Original title"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        
        # Try to update with empty title
        update_result = run_todo_command(["update", str(added_todo['id']), ""])
        
        # Verify the command failed
        assert update_result.returncode == 1
        
        # Verify the error message
        assert "Error:" in update_result.stderr
        assert "Title cannot be empty" in update_result.stderr
    
    def test_update_todo_with_whitespace_only_title_fails(self):
        """Test that updating a todo with whitespace-only title fails."""
        # Add a todo first
        add_result = run_todo_command(["add", "Original title"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        
        # Try to update with whitespace-only title
        update_result = run_todo_command(["update", str(added_todo['id']), "   "])
        
        # Verify the command failed
        assert update_result.returncode == 1
        
        # Verify the error message
        assert "Error:" in update_result.stderr
        assert "Title cannot be empty" in update_result.stderr
    
    def test_update_command_updates_persistence(self):
        """Test that the update command properly updates the persistent state."""
        # Add a todo first
        add_result = run_todo_command(["add", "Original title"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        original_id = added_todo['id']
        
        # Update the todo
        update_result = run_todo_command(["update", str(original_id), "Updated title"])
        assert update_result.returncode == 0
        
        # List todos to verify the update is persisted
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        parsed_list = json.loads(list_result.stdout.strip())
        
        # Find the updated todo
        found_todo = next((t for t in parsed_list if t['id'] == original_id), None)
        assert found_todo is not None
        assert found_todo['title'] == "Updated title"
    
    def test_update_command_only_changes_title(self):
        """Test that the update command only changes the title, leaving other fields unchanged."""
        # Add a todo first
        add_result = run_todo_command(["add", "Original title"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        original_id = added_todo['id']
        
        # Mark as complete to change the completion status
        complete_result = run_todo_command(["complete", str(original_id)])
        assert complete_result.returncode == 0
        
        # Update the todo
        update_result = run_todo_command(["update", str(original_id), "Updated title"])
        assert update_result.returncode == 0
        updated_todo = json.loads(update_result.stdout.strip())
        
        # Verify only the title changed
        assert updated_todo['id'] == original_id
        assert updated_todo['title'] == "Updated title"
        assert updated_todo['completed'] is True  # Should remain completed
    
    def test_update_command_strips_whitespace_from_title(self):
        """Test that the update command strips leading/trailing whitespace from the title."""
        # Add a todo first
        add_result = run_todo_command(["add", "Original title"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        original_id = added_todo['id']
        
        # Update the todo with whitespace around the title
        update_result = run_todo_command([
            "update", 
            str(original_id), 
            "  Updated title with spaces  "
        ])
        assert update_result.returncode == 0
        updated_todo = json.loads(update_result.stdout.strip())
        
        # Verify the title is properly stripped
        assert updated_todo['title'] == "Updated title with spaces"
    
    def test_update_command_works_with_special_characters(self):
        """Test that the update command works with special characters in the title."""
        # Add a todo first
        add_result = run_todo_command(["add", "Original title"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        original_id = added_todo['id']
        
        # Update the todo with special characters
        special_title = "Updated title with special chars: !@#$%^&*()"
        update_result = run_todo_command(["update", str(original_id), special_title])
        assert update_result.returncode == 0
        updated_todo = json.loads(update_result.stdout.strip())
        
        # Verify the title is preserved
        assert updated_todo['title'] == special_title