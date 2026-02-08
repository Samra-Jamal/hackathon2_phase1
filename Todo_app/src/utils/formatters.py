"""
JSON response formatter for the Todo application.
"""
import json
from typing import Any, List, Dict
from ..models.todo import Todo


def format_todo_response(todo: Todo) -> str:
    """
    Format a single Todo object as a JSON string.
    
    Args:
        todo (Todo): The Todo object to format
        
    Returns:
        str: JSON string representation of the Todo
    """
    return json.dumps(todo.to_dict())


def format_todos_response(todos: List[Todo]) -> str:
    """
    Format a list of Todo objects as a JSON string.
    
    Args:
        todos (List[Todo]): The list of Todo objects to format
        
    Returns:
        str: JSON string representation of the Todo list
    """
    return json.dumps([todo.to_dict() for todo in todos])


def format_success_response(data: Any = None, message: str = "") -> str:
    """
    Format a success response as a JSON string.
    
    Args:
        data (Any): Optional data to include in the response
        message (str): Optional message to include in the response
        
    Returns:
        str: JSON string representation of the success response
    """
    response = {
        "status": "success",
        "message": message
    }
    if data is not None:
        response["data"] = data
    return json.dumps(response)


def format_error_response(message: str, error_code: str = None) -> str:
    """
    Format an error response as a JSON string.
    
    Args:
        message (str): Error message
        error_code (str): Optional error code
        
    Returns:
        str: JSON string representation of the error response
    """
    response = {
        "status": "error",
        "message": message
    }
    if error_code:
        response["error_code"] = error_code
    return json.dumps(response)


def format_confirmation_response(message: str) -> str:
    """
    Format a confirmation response as a simple string.
    
    Args:
        message (str): Confirmation message
        
    Returns:
        str: Plain text confirmation message
    """
    return message