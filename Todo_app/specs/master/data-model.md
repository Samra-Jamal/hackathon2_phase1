# Data Model: Todo In-Memory Console App

## Entity: Todo

### Fields
| Field | Type | Description | Validation |
|-------|------|-------------|------------|
| id | integer | Unique identifier for the todo | Auto-generated, must be unique |
| title | string | Short description of the task | Required, must not be empty |
| completed | boolean | Completion status of the task | Required, defaults to false |

### Relationships
- None (standalone entity)

### State Transitions
- `pending` → `completed`: When user marks the todo as complete
- `completed` → `pending`: Not supported (completed todos remain completed)

## In-Memory Data Structure

### Storage Schema
```python
todos: Dict[int, Todo] = {}
next_id: int = 1

class Todo:
    id: int
    title: str
    completed: bool
```

### Operations
- **CREATE**: Add new todo to the dictionary with auto-generated ID
- **READ**: Retrieve todo by ID from the dictionary
- **UPDATE**: Modify existing todo in the dictionary
- **DELETE**: Remove todo from the dictionary
- **LIST**: Return all todos in the dictionary

## Validation Rules

### Business Rules
1. **Unique ID**: Each todo must have a unique integer ID
2. **Non-empty Title**: Todo title must not be empty or contain only whitespace
3. **Default Status**: New todos must have `completed` set to `false`
4. **Existence Check**: Operations requiring an ID must verify the todo exists

### Error Conditions
1. **Invalid ID**: Attempting operations on non-existent todo ID
2. **Empty Title**: Providing empty or whitespace-only title during creation/update
3. **Type Mismatch**: Providing incorrect data types for fields

## Sample Data Representation

### Example Todo Object
```json
{
  "id": 1,
  "title": "Buy groceries",
  "completed": false
}
```

### In-Memory Storage Example
```python
{
  1: {
    "id": 1,
    "title": "Buy groceries",
    "completed": false
  },
  2: {
    "id": 2,
    "title": "Walk the dog",
    "completed": true
  }
}
```