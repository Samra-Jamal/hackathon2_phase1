"""
TodoCollection model representing the in-memory storage for todos.
"""
from typing import Dict, List, Optional
from .todo import Todo


class TodoCollection:
    """
    Represents the in-memory storage container holding all todos with methods for CRUD operations.
    """
    
    def __init__(self):
        """
        Initialize an empty TodoCollection with an auto-incrementing ID counter.
        """
        self.todos: Dict[int, Todo] = {}
        self.next_id: int = 1
    
    def add_todo(self, title: str) -> Todo:
        """
        Add a new todo with the given title.
        
        Args:
            title (str): The title of the new todo
            
        Returns:
            Todo: The newly created Todo object
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        
        todo = Todo(id=self.next_id, title=title.strip())
        self.todos[self.next_id] = todo
        self.next_id += 1
        return todo
    
    def get_todo(self, id: int) -> Optional[Todo]:
        """
        Retrieve a todo by its ID.
        
        Args:
            id (int): The ID of the todo to retrieve
            
        Returns:
            Optional[Todo]: The Todo object if found, None otherwise
        """
        return self.todos.get(id)
    
    def list_todos(self) -> List[Todo]:
        """
        Retrieve all todos.
        
        Returns:
            List[Todo]: A list of all Todo objects
        """
        return list(self.todos.values())
    
    def update_todo(self, id: int, new_title: str) -> Optional[Todo]:
        """
        Update the title of an existing todo.
        
        Args:
            id (int): The ID of the todo to update
            new_title (str): The new title for the todo
            
        Returns:
            Optional[Todo]: The updated Todo object if successful, None if todo doesn't exist
        """
        if not new_title or not new_title.strip():
            raise ValueError("Title cannot be empty")
        
        if id not in self.todos:
            return None
        
        todo = self.todos[id]
        todo.title = new_title.strip()
        return todo
    
    def complete_todo(self, id: int) -> Optional[Todo]:
        """
        Mark a todo as completed.
        
        Args:
            id (int): The ID of the todo to mark as complete
            
        Returns:
            Optional[Todo]: The updated Todo object if successful, None if todo doesn't exist
        """
        if id not in self.todos:
            return None
        
        todo = self.todos[id]
        todo.completed = True
        return todo
    
    def delete_todo(self, id: int) -> bool:
        """
        Remove a todo from the collection.
        
        Args:
            id (int): The ID of the todo to delete
            
        Returns:
            bool: True if the todo was deleted, False if it didn't exist
        """
        if id not in self.todos:
            return False
        
        del self.todos[id]
        return True