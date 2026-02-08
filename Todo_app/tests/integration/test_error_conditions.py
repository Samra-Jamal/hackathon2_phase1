"""
Integration tests covering error conditions for the Todo application.
"""
import subprocess
import sys
import json


def run_todo_command(args):
    """Helper function to run the todo command with given arguments."""
    cmd = [sys.executable, "src/todo_app.py"] + args
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result


class TestErrorConditions:
    """Integration tests for error conditions."""
    
    def test_add_command_with_no_arguments_shows_help(self):
        """Test that the add command with no arguments shows appropriate help/error."""
        result = run_todo_command(["add"])
        
        # Should fail since title is required
        assert result.returncode != 0
    
    def test_update_command_with_invalid_id_fails(self):
        """Test that the update command with an invalid ID fails appropriately."""
        result = run_todo_command(["update", "abc", "New title"])
        
        # Should fail since ID must be an integer
        assert result.returncode != 0
    
    def test_complete_command_with_invalid_id_fails(self):
        """Test that the complete command with an invalid ID fails appropriately."""
        result = run_todo_command(["complete", "abc"])
        
        # Should fail since ID must be an integer
        assert result.returncode != 0
    
    def test_delete_command_with_invalid_id_fails(self):
        """Test that the delete command with an invalid ID fails appropriately."""
        result = run_todo_command(["delete", "abc"])
        
        # Should fail since ID must be an integer
        assert result.returncode != 0
    
    def test_update_command_with_negative_id_fails(self):
        """Test that the update command with a negative ID fails appropriately."""
        result = run_todo_command(["update", "-1", "New title"])
        
        # Should fail since ID must be positive
        assert result.returncode != 0
    
    def test_complete_command_with_negative_id_fails(self):
        """Test that the complete command with a negative ID fails appropriately."""
        result = run_todo_command(["complete", "-1"])
        
        # Should fail since ID must be positive
        assert result.returncode != 0
    
    def test_delete_command_with_negative_id_fails(self):
        """Test that the delete command with a negative ID fails appropriately."""
        result = run_todo_command(["delete", "-1"])
        
        # Should fail since ID must be positive
        assert result.returncode != 0
    
    def test_multiple_errors_in_sequence(self):
        """Test that multiple error conditions can be handled in sequence."""
        # Try to complete a non-existent todo
        result1 = run_todo_command(["complete", "999"])
        assert result1.returncode == 1
        assert "does not exist" in result1.stderr
        
        # Add a valid todo
        result2 = run_todo_command(["add", "Valid todo"])
        assert result2.returncode == 0
        added_todo = json.loads(result2.stdout.strip())
        
        # Try to update with empty title
        result3 = run_todo_command(["update", str(added_todo['id']), ""])
        assert result3.returncode == 1
        assert "Title cannot be empty" in result3.stderr
        
        # Verify the todo still exists and is unchanged
        result4 = run_todo_command(["list"])
        assert result4.returncode == 0
        parsed_list = json.loads(result4.stdout.strip())
        assert len(parsed_list) == 1
        assert parsed_list[0]['id'] == added_todo['id']
        assert parsed_list[0]['title'] == "Valid todo"
    
    def test_invalid_command_shows_help(self):
        """Test that an invalid command shows help."""
        result = run_todo_command(["invalidcommand"])
        
        # Should fail since command doesn't exist
        assert result.returncode != 0
    
    def test_malformed_input_handling(self):
        """Test handling of various malformed inputs."""
        # Add a todo
        add_result = run_todo_command(["add", "Test todo"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        
        # Try to update with special characters that could be problematic
        special_chars = "Title with \x00 null byte"
        update_result = run_todo_command(["update", str(added_todo['id']), special_chars])
        assert update_result.returncode == 0  # Should succeed after sanitization
        
        # Verify the sanitized result
        updated_todo = json.loads(update_result.stdout.strip())
        # Null byte should be removed
        assert '\x00' not in updated_todo['title']
    
    def test_long_title_handling(self):
        """Test handling of very long titles."""
        # Create a very long title
        long_title = "A" * 10000  # 10,000 character title
        
        result = run_todo_command(["add", long_title])
        # This should succeed, though implementation might have limits
        # For our implementation, it should work as long as memory permits
        assert result.returncode == 0
        
        parsed_result = json.loads(result.stdout.strip())
        assert parsed_result['title'] == long_title