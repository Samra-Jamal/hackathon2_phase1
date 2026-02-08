---
id: 2
title: Create Todo Console Spec
stage: spec
date: 2026-02-08
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-console
branch: 1-todo-console
user: Jamal
command: /sp.specify
labels: [specification, todo-app, console-app]
links:
  spec: ../specs/todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/todo-app/spec.md
  - specs/todo-app/checklists/requirements.md
tests:
---

## Prompt

```text
# Phase 1 Specification – Todo In-Memory Console App

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
- File storage
```

## Response snapshot

Created the specification document for the Todo In-Memory Console App based on the provided requirements. The specification includes:

- Five prioritized user stories covering all required functionality (add, view, update, complete, delete)
- Functional requirements that map to the specified user journeys
- Key entities (Todo and Todo Collection)
- Success criteria that are measurable and technology-agnostic
- Edge cases to consider during implementation
- A quality checklist that validates the specification completeness

## Outcome

- ✅ Impact: Complete specification created with all required sections
- 🧪 Tests: Quality checklist confirms spec meets standards
- 📁 Files: Created spec.md and requirements.md checklist
- 🔁 Next prompts: Ready for planning phase with /sp.plan
- 🧠 Reflection: Spec captures all Phase 1 requirements without implementation details

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All checklist items passed
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin planning phase