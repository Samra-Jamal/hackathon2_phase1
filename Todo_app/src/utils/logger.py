"""
Logging utilities for the Todo application.
"""
import logging
import sys
from pathlib import Path


def setup_logger(name: str, log_file: str = None, level: int = logging.INFO) -> logging.Logger:
    """
    Set up a logger with the specified name and configuration.
    
    Args:
        name (str): Name of the logger
        log_file (str): Optional file path to write logs to
        level (int): Logging level (default: INFO)
        
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Prevent adding multiple handlers if logger already exists
    if logger.handlers:
        return logger
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Optionally add file handler
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


# Create a default logger for the application
app_logger = setup_logger('todo_app')


def log_info(message: str):
    """Log an info message."""
    app_logger.info(message)


def log_warning(message: str):
    """Log a warning message."""
    app_logger.warning(message)


def log_error(message: str):
    """Log an error message."""
    app_logger.error(message)


def log_debug(message: str):
    """Log a debug message."""
    app_logger.debug(message)