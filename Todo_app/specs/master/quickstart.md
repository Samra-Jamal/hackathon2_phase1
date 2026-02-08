# Quickstart Guide: Todo In-Memory Console App

## Prerequisites
- Python 3.11 or higher
- pip (Python package installer)

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```
   (Note: This project may not have a requirements.txt if using only built-in Python libraries)

## Usage

### Running the Application
The application can be run directly as a Python script:

```bash
python todo.py [command] [arguments...]
```

Or if the script has been made executable:
```bash
./todo.py [command] [arguments...]
```

### Available Commands

#### Add a Todo
Add a new todo with the specified title:
```bash
python todo.py add "My new task"
```

#### List All Todos
View all todos in the system:
```bash
python todo.py list
```

#### Update a Todo
Change the title of an existing todo:
```bash
python todo.py update 1 "Updated task title"
```

#### Mark Todo as Complete
Mark a todo as completed:
```bash
python todo.py complete 1
```

#### Delete a Todo
Remove a todo from the system:
```bash
python todo.py delete 1
```

#### Get Help
Display help information:
```bash
python todo.py --help
python todo.py add --help
```

## Examples

### Complete Workflow Example
```bash
# Add a few todos
python todo.py add "Buy groceries"
python todo.py add "Walk the dog"
python todo.py add "Finish report"

# List all todos
python todo.py list

# Update a todo
python todo.py update 2 "Walk the cat"

# Mark a todo as complete
python todo.py complete 1

# Delete a todo
python todo.py delete 3

# List todos again to see changes
python todo.py list
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

## Troubleshooting

### Common Issues

1. **Command not found**: Ensure you're running the command from the correct directory where `todo.py` is located.

2. **Permission denied**: On Unix-like systems, you may need to make the file executable:
   ```bash
   chmod +x todo.py
   ```

3. **Python version**: Ensure you're using Python 3.11 or higher:
   ```bash
   python --version
   ```

4. **Missing arguments**: Each command expects specific arguments. Use `--help` to see the correct usage.

## Development

### Running Tests
If tests are available, run them with:
```bash
pytest
```

### Project Structure
```
todo.py                 # Main application file
tests/                  # Test files
specs/                  # Specification documents
  └── todo-app/
      ├── spec.md       # Feature specification
      ├── research.md   # Research findings
      ├── data-model.md # Data model
      └── contracts/    # API contracts
```