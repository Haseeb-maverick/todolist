---
description: "Task list for Phase I – In-Memory Console-Based Todo App"
---

# Tasks: Phase I – In-Memory Console-Based Todo App

**Input**: Design documents from `/specs/001-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan in todo_app/
- [ ] T002 [P] Create domain/ directory and initialize as Python package with empty __init__.py
- [ ] T003 [P] Create store/ directory and initialize as Python package with empty __init__.py
- [ ] T004 [P] Create commands/ directory and initialize as Python package with empty __init__.py
- [ ] T005 [P] Create cli/ directory and initialize as Python package with empty __init__.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 Create Todo entity class in todo_app/domain/todo.py with id, title, description, status, priority attributes
- [X] T007 [P] Implement Todo validation rules in todo_app/domain/todo.py (title/description length, status values, etc.)
- [X] T008 Create TodoStore class in todo_app/store/todo_store.py with in-memory storage structure
- [X] T009 [P] Implement TodoStore CRUD operations (add, get, update, delete) in todo_app/store/todo_store.py
- [X] T010 [P] Implement TodoStore list operations (list_all, list_by_status) in todo_app/store/todo_store.py
- [X] T011 [P] Implement TodoStore status operations (mark_complete, mark_incomplete) in todo_app/store/todo_store.py
- [X] T012 Create main.py with basic application structure and TodoStore initialization

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Todo (Priority: P1) 🎯 MVP

**Goal**: Enable users to create new todo items with required information through console interface

**Independent Test**: Can be fully tested by entering "add" command with title and description, then verifying the todo appears in the list. Delivers core value of being able to capture tasks.

### Implementation for User Story 1

- [X] T013 [P] [US1] Create add command handler in todo_app/commands/add.py
- [X] T014 [US1] Implement input validation for add command in todo_app/commands/add.py (title/description non-empty)
- [X] T015 [US1] Implement error handling for invalid inputs in todo_app/commands/add.py
- [X] T016 [US1] Create console interface for add command in todo_app/cli/console.py
- [X] T017 [US1] Integrate add command with main.py application flow

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todos (Priority: P1)

**Goal**: Allow users to see their list of todos in readable console format with filtering options

**Independent Test**: Can be fully tested by adding several todos, then using view commands to display them. Delivers core value of being able to see and track tasks.

### Implementation for User Story 2

- [X] T018 [P] [US2] Create view command handler in todo_app/commands/view.py
- [X] T019 [US2] Implement view all todos functionality in todo_app/commands/view.py
- [X] T020 [US2] Implement view by status functionality (completed/incomplete) in todo_app/commands/view.py
- [X] T021 [US2] Create console interface for view command in todo_app/cli/console.py
- [X] T022 [US2] Format output display for todos in readable console format in todo_app/cli/console.py
- [X] T023 [US2] Integrate view command with main.py application flow

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Todo (Priority: P2)

**Goal**: Allow users to modify an existing todo's title, description, or priority by unique ID

**Independent Test**: Can be fully tested by updating an existing todo's details and verifying the changes are reflected when viewing the todo. Delivers value by allowing task refinement.

### Implementation for User Story 3

- [X] T024 [P] [US3] Create update command handler in todo_app/commands/update.py
- [X] T025 [US3] Implement validation for update command in todo_app/commands/update.py (todo exists, valid updates)
- [X] T026 [US3] Implement error handling for invalid todo IDs in todo_app/commands/update.py
- [X] T027 [US3] Create console interface for update command in todo_app/cli/console.py
- [X] T028 [US3] Integrate update command with main.py application flow

**Checkpoint**: User Stories 1, 2, and 3 should all work independently

---

## Phase 6: User Story 4 - Mark Todo as Complete (Priority: P2)

**Goal**: Allow users to change a todo's status from incomplete to complete by unique ID

**Independent Test**: Can be fully tested by marking a todo as complete and verifying it appears in completed lists and not in incomplete lists. Delivers value by tracking task completion.

### Implementation for User Story 4

- [X] T029 [P] [US4] Create complete command handler in todo_app/commands/complete.py
- [X] T030 [US4] Implement validation for complete command in todo_app/commands/complete.py (todo exists)
- [X] T031 [US4] Implement error handling for invalid todo IDs in todo_app/commands/complete.py
- [X] T032 [US4] Create console interface for complete command in todo_app/cli/console.py
- [X] T033 [US4] Integrate complete command with main.py application flow

**Checkpoint**: User Stories 1, 2, 3, and 4 should all work independently

---

## Phase 7: User Story 5 - Delete Todo (Priority: P3)

**Goal**: Allow users to remove a todo permanently from memory by unique ID with confirmation

**Independent Test**: Can be fully tested by deleting a todo and verifying it no longer appears in any lists. Delivers value by allowing list management.

### Implementation for User Story 5

- [X] T034 [P] [US5] Create delete command handler in todo_app/commands/delete.py
- [X] T035 [US5] Implement validation for delete command in todo_app/commands/delete.py (todo exists)
- [X] T036 [US5] Implement user confirmation prompt for delete command in todo_app/commands/delete.py
- [X] T037 [US5] Create console interface for delete command in todo_app/cli/console.py
- [X] T038 [US5] Integrate delete command with main.py application flow

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T039 [P] Add comprehensive error handling throughout application with user-friendly messages
- [X] T040 Implement consistent command-line interface with menu system in todo_app/cli/console.py
- [X] T041 Add input validation and sanitization across all command handlers
- [X] T042 [P] Create README.md with setup and usage instructions
- [X] T043 Create requirements.txt (though will be empty since using standard library only)
- [X] T044 Add documentation strings to all classes and methods
- [X] T045 Implement edge case handling (empty lists, invalid commands, etc.)
- [X] T046 Run quickstart validation to ensure all features work as expected

### Constitution Compliance Check

- [ ] All code follows production-grade practices (error handling, logging, documentation)
- [ ] State management is explicit with no hidden global state
- [ ] Clear separation of concerns maintained across all components
- [ ] Simplicity-first approach validated - no over-engineering present
- [ ] Implementation can evolve incrementally without breaking existing abstractions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Create add command handler in todo_app/commands/add.py"
Task: "Create console interface for add command in todo_app/cli/console.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence