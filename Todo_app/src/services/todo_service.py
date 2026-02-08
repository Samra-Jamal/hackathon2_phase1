"""
Application service layer for the Todo application.
"""
import json
from typing import Union
from ..models.todo_collection import TodoCollection


class TodoService:
    """
    Service layer that handles business logic for todo operations.
    """
    
    def __init__(self):
        """
        Initialize the TodoService with a TodoCollection.
        """
        self.collection = TodoCollection()
    
    def add_todo(self, title: str) -> str:
        """
        Add a new todo with the given title.
        
        Args:
            title (str): The title of the new todo
            
        Returns:
            str: JSON string representation of the created todo
        """
        try:
            todo = self.collection.add_todo(title)
            return json.dumps(todo.to_dict())
        except ValueError as e:
            raise e  # Re-raise ValueError for validation issues
    
    def list_todos(self) -> str:
        """
        List all todos in the collection.
        
        Returns:
            str: JSON string representation of all todos
        """
        todos = self.collection.list_todos()
        return json.dumps([todo.to_dict() for todo in todos])
    
    def update_todo(self, id: int, title: str) -> str:
        """
        Update the title of an existing todo.
        
        Args:
            id (int): The ID of the todo to update
            title (str): The new title for the todo
            
        Returns:
            str: JSON string representation of the updated todo
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        
        todo = self.collection.update_todo(id, title)
        if todo is None:
            raise ValueError(f"Todo with ID {id} does not exist")
        
        return json.dumps(todo.to_dict())
    
    def complete_todo(self, id: int) -> str:
        """
        Mark a todo as completed.
        
        Args:
            id (int): The ID of the todo to mark as complete
            
        Returns:
            str: JSON string representation of the completed todo
        """
        todo = self.collection.complete_todo(id)
        if todo is None:
            raise ValueError(f"Todo with ID {id} does not exist")
        
        return json.dumps(todo.to_dict())
    
    def delete_todo(self, id: int) -> str:
        """
        Delete a todo from the collection.
        
        Args:
            id (int): The ID of the todo to delete
            
        Returns:
            str: Confirmation message
        """
        deleted = self.collection.delete_todo(id)
        if not deleted:
            raise ValueError(f"Todo with ID {id} does not exist")
        
        return f"Todo with ID {id} deleted successfully"