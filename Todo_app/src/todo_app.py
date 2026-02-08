#!/usr/bin/env python3
"""
Todo In-Memory Console Application

A command-line tool for managing todos in memory.
"""

import sys
from src.cli.parser import create_parser
from src.services.todo_service import TodoService


def main():
    """Main entry point for the application."""
    parser = create_parser()
    args = parser.parse_args()

    # Initialize the service
    service = TodoService()

    # Execute the appropriate command
    try:
        if args.command == 'add':
            result = service.add_todo(args.title)
            print(result)
        elif args.command == 'list':
            result = service.list_todos()
            print(result)
        elif args.command == 'update':
            result = service.update_todo(args.id, args.title)
            print(result)
        elif args.command == 'complete':
            result = service.complete_todo(args.id)
            print(result)
        elif args.command == 'delete':
            result = service.delete_todo(args.id)
            print(result)
        else:
            parser.print_help()
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()