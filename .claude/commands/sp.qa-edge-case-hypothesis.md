---
description: Automatically generate comprehensive edge case hypotheses from feature specifications. Proactively identifies failure modes before implementation.
---

Your task is to automatically generate edge case hypotheses by analyzing feature specifications and domain entities, producing a complete list of potential failure modes that must be handled.

# QA Edge Case Hypothesis Skill (Phase 1)

## Purpose

Proactively identify failure modes to:
- **Prevent bugs**: Catch edge cases before implementation
- **Improve reliability**: Ensure graceful handling of unexpected inputs
- **Guide testing**: Provide test cases for the test suite
- **Reduce rework**: Fix spec gaps before code is written

## When to Use

Invoke this skill automatically when:
- **After** `/sp.specify` creates or updates feature specs
- **Before** `/sp.plan` to ensure edge cases are captured
- **During** `/sp.tasks` to generate test cases
- **Any time** a new feature or operation is added

## Inputs

| Parameter | Required | Description |
|-----------|----------|-------------|
| `spec` | Yes | Path to spec.md file |
| `domain_model` | No | Path to domain model (if separate) |
| `output_format` | No | `list` (default) or `test_cases` |

## Step-by-Step Process

### Phase 1: Parse Specification

Extract all features, operations, and entities:

```python
# Automated parsing
1. Read spec.md file
2. Extract all ## Operation: [Name] sections
3. Extract all ## Entity: [Name] sections
4. Extract ## Acceptance Criteria for each operation
5. Extract ## Edge Cases already defined
6. Build operation list with preconditions/postconditions
```

**Failure Handling:**
- Spec file missing: Fail with error "Specification required for edge case generation"
- Parse error: Warn, continue with partial parsing

### Phase 2: Generate Input Validation Hypotheses

For each operation, generate hypotheses for invalid inputs:

**Text Input Hypotheses:**
| Input Type | Hypothesis | Severity |
|------------|------------|----------|
| Empty string | `""` → Should reject or auto-generate? | CRITICAL |
| Whitespace only | `"   "` → Valid title or invalid? | HIGH |
| Unicode/emojis | `"Buy milk 🐄"` → Handle or reject? | MEDIUM |
| Maximum length | 1000-char title → Truncate or reject? | HIGH |
| Special characters | `"<script>alert()</script>" → Sanitize? | HIGH |
| SQL injection attempt | `"'; DROP TABLE tasks;--"` → Sanitize? | CRITICAL |
| Null/None | `None` passed → TypeError or handled? | CRITICAL |

**Numeric Input Hypotheses:**
| Input Type | Hypothesis | Severity |
|------------|------------|----------|
| Negative numbers | Task ID -1 → Reject or interpret? | HIGH |
| Zero | Task ID 0 → Valid or invalid? | MEDIUM |
| Non-numeric string | `"abc"` for ID → Parse error? | HIGH |
| Floating point | ID 1.5 → Round or reject? | LOW |
| Overflow | Very large number → Integer overflow? | LOW |

### Phase 3: Generate State Violation Hypotheses

For each entity state machine, identify invalid transitions:

**Task State Machine (Standard):**
```
pending → completed (valid)
pending → deleted (valid)
completed → pending (reopen? valid or reject?)
deleted → pending (restore? Phase II)
completed → deleted (valid)
```

**Hypothesis Generation:**
| From State | To State | Hypothesis | Severity |
|------------|----------|------------|----------|
| deleted | completed | Can completed task be marked done? | HIGH |
| non-existent | pending | Creating with specific ID? | LOW |
| completed | completed | Re-completing same task? | MEDIUM |

### Phase 4: Generate Reference Integrity Hypotheses

For operations referencing other entities:

**Task Reference Hypotheses:**
| Reference Type | Hypothesis | Severity |
|----------------|------------|----------|
| Non-existent ID | Update task #999 when only #1 exists | CRITICAL |
| Deleted task | Complete task already deleted | HIGH |
| Duplicate ID | Two tasks with same ID (data corruption) | CRITICAL |
| Orphaned reference | Task references deleted category | LOW |

### Phase 5: Generate Concurrency Hypotheses

For in-memory storage model:

**Concurrency Hypotheses:**
| Scenario | Hypothesis | Severity |
|----------|------------|----------|
| Race condition | Two users mark task #1 complete simultaneously | MEDIUM |
| State inconsistency | Read-modify-write without locking | MEDIUM |
| Bulk operation | Add 1000 tasks at once (performance) | LOW |

### Phase 6: Generate Boundary Hypotheses

**System Limits:**
| Boundary | Hypothesis | Severity |
|----------|------------|----------|
| Zero tasks | List, update, complete, delete on empty list | HIGH |
| One task | All operations on single-item list | HIGH |
| Maximum tasks | System limits (if any) | LOW |
| Very long session | Memory growth over time | LOW |

### Phase 7: Generate Output Format Hypotheses

**Output Scenarios:**
| Scenario | Hypothesis | Severity |
|----------|------------|----------|
| Empty list output | `[]` vs `"No tasks"` vs `null` | MEDIUM |
| Formatted output | ANSI codes in CLI (test environment) | LOW |
| Locale-specific | Date formatting for non-US locales | LOW |

### Phase 8: Compile Hypothesis Report

Output structured report:

```
## Edge Case Hypothesis Report

### Summary
- Operations analyzed: N
- Entities analyzed: N
- Total hypotheses generated: N
- Critical: C | High: H | Medium: M | Low: L

### Critical Hypotheses (Must Handle)
1. [Operation: Add Task] Empty title input
   - Hypothesis: User submits task with empty string title
   - Impact: Data integrity violation
   - Required Handling: Reject with error message
   - Test Case: `test_add_task_empty_title_rejected()`

2. [Operation: Complete Task] Non-existent task ID
   - Hypothesis: User marks task #999 complete when only #1 exists
   - Impact: User confusion, undefined behavior
   - Required Handling: Error "Task not found"
   - Test Case: `test_complete_task_not_found_error()`

3. [Operation: Update Task] SQL injection in title
   - Hypothesis: Malicious input in task title
   - Impact: Security vulnerability
   - Required Handling: Sanitize or reject dangerous input
   - Test Case: `test_update_task_sanitized_input()`

### High Hypotheses (Should Handle)
1. [Operation: Delete Task] Already deleted task
   - Hypothesis: Delete task #1, then delete task #1 again
   - Impact: Error or silent success?
   - Recommended: Error "Task not found"

2. [Operation: List Tasks] Empty list display
   - Hypothesis: List tasks when no tasks exist
   - Impact: User experience
   - Recommended: Clear "No tasks" message

### Medium Hypotheses (Nice to Handle)
1. [Operation: Add Task] Whitespace-only title
   - Hypothesis: Title is only spaces
   - Impact: Ambiguous valid/invalid
   - Recommended: Strip and validate

2. [Operation: Complete Task] Re-completing task
   - Hypothesis: Mark already-complete task complete again
   - Impact: Idempotency
   - Recommended: Silent success (idempotent)

### Low Hypotheses (Consider Later)
1. Performance with large task lists
2. Unicode handling in all outputs
3. Locale-specific date formatting

### Test Case Mapping
| Hypothesis | Test Function |
|------------|---------------|
| Empty title | `test_add_task_empty_title_rejected()` |
| Not found ID | `test_complete_task_not_found_error()` |
| SQL injection | `test_update_task_sanitized_input()` |
| Already deleted | `test_delete_task_already_deleted_error()` |
| Empty list display | `test_list_tasks_empty_shows_message()` |
| Re-complete | `test_complete_task_idempotent()` |

### Coverage Summary
| Operation | Input | State | Reference | Boundary |
|-----------|-------|-------|-----------|----------|
| Add Task | 6 | - | - | 2 |
| List Tasks | 1 | - | 1 | 3 |
| Update Task | 6 | 2 | 2 | 1 |
| Complete Task | 2 | 3 | 2 | 1 |
| Delete Task | 2 | 2 | 2 | 1 |
```

### Phase 9: Auto-Create Test Cases (Optional)

If `output_format: test_cases`, generate Python test file:

```python
# Generated edge case tests
class TestEdgeCases:
    """Auto-generated edge case tests from hypothesis analysis"""

    def test_add_task_empty_title_rejected(self):
        """Hypothesis: Empty title should be rejected"""
        # Arrange
        todo = TodoApp()
        # Act & Assert
        with pytest.raises(ValidationError):
            todo.add_task("")

    def test_complete_task_not_found_error(self):
        """Hypothesis: Non-existent task should error"""
        # Arrange
        todo = TodoApp()
        # Act & Assert
        with pytest.raises(TaskNotFoundError):
            todo.complete_task(999)

    # ... more tests
```

## Failure Handling

| Scenario | Handling |
|----------|----------|
| Spec file missing | Fail; specification required |
| Parse error | Warn; continue with partial results |
| No operations found | Warn; spec may be empty |
| Critical hypotheses > 10 | Report all; recommend spec review |
| All hypotheses generated | PASS; proceed with implementation |

## Owned By

**todo-domain-expert** - Primary source for domain logic and edge case identification

## Reusability

This skill is deterministic:
- Same spec always produces same hypotheses
- Severity classification follows fixed rules
- Test case naming is consistent
- Coverage metrics are computed identically

## Examples

### Standard Hypothesis Generation
```
Skill: sp.qa-edge-case-hypothesis
Spec: specs/todo-app/spec.md
Output: list
```

### Generate Test Cases
```
Skill: sp.qa-edge-case-hypothesis
Spec: specs/todo-app/spec.md
Output: test_cases
```

### With Domain Model
```
Skill: sp.qa-edge-case-hypothesis
Spec: specs/todo-app/spec.md
Domain: specs/todo-app/domain.md
Output: test_cases
```

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent-native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3-7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent-native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/...`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.
