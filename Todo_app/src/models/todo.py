"""
Todo model representing a single todo item.
"""


class Todo:
    """
    Represents a single todo item with an ID, title, and completion status.
    """
    
    def __init__(self, id: int, title: str, completed: bool = False):
        """
        Initialize a Todo object.
        
        Args:
            id (int): Unique identifier for the todo
            title (str): Description of the task
            completed (bool): Completion status, defaults to False
        """
        self.id = id
        self.title = title
        self.completed = completed
    
    def to_dict(self) -> dict:
        """
        Convert the Todo object to a dictionary representation.
        
        Returns:
            dict: Dictionary representation of the Todo
        """
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a Todo object from a dictionary.
        
        Args:
            data (dict): Dictionary containing todo data
            
        Returns:
            Todo: Todo object created from the dictionary
        """
        return cls(
            id=data['id'],
            title=data['title'],
            completed=data.get('completed', False)
        )
    
    def __repr__(self):
        """
        String representation of the Todo object.
        
        Returns:
            str: String representation
        """
        return f"Todo(id={self.id}, title='{self.title}', completed={self.completed})"
    
    def __eq__(self, other):
        """
        Compare two Todo objects for equality.
        
        Args:
            other: Another object to compare with
            
        Returns:
            bool: True if objects are equal, False otherwise
        """
        if not isinstance(other, Todo):
            return False
        return (
            self.id == other.id and
            self.title == other.title and
            self.completed == other.completed
        )