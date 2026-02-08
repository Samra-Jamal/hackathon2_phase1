"""
Integration tests for the complete command in the Todo application.
"""
import subprocess
import sys
import json


def run_todo_command(args):
    """Helper function to run the todo command with given arguments."""
    cmd = [sys.executable, "src/todo_app.py"] + args
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result


class TestCompleteCommandIntegration:
    """Integration tests for the complete command."""
    
    def test_complete_existing_todo_succeeds(self):
        """Test that marking an existing todo as complete succeeds."""
        # Add a todo first
        add_result = run_todo_command(["add", "Test todo"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        
        # Verify it starts as incomplete
        assert added_todo['completed'] is False
        
        # Mark as complete
        complete_result = run_todo_command(["complete", str(added_todo['id'])])
        assert complete_result.returncode == 0
        completed_todo = json.loads(complete_result.stdout.strip())
        
        # Verify it's now complete
        assert completed_todo['id'] == added_todo['id']
        assert completed_todo['title'] == added_todo['title']
        assert completed_todo['completed'] is True
    
    def test_complete_nonexistent_todo_fails(self):
        """Test that marking a nonexistent todo as complete fails."""
        # Try to complete a todo with ID 999 (which shouldn't exist)
        complete_result = run_todo_command(["complete", "999"])
        
        # Verify the command failed
        assert complete_result.returncode == 1
        
        # Verify the error message
        assert "Error:" in complete_result.stderr
        assert "Todo with ID 999 does not exist" in complete_result.stderr
    
    def test_complete_command_updates_persistence(self):
        """Test that the complete command properly updates the persistent state."""
        # Add a todo first
        add_result = run_todo_command(["add", "Test todo"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        original_id = added_todo['id']
        
        # Mark as complete
        complete_result = run_todo_command(["complete", str(original_id)])
        assert complete_result.returncode == 0
        
        # List todos to verify the completion is persisted
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        parsed_list = json.loads(list_result.stdout.strip())
        
        # Find the completed todo
        found_todo = next((t for t in parsed_list if t['id'] == original_id), None)
        assert found_todo is not None
        assert found_todo['completed'] is True
    
    def test_complete_command_only_changes_completion_status(self):
        """Test that the complete command only changes the completion status."""
        # Add a todo first
        add_result = run_todo_command(["add", "Original title"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        original_id = added_todo['id']
        
        # Mark as complete
        complete_result = run_todo_command(["complete", str(original_id)])
        assert complete_result.returncode == 0
        completed_todo = json.loads(complete_result.stdout.strip())
        
        # Verify only the completion status changed
        assert completed_todo['id'] == original_id
        assert completed_todo['title'] == "Original title"
        assert completed_todo['completed'] is True  # Changed from False
    
    def test_complete_already_completed_todo_succeeds(self):
        """Test that marking an already completed todo as complete succeeds."""
        # Add a todo first
        add_result = run_todo_command(["add", "Test todo"])
        assert add_result.returncode == 0
        added_todo = json.loads(add_result.stdout.strip())
        original_id = added_todo['id']
        
        # Mark as complete first time
        complete_result1 = run_todo_command(["complete", str(original_id)])
        assert complete_result1.returncode == 0
        completed_todo1 = json.loads(complete_result1.stdout.strip())
        assert completed_todo1['completed'] is True
        
        # Mark as complete second time
        complete_result2 = run_todo_command(["complete", str(original_id)])
        assert complete_result2.returncode == 0
        completed_todo2 = json.loads(complete_result2.stdout.strip())
        
        # Verify it's still complete
        assert completed_todo2['id'] == original_id
        assert completed_todo2['title'] == added_todo['title']
        assert completed_todo2['completed'] is True
    
    def test_can_distinguish_completed_and_incomplete_todos(self):
        """Test that completed and incomplete todos can be distinguished."""
        # Add two todos
        add_result1 = run_todo_command(["add", "Incomplete todo"])
        assert add_result1.returncode == 0
        add_result2 = run_todo_command(["add", "Complete me"])
        assert add_result2.returncode == 0
        
        added_todo1 = json.loads(add_result1.stdout.strip())
        added_todo2 = json.loads(add_result2.stdout.strip())
        
        # Mark one as complete
        complete_result = run_todo_command(["complete", str(added_todo2['id'])])
        assert complete_result.returncode == 0
        
        # List todos
        list_result = run_todo_command(["list"])
        assert list_result.returncode == 0
        parsed_list = json.loads(list_result.stdout.strip())
        
        # Find both todos
        todo1 = next((t for t in parsed_list if t['id'] == added_todo1['id']), None)
        todo2 = next((t for t in parsed_list if t['id'] == added_todo2['id']), None)
        
        assert todo1 is not None
        assert todo2 is not None
        assert todo1['completed'] is False
        assert todo2['completed'] is True
    
    def test_complete_command_works_after_other_operations(self):
        """Test that the complete command works correctly after other operations."""
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
        
        # Now mark the updated one as complete
        complete_result = run_todo_command(["complete", str(added_todo1['id'])])
        assert complete_result.returncode == 0
        completed_todo = json.loads(complete_result.stdout.strip())
        
        # Verify the completion worked with the updated title
        assert completed_todo['id'] == added_todo1['id']
        assert completed_todo['title'] == "Updated Todo 1"
        assert completed_todo['completed'] is True