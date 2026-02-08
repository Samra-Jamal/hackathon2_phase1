"""
Error handling utilities for the Todo application.
"""


class TodoError(Exception):
    """
    Base exception class for todo-related errors.
    """
    pass


class ValidationError(TodoError):
    """
    Exception raised for validation errors.
    """
    pass


class NotFoundError(TodoError):
    """
    Exception raised when a requested todo is not found.
    """
    pass


class DuplicateError(TodoError):
    """
    Exception raised when trying to create a duplicate todo.
    """
    pass