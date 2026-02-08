"""
CLI argument parser for the Todo application.
"""
import argparse


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser for the Todo CLI application.
    
    Returns:
        argparse.ArgumentParser: Configured argument parser
    """
    parser = argparse.ArgumentParser(
        prog='todo',
        description='A command-line tool for managing todos in memory.',
        epilog='Example: todo add "Buy groceries"'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new todo')
    add_parser.add_argument('title', type=str, help='Title of the new todo')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all todos')
    
    # Update command
    update_parser = subparsers.add_parser('update', help='Update an existing todo')
    update_parser.add_argument('id', type=int, help='ID of the todo to update')
    update_parser.add_argument('title', type=str, help='New title for the todo')
    
    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark a todo as complete')
    complete_parser.add_argument('id', type=int, help='ID of the todo to mark complete')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a todo')
    delete_parser.add_argument('id', type=int, help='ID of the todo to delete')
    
    return parser