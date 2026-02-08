# Data Model: Todo In-Memory Console App

**Feature**: Todo In-Memory Console App
**Date**: 2026-02-08
**Related Plan**: specs/todo-app/plan.md

## Todo Entity

### Fields
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | integer | Unique, auto-generated | Unique identifier for each todo |
| title | string | Non-empty | Short description of the task |
| completed | boolean | None | Completion status (true = completed, false = pending) |

### Validation Rules
- `id`: Automatically assigned, must be unique within the collection
- `title`: Must be a non-empty string (length > 0)
- `completed`: Boolean value, defaults to False when creating a new todo

### State Transitions
- **Initial State**: `completed = False` (when todo is created)
- **Transition 1**: `completed = False` → `completed = True` (when marked complete)
- **Transition 2**: `completed = True` → `completed = False` (when marked incomplete, if feature is implemented)

## Todo Collection

### Operations
- **Create**: Add a new todo with unique ID and non-empty title
- **Read**: Retrieve all todos or a specific todo by ID
- **Update**: Modify the title of an existing todo
- **Complete**: Change the completion status of an existing todo
- **Delete**: Remove a todo from the collection

### Constraints
- All operations must validate that referenced todos exist before modifying
- All operations must validate input parameters before execution
- Title updates must not be empty strings
- Operations must return appropriate errors when todos don't exist