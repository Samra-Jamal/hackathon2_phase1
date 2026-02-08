# CLI API Contract: Todo In-Memory Console App

## Overview
This document defines the command-line interface contract for the Todo In-Memory Console Application. It specifies the commands, arguments, options, and expected behaviors.

## Command Structure
```
todo [command] [arguments...] [options...]
```

## Commands

### 1. Add Todo
**Command**: `todo add [TITLE]`

**Description**: Creates a new todo with the specified title.

**Arguments**:
- `TITLE` (required): The title of the new todo (string)

**Options**: None

**Success Response**:
- Status: 0 (success)
- Output: JSON representation of the created todo
```
{"id": 1, "title": "Sample task", "completed": false}
```

**Error Responses**:
- Status: 1 (error)
- Output: Error message if title is empty
```
Error: Title cannot be empty
```

### 2. List Todos
**Command**: `todo list`

**Description**: Displays all todos in the system.

**Arguments**: None

**Options**: None

**Success Response**:
- Status: 0 (success)
- Output: JSON array of all todos
```
[
  {"id": 1, "title": "Sample task", "completed": false},
  {"id": 2, "title": "Another task", "completed": true}
]
```

**Error Responses**: None (returns empty array if no todos exist)

### 3. Update Todo
**Command**: `todo update [ID] [NEW_TITLE]`

**Description**: Updates the title of an existing todo.

**Arguments**:
- `ID` (required): The ID of the todo to update (integer)
- `NEW_TITLE` (required): The new title for the todo (string)

**Options**: None

**Success Response**:
- Status: 0 (success)
- Output: JSON representation of the updated todo
```
{"id": 1, "title": "Updated task", "completed": false}
```

**Error Responses**:
- Status: 1 (error)
- Output: Error message if todo doesn't exist
```
Error: Todo with ID 1 does not exist
```
- Output: Error message if new title is empty
```
Error: Title cannot be empty
```

### 4. Complete Todo
**Command**: `todo complete [ID]`

**Description**: Marks a todo as completed.

**Arguments**:
- `ID` (required): The ID of the todo to mark as complete (integer)

**Options**: None

**Success Response**:
- Status: 0 (success)
- Output: JSON representation of the completed todo
```
{"id": 1, "title": "Sample task", "completed": true}
```

**Error Responses**:
- Status: 1 (error)
- Output: Error message if todo doesn't exist
```
Error: Todo with ID 1 does not exist
```

### 5. Delete Todo
**Command**: `todo delete [ID]`

**Description**: Removes a todo from the system.

**Arguments**:
- `ID` (required): The ID of the todo to delete (integer)

**Options**: None

**Success Response**:
- Status: 0 (success)
- Output: Confirmation message
```
Todo with ID 1 deleted successfully
```

**Error Responses**:
- Status: 1 (error)
- Output: Error message if todo doesn't exist
```
Error: Todo with ID 1 does not exist
```

## Global Options

### Help
**Option**: `-h, --help`

**Description**: Display help information for the application or specific command.

**Usage**:
- `todo --help`: Show general help
- `todo add --help`: Show help for add command

## Error Handling

### Standard Error Format
All error messages follow the format:
```
Error: [DETAILED_ERROR_MESSAGE]
```

### Exit Codes
- `0`: Success
- `1`: General error (validation, not found, etc.)
- `2`: Command-line argument error (missing arguments, invalid format, etc.)

## Data Formats

### Input Validation
- ID: Positive integer only
- Title: Non-empty string (after trimming whitespace)

### Output Format
- All successful outputs are in valid JSON format
- Error messages are plain text with "Error:" prefix

## Examples

### Adding a Todo
```
$ todo add "Buy groceries"
{"id": 1, "title": "Buy groceries", "completed": false}
```

### Listing Todos
```
$ todo list
[
  {"id": 1, "title": "Buy groceries", "completed": false},
  {"id": 2, "title": "Walk the dog", "completed": true}
]
```

### Updating a Todo
```
$ todo update 1 "Buy groceries and cook dinner"
{"id": 1, "title": "Buy groceries and cook dinner", "completed": false}
```

### Completing a Todo
```
$ todo complete 1
{"id": 1, "title": "Buy groceries and cook dinner", "completed": true}
```

### Deleting a Todo
```
$ todo delete 2
Todo with ID 2 deleted successfully
```