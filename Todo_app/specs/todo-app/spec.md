# Feature Specification: Todo In-Memory Console App

**Feature Branch**: `1-todo-console`
**Created**: 2026-02-08
**Status**: Draft
**Input**: User description: "# Phase 1 Specification – Todo In-Memory Console App

## Overview
Phase-1 implements a basic Todo application that runs locally and stores all data in memory.
The application supports creating, viewing, updating, deleting, and completing tasks.

---

## Domain Entity: Todo

### Todo Fields
| Field | Type | Description |
|-----|------|-------------|
| id | integer | Unique identifier |
| title | string | Short description of the task |
| completed | boolean | Completion status |

---

## User Journeys

### Journey 1: Add a Todo
*As a user*,
I want to add a new todo,
So that I can track something I need to do.

*Input*
- title (string)

*Rules*
- Title must not be empty
- ID must be unique
- completed defaults to false

*Output*
- Newly created todo

---

### Journey 2: View All Todos
*As a user*,
I want to see all my todos,
So that I can review my tasks.

*Output*
- List of all todos
- Each todo shows:
  - id
  - title
  - completed status

---

### Journey 3: Update a Todo
*As a user*,
I want to update an existing todo,
So that I can correct or change it.

*Input*
- id
- new title

*Rules*
- Todo must exist
- New title must not be empty

*Output*
- Updated todo

---

### Journey 4: Mark Todo as Complete
*As a user*,
I want to mark a todo as completed,
So that I know it is done.

*Input*
- id

*Rules*
- Todo must exist

*Effect*
- completed becomes true

---

### Journey 5: Delete a Todo
*As a user*,
I want to delete a todo,
So that I can remove tasks I no longer need.

*Input*
- id

*Rules*
- Todo must exist

*Effect*
- Todo is removed from memory

---

## Error Handling Rules
- If a todo ID does not exist → return a clear error
- If title is empty → return a validation error
- Application must not crash on invalid input

---

## Acceptance Criteria

✔ User can add a todo
✔ User can list todos
✔ User can update a todo
✔ User can delete a todo
✔ User can mark a todo complete
✔ Data is stored only in memory
✔ No extra features beyond Phase-1

---

## Explicitly Out of Scope
- Authentication
- Databases
- Web UI
- APIs
- Multi-user support
- File storage"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add Todo (Priority: P1)

As a user, I want to add a new todo so that I can track something I need to do. This functionality forms the core of the todo application - without being able to create todos, other features are meaningless.

**Why this priority**: This is foundational functionality - users must be able to create todos to use the application effectively. Without this, there's nothing to view, update, or delete.

**Independent Test**: Can be fully tested by adding various todo titles and verifying they appear in the list. Delivers core value of allowing task capture.

**Acceptance Scenarios**:

1. **Given** user wants to add a new task, **When** user provides a non-empty title, **Then** a new todo with a unique ID is created with completed status as false
2. **Given** user attempts to add a todo with an empty title, **When** user submits the form, **Then** a validation error is returned and no todo is created

---

### User Story 2 - View All Todos (Priority: P1)

As a user, I want to see all my todos so that I can review my tasks. This allows users to see what they've captured and manage their tasks.

**Why this priority**: Essential for utility - users need to see their todos to know what they have to do. Without viewing, adding todos is pointless.

**Independent Test**: Can be fully tested by adding some todos and then listing them. Delivers value of task visibility and overview.

**Acceptance Scenarios**:

1. **Given** user has multiple todos in the system, **When** user requests to view all todos, **Then** all todos are displayed showing their ID, title, and completion status
2. **Given** user has no todos in the system, **When** user requests to view all todos, **Then** an empty list is displayed

---

### User Story 3 - Update Todo (Priority: P2)

As a user, I want to update an existing todo so that I can correct or change it. This allows for maintenance of accurate task information.

**Why this priority**: Enhances usability by allowing corrections to typos or changes to task details without requiring deletion and recreation.

**Independent Test**: Can be fully tested by creating a todo, updating its title, and verifying the change. Delivers value of maintaining accurate task information.

**Acceptance Scenarios**:

1. **Given** a valid todo exists, **When** user updates the title with a non-empty value, **Then** the todo's title is updated and all other properties remain unchanged
2. **Given** user attempts to update a non-existent todo, **When** user provides ID of missing todo, **Then** a clear error message is returned and no changes are made

---

### User Story 4 - Mark Todo Complete (Priority: P2)

As a user, I want to mark a todo as completed so that I know it is done. This allows tracking of progress and task completion status.

**Why this priority**: Critical for the todo concept - distinguishing between completed and pending tasks is essential functionality.

**Independent Test**: Can be fully tested by creating a todo, marking it complete, and verifying its status changes. Delivers value of progress tracking.

**Acceptance Scenarios**:

1. **Given** a pending todo exists, **When** user marks it as complete, **Then** the todo's completion status becomes true
2. **Given** user attempts to mark a non-existent todo as complete, **When** user provides ID of missing todo, **Then** a clear error message is returned and no changes are made

---

### User Story 5 - Delete Todo (Priority: P3)

As a user, I want to delete a todo so that I can remove tasks I no longer need. This helps maintain a clean, manageable list of active tasks.

**Why this priority**: Improves organization and prevents clutter with outdated or irrelevant tasks, though lower priority than basic CRUD operations.

**Independent Test**: Can be fully tested by creating a todo, deleting it, and verifying it no longer appears in the list. Delivers value of list organization.

**Acceptance Scenarios**:

1. **Given** a valid todo exists, **When** user requests to delete the todo, **Then** the todo is removed from the system
2. **Given** user attempts to delete a non-existent todo, **When** user provides ID of missing todo, **Then** a clear error message is returned and no changes are made

---

### Edge Cases

- What happens when the application receives malformed input?
- How does the system handle attempts to create todos with very long titles?
- What occurs when trying to perform operations with extremely large integer IDs?
- How does the system respond to rapid consecutive operations?
- What happens if the memory storage reaches capacity limits?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add a new todo with a non-empty title
- **FR-002**: System MUST assign a unique ID to each newly created todo
- **FR-003**: System MUST set the completed status to false by default when creating a new todo
- **FR-004**: System MUST display all existing todos showing their ID, title, and completion status
- **FR-005**: System MUST allow users to update an existing todo's title with a non-empty value
- **FR-006**: System MUST allow users to mark an existing todo as completed
- **FR-007**: System MUST allow users to delete an existing todo from the system
- **FR-008**: System MUST return a clear error message when attempting to update/delete a non-existent todo
- **FR-009**: System MUST return a validation error when attempting to create/update with an empty title
- **FR-010**: System MUST prevent crashes when handling invalid input or operations
- **FR-011**: System MUST store all todo data only in memory (no persistent storage)
- **FR-012**: System MUST ensure all todo IDs are integers and unique within the application

### Key Entities *(include if feature involves data)*

- **Todo**: Represents a task that needs to be tracked, with an integer ID, string title, and boolean completion status
- **Todo Collection**: Represents the in-memory storage container holding all todos with methods for CRUD operations

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully add, view, update, delete, and mark todos complete in a console application
- **SC-002**: Application operates without crashing when handling all valid user operations and returns appropriate error messages for invalid operations
- **SC-003**: All todo data remains only in memory and is not persisted to disk or external storage
- **SC-004**: Users can perform all basic todo operations without authentication requirements
- **SC-005**: The application supports single-user usage with no multi-user features implemented