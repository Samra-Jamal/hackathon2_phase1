---
ID: 1
TITLE: Update constitution
STAGE: constitution
DATE_ISO: 2026-02-07
SURFACE: agent
MODEL: claude-sonnet-4-5-20250929
FEATURE: none
BRANCH: master
USER: Jamal
COMMAND: .specify/scripts/bash/create-phr.sh --title "Update constitution" --stage constitution --json
LABELS:
  - constitution
  - docs
LINKS:
  SPEC/TICKET/ADR/PR: null
FILES_YAML:
  - .specify/memory/constitution.md
TESTS_YAML:
  - None
PROMPT_TEXT: |
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
RESPONSE_TEXT: |
  # Sync Impact Report
  <!--
  Version change: null → 1.0.0
  List of modified principles:
  - None
  Added sections:
  - None
  Removed sections:
  - None
  Templates requiring updates:
  - ⚠ pending: .specify/templates/plan-template.md
  - ⚠ pending: .specify/templates/spec-template.md
  - ⚠ pending: .specify/templates/tasks-template.md
  - ⚠ pending: .specify/commands/sp.adr.md
  - ⚠ pending: .specify/commands/sp.analyze.md
  - ⚠ pending: .specify/commands/sp.checklist.md
  - ⚠ pending: .specify/commands/sp.clarify.md
  - ⚠ pending: .specify/commands/sp.constitution.md
  - ⚠ pending: .specify/commands/sp.git.commit_pr.md
  - ⚠ pending: .specify/commands/sp.implement.md
  - ⚠ pending: .specify/commands/sp.phr.md
  - ⚠ pending: .specify/commands/sp.plan.md
  - ⚠ pending: .specify/commands/sp.reverse-engineer.md
  - ⚠ pending: .specify/commands/sp.specify.md
  - ⚠ pending: .specify/commands/sp.tasks.md
  - ⚠ pending: .specify/templates/phr-template.prompt.md
  - ⚠ pending: README.md
  Follow-up TODOs:
  - None
  -->
  # Todo App Constitution

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

  ## Governance
  Amendments require documentation, approval, and a migration plan. All PRs/reviews must verify compliance. Use `docs/development-guidance.md` for runtime development guidance.

  **Version**: 1.0.0 | **Ratified**: 2026-02-07 | **Last Amended**: 2026-02-07
