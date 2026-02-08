"""
Unit tests for foundational components of the Todo application.
"""
import pytest
from src.models.todo import Todo
from src.models.todo_collection import TodoCollection
from src.utils.validators import validate_non_empty_string, validate_positive_integer, validate_todo_title, validate_todo_id


class TestTodoModel:
    """Tests for the Todo model."""
    
    def test_todo_creation(self):
        """Test creating a Todo object."""
        todo = Todo(id=1, title="Test todo", completed=False)
        assert todo.id == 1
        assert todo.title == "Test todo"
        assert todo.completed is False
    
    def test_todo_creation_defaults(self):
        """Test creating a Todo object with default values."""
        todo = Todo(id=1, title="Test todo")
        assert todo.id == 1
        assert todo.title == "Test todo"
        assert todo.completed is False  # Default value
    
    def test_todo_to_dict(self):
        """Test converting a Todo object to a dictionary."""
        todo = Todo(id=1, title="Test todo", completed=True)
        expected_dict = {
            'id': 1,
            'title': 'Test todo',
            'completed': True
        }
        assert todo.to_dict() == expected_dict
    
    def test_todo_from_dict(self):
        """Test creating a Todo object from a dictionary."""
        data = {
            'id': 1,
            'title': 'Test todo',
            'completed': True
        }
        todo = Todo.from_dict(data)
        assert todo.id == 1
        assert todo.title == 'Test todo'
        assert todo.completed is True
    
    def test_todo_repr(self):
        """Test the string representation of a Todo object."""
        todo = Todo(id=1, title="Test todo", completed=True)
        expected_repr = "Todo(id=1, title='Test todo', completed=True)"
        assert repr(todo) == expected_repr
    
    def test_todo_equality(self):
        """Test equality comparison between Todo objects."""
        todo1 = Todo(id=1, title="Test todo", completed=True)
        todo2 = Todo(id=1, title="Test todo", completed=True)
        todo3 = Todo(id=2, title="Different todo", completed=False)
        
        assert todo1 == todo2
        assert todo1 != todo3


class TestTodoCollection:
    """Tests for the TodoCollection model."""
    
    def test_initial_state(self):
        """Test initial state of TodoCollection."""
        collection = TodoCollection()
        assert len(collection.todos) == 0
        assert collection.next_id == 1
    
    def test_add_todo(self):
        """Test adding a todo to the collection."""
        collection = TodoCollection()
        todo = collection.add_todo("Test todo")
        
        assert todo.id == 1
        assert todo.title == "Test todo"
        assert todo.completed is False
        assert len(collection.todos) == 1
        assert collection.next_id == 2
    
    def test_add_todo_with_empty_title_raises_error(self):
        """Test that adding a todo with an empty title raises an error."""
        collection = TodoCollection()
        with pytest.raises(ValueError, match="Title cannot be empty"):
            collection.add_todo("")
        
        with pytest.raises(ValueError, match="Title cannot be empty"):
            collection.add_todo("   ")  # Only whitespace
    
    def test_get_todo(self):
        """Test retrieving a todo by ID."""
        collection = TodoCollection()
        added_todo = collection.add_todo("Test todo")
        
        retrieved_todo = collection.get_todo(added_todo.id)
        assert retrieved_todo is not None
        assert retrieved_todo.id == added_todo.id
        assert retrieved_todo.title == added_todo.title
        assert retrieved_todo.completed == added_todo.completed
    
    def test_get_nonexistent_todo(self):
        """Test retrieving a non-existent todo."""
        collection = TodoCollection()
        retrieved_todo = collection.get_todo(999)
        assert retrieved_todo is None
    
    def test_list_todos(self):
        """Test listing all todos."""
        collection = TodoCollection()
        todo1 = collection.add_todo("First todo")
        todo2 = collection.add_todo("Second todo")
        
        todos = collection.list_todos()
        assert len(todos) == 2
        assert todo1 in todos
        assert todo2 in todos
    
    def test_update_todo(self):
        """Test updating a todo's title."""
        collection = TodoCollection()
        original_todo = collection.add_todo("Original title")
        
        updated_todo = collection.update_todo(original_todo.id, "Updated title")
        
        assert updated_todo is not None
        assert updated_todo.id == original_todo.id
        assert updated_todo.title == "Updated title"
        assert updated_todo.completed == original_todo.completed  # Should remain unchanged
    
    def test_update_nonexistent_todo(self):
        """Test updating a non-existent todo."""
        collection = TodoCollection()
        result = collection.update_todo(999, "Updated title")
        assert result is None
    
    def test_update_todo_with_empty_title_raises_error(self):
        """Test that updating a todo with an empty title raises an error."""
        collection = TodoCollection()
        original_todo = collection.add_todo("Original title")
        
        with pytest.raises(ValueError, match="Title cannot be empty"):
            collection.update_todo(original_todo.id, "")
        
        with pytest.raises(ValueError, match="Title cannot be empty"):
            collection.update_todo(original_todo.id, "   ")  # Only whitespace
    
    def test_complete_todo(self):
        """Test marking a todo as complete."""
        collection = TodoCollection()
        todo = collection.add_todo("Test todo")
        assert todo.completed is False
        
        completed_todo = collection.complete_todo(todo.id)
        assert completed_todo is not None
        assert completed_todo.completed is True
        # Verify the change is reflected in the collection
        retrieved_todo = collection.get_todo(todo.id)
        assert retrieved_todo.completed is True
    
    def test_complete_nonexistent_todo(self):
        """Test marking a non-existent todo as complete."""
        collection = TodoCollection()
        result = collection.complete_todo(999)
        assert result is None
    
    def test_delete_todo(self):
        """Test deleting a todo."""
        collection = TodoCollection()
        todo = collection.add_todo("Test todo")
        
        deleted = collection.delete_todo(todo.id)
        assert deleted is True
        assert len(collection.todos) == 0
        assert collection.get_todo(todo.id) is None
    
    def test_delete_nonexistent_todo(self):
        """Test deleting a non-existent todo."""
        collection = TodoCollection()
        deleted = collection.delete_todo(999)
        assert deleted is False


class TestValidators:
    """Tests for validation utilities."""
    
    def test_validate_non_empty_string(self):
        """Test validating a non-empty string."""
        result = validate_non_empty_string("Valid string", "Field")
        assert result == "Valid string"
    
    def test_validate_non_empty_string_strips_whitespace(self):
        """Test that validation strips leading/trailing whitespace."""
        result = validate_non_empty_string("  Valid string  ", "Field")
        assert result == "Valid string"
    
    def test_validate_non_empty_string_raises_error_for_empty(self):
        """Test that validation raises an error for an empty string."""
        with pytest.raises(ValueError, match="Field cannot be empty"):
            validate_non_empty_string("", "Field")
    
    def test_validate_non_empty_string_raises_error_for_whitespace_only(self):
        """Test that validation raises an error for a whitespace-only string."""
        with pytest.raises(ValueError, match="Field cannot be empty"):
            validate_non_empty_string("   ", "Field")
    
    def test_validate_positive_integer(self):
        """Test validating a positive integer."""
        result = validate_positive_integer(42, "Field")
        assert result == 42
    
    def test_validate_positive_integer_raises_error_for_negative(self):
        """Test that validation raises an error for a negative integer."""
        with pytest.raises(ValueError, match="Field must be a positive integer"):
            validate_positive_integer(-1, "Field")
    
    def test_validate_positive_integer_raises_error_for_zero(self):
        """Test that validation raises an error for zero."""
        with pytest.raises(ValueError, match="Field must be a positive integer"):
            validate_positive_integer(0, "Field")
    
    def test_validate_positive_integer_raises_error_for_non_integer(self):
        """Test that validation raises an error for a non-integer value."""
        with pytest.raises(ValueError, match="Field must be a positive integer"):
            validate_positive_integer(3.14, "Field")
        
        with pytest.raises(ValueError, match="Field must be a positive integer"):
            validate_positive_integer("42", "Field")
    
    def test_validate_todo_title(self):
        """Test validating a todo title."""
        result = validate_todo_title("Valid title")
        assert result == "Valid title"
    
    def test_validate_todo_title_strips_whitespace(self):
        """Test that title validation strips leading/trailing whitespace."""
        result = validate_todo_title("  Valid title  ")
        assert result == "Valid title"
    
    def test_validate_todo_title_raises_error_for_empty(self):
        """Test that title validation raises an error for an empty title."""
        with pytest.raises(ValueError, match="Title cannot be empty"):
            validate_todo_title("")
    
    def test_validate_todo_id(self):
        """Test validating a todo ID."""
        result = validate_todo_id(42)
        assert result == 42
    
    def test_validate_todo_id_raises_error_for_invalid_id(self):
        """Test that ID validation raises an error for invalid IDs."""
        with pytest.raises(ValueError, match="ID must be a positive integer"):
            validate_todo_id(-1)
        
        with pytest.raises(ValueError, match="ID must be a positive integer"):
            validate_todo_id(0)
        
        with pytest.raises(ValueError, match="ID must be a positive integer"):
            validate_todo_id("invalid")