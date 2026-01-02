# CLI Interface Contracts: Phase I – In-Memory Console-Based Todo App

**Date**: 2026-01-01
**Feature**: 001-todo-app

## Overview

This document defines the contracts between the CLI layer and the application/command layers for the in-memory console-based todo application.

## Command Interface Contract

### Add Command
- **Input**: title (str), description (str), priority (optional str)
- **Output**: success message with todo ID or error message
- **Validation**: Title and description must be non-empty
- **Error cases**: Invalid input parameters

### View Command
- **Input**: view_type (all|completed|incomplete)
- **Output**: Formatted list of todos matching criteria
- **Validation**: view_type must be one of allowed values
- **Error cases**: Invalid view type

### Update Command
- **Input**: todo_id (int), updates (dict with title, description, priority)
- **Output**: success message or error message
- **Validation**: todo_id must exist, updates must be valid
- **Error cases**: Todo not found, invalid updates

### Delete Command
- **Input**: todo_id (int)
- **Output**: confirmation message or error message
- **Validation**: todo_id must exist
- **Error cases**: Todo not found

### Complete Command
- **Input**: todo_id (int)
- **Output**: success message or error message
- **Validation**: todo_id must exist
- **Error cases**: Todo not found

## TodoStore Interface Contract

### add(todo)
- **Input**: Todo object with title and description (id auto-generated)
- **Output**: Todo object with assigned ID
- **Side effects**: Todo added to store
- **Error cases**: Validation failure

### get(todo_id)
- **Input**: todo_id (int)
- **Output**: Todo object or None if not found
- **Side effects**: None
- **Error cases**: Todo not found

### update(todo_id, updates)
- **Input**: todo_id (int), updates (dict)
- **Output**: Updated Todo object or None if not found
- **Side effects**: Todo modified in store
- **Error cases**: Todo not found, invalid updates

### delete(todo_id)
- **Input**: todo_id (int)
- **Output**: Boolean indicating success
- **Side effects**: Todo removed from store
- **Error cases**: Todo not found

### list_all()
- **Input**: None
- **Output**: List of all Todo objects
- **Side effects**: None
- **Error cases**: None

### list_by_status(status)
- **Input**: status (str)
- **Output**: List of Todo objects with matching status
- **Side effects**: None
- **Error cases**: Invalid status

### mark_complete(todo_id)
- **Input**: todo_id (int)
- **Output**: Updated Todo object or None if not found
- **Side effects**: Todo status changed to "complete"
- **Error cases**: Todo not found

## Error Handling Contract

All commands follow the same error handling pattern:
- Return structured error objects with error type and message
- Never crash the application on invalid input
- Provide clear feedback to the user
- Maintain application state integrity