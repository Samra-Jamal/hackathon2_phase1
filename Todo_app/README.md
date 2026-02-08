# Todo In-Memory Console App

A command-line tool for managing todos in memory. This application supports creating, viewing, updating, deleting, and completing tasks via a simple CLI interface.

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The application can be run directly as a Python script:

```bash
python src/todo_app.py [command] [arguments...]
```

### Available Commands

#### Add a Todo
Add a new todo with the specified title:
```bash
python src/todo_app.py add "My new task"
```

#### List All Todos
View all todos in the system:
```bash
python src/todo_app.py list
```

#### Update a Todo
Change the title of an existing todo:
```bash
python src/todo_app.py update 1 "Updated task title"
```

#### Mark Todo as Complete
Mark a todo as completed:
```bash
python src/todo_app.py complete 1
```

#### Delete a Todo
Remove a todo from the system:
```bash
python src/todo_app.py delete 1
```

#### Get Help
Display help information:
```bash
python src/todo_app.py --help
python src/todo_app.py add --help
```

## Examples

### Complete Workflow Example
```bash
# Add a few todos
python src/todo_app.py add "Buy groceries"
python src/todo_app.py add "Walk the dog"
python src/todo_app.py add "Finish report"

# List all todos
python src/todo_app.py list

# Update a todo
python src/todo_app.py update 2 "Walk the cat"

# Mark a todo as complete
python src/todo_app.py complete 1

# Delete a todo
python src/todo_app.py delete 3

# List todos again to see changes
python src/todo_app.py list
```

## Expected Output Format

### Successful Operations
Most operations return JSON-formatted output:
```json
{"id": 1, "title": "Sample task", "completed": false}
```

### Error Messages
Error messages follow the format:
```
Error: Detailed error message
```

## Development

### Running Tests
If tests are available, run them with:
```bash
pytest
```