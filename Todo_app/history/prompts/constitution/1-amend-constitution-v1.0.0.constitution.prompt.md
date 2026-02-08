---
id: 1
title: Amend Constitution v1.0.0
stage: constitution
date: 2026-02-08
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: Jamal
command: /sp.constitution
labels: [constitution, governance, todo-app]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
---

## Prompt

```text
# Phase 1 Constitution – Todo App (WHY)

## Purpose
This project follows *Spec-Driven Development (SDD)* using *Claude Code + Spec-Kit Plus*.
No code may be written unless explicitly authorized by the specification.

---

## Non-Negotiable Principles

### 1. Spec Is the Single Source of Truth
- No implementation is allowed without a corresponding requirement in the specification.
- If a requirement is missing, it must be added to the spec before coding.

### 2. Phase-1 Scope Is Strictly Limited
Only the following are allowed in Phase-1:
- In-memory data storage
- Console / local execution
- Single-user usage
- No databases
- No authentication
- No networking requirements beyond local execution

Anything outside this scope is forbidden.

---

### 3. Technology Constraints
- Language: *Python 3.13+*
- Environment: *Local execution only*
- Frameworks: Standard Python libraries only
- No external databases
- No web frameworks

---

### 4. Data Rules
- All todo data must exist *only in memory*
- Data persistence across runs is not required
- Each todo must have:
  - A unique ID
  - A non-empty title
  - A completion status

---

### 5. Code Quality Rules
- Code must be readable and modular
- Business logic must be separated from input/output
- No hard-coded data except defaults
- Errors must be handled gracefully

---

### 6. Agent Behavior Rules
AI agents (Claude or others) must:
- Never write code without an approved spec
- Never invent features
- Never expand scope beyond Phase-1
- Stop and request clarification if requirements are unclear

---

### 7. Phase Transition Rule
Phase-1 must be *fully complete and correct* before starting Phase-2.
Incomplete Phase-1 invalidates later phases.

---

## Constitution Hierarchy
If conflicts arise:
*Constitution > Specification > Plan > Tasks > Code*

This constitution overrides all other documents.
```

## Response snapshot

Updated the project constitution with the Phase 1 Todo App principles, including:
- Spec as the single source of truth
- Phase-1 scope limitations
- Technology constraints
- Data rules
- Code quality rules
- Agent behavior rules
- Phase transition rule
- Governance structure with hierarchy

## Outcome

- ✅ Impact: Updated constitution document to version 1.0.0 with all required principles
- 🧪 Tests: No tests needed for this configuration file
- 📁 Files: Modified .specify/memory/constitution.md with new constitution
- 🔁 Next prompts: Ready for spec development based on new constitution
- 🧠 Reflection: Successfully transformed template constitution into project-specific governance document

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin spec development