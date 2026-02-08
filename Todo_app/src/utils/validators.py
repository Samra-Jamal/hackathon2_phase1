"""
Validation utilities for the Todo application.
"""
import re
from typing import Any


def validate_non_empty_string(value: str, field_name: str = "Value") -> str:
    """
    Validate that a string is not empty or contains only whitespace.
    
    Args:
        value (str): The string value to validate
        field_name (str): The name of the field being validated (for error messages)
        
    Returns:
        str: The validated string with leading/trailing whitespace stripped
        
    Raises:
        ValueError: If the string is empty or contains only whitespace
    """
    if not value or not value.strip():
        raise ValueError(f"{field_name} cannot be empty")
    
    return value.strip()


def validate_positive_integer(value: Any, field_name: str = "Value") -> int:
    """
    Validate that a value is a positive integer.
    
    Args:
        value (Any): The value to validate
        field_name (str): The name of the field being validated (for error messages)
        
    Returns:
        int: The validated positive integer
        
    Raises:
        ValueError: If the value is not a positive integer
    """
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field_name} must be a positive integer")
    
    return value


def validate_todo_title(title: str) -> str:
    """
    Validate a todo title according to business rules.
    
    Args:
        title (str): The title to validate
        
    Returns:
        str: The validated title with leading/trailing whitespace stripped
        
    Raises:
        ValueError: If the title is empty or contains only whitespace
    """
    return validate_non_empty_string(title, "Title")


def validate_todo_id(todo_id: Any) -> int:
    """
    Validate a todo ID according to business rules.
    
    Args:
        todo_id (Any): The ID to validate
        
    Returns:
        int: The validated ID
        
    Raises:
        ValueError: If the ID is not a positive integer
    """
    return validate_positive_integer(todo_id, "ID")


def sanitize_input(input_str: str) -> str:
    """
    Sanitize user input by removing potentially harmful characters.
    
    Args:
        input_str (str): The input string to sanitize
        
    Returns:
        str: The sanitized string
    """
    # Remove null bytes and other potentially problematic characters
    sanitized = input_str.replace('\x00', '')
    
    # Strip leading/trailing whitespace
    return sanitized.strip()