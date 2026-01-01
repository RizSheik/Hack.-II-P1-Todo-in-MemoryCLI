---
description: Audit Phase I specification for completeness, determinism, and hackathon readiness before planning or implementation.
---

Your task is to perform a comprehensive audit of the Phase I specification to ensure it is complete, deterministic, and ready for planning/implementation.

# Specification Completeness Audit Skill (Phase 1)

## Purpose

Ensure the Phase I specification is:
- **Complete**: All required features are defined with acceptance criteria
- **Deterministic**: No ambiguity in expected behavior
- **Judge-Ready**: Clear, simple, and demo-able within hackathon constraints
- **Phase-I Scoped**: Only contains Phase I features (no Phase II+ items)

## When to Use

Invoke this skill when:
- **After** writing `/sp.specify` (before `/sp.plan`)
- **Before** approving implementation planning
- **During** spec review checkpoints
- When checking if specification meets quality gates

## Inputs

| Parameter | Required | Description |
|-----------|----------|-------------|
| `constitution` | Yes | Path to constitution file (default: `.specify/memory/constitution.md`) |
| `spec` | Yes | Path to spec file (default: `specs/<feature>/spec.md`) |
| `strict` | No | `true` = fail on minor gaps; `false` = warnings only (default: true) |

## Step-by-Step Process

### Phase 1: Pre-Flight Checks

```bash
# Verify audit prerequisites
1. Confirm constitution file exists and is readable
2. Confirm spec file exists and is readable
3. Check spec is Phase I scoped (no Phase II+ indicators)
```

**Failure Handling:**
- If constitution missing: Fail with "Constitution required for spec audit"
- If spec file missing: Fail with "Specification file not found"
- If spec references Phase II+ features: Flag as scope creep (see sp.audit-spec-completeness)

### Phase 2: Constitution Compliance Check

Validate spec against constitution principles:

1. **Project Principles Alignment**
   - Spec follows stated code quality standards
   - Acceptable complexity level matches constitution guidance
   - No violations of explicit principles

2. **Phase I Constraints Verification**
   - Only Python mentioned as language
   - Console application only (no GUI/web)
   - In-memory storage only (no persistence mentioned)
   - No external dependencies or APIs

3. **Quality Gate Alignment**
   - Clarity: User scenarios are understandable
   - Simplicity: No over-engineering detected
   - Testability: Each feature has clear acceptance criteria

### Phase 3: Required Features Audit

Confirm all Phase I core features are specified:

| Feature | Required | Check |
|---------|----------|-------|
| Add task | Yes | Title, description, optional due date |
| List tasks | Yes | Show all, filter by status (pending/complete) |
| Update task | Yes | Edit title, description, status |
| Complete task | Yes | Mark as done, preserve data |
| Delete task | Yes | Remove task, confirm deletion |

**Audit Each Feature For:**
- User scenario (when/who/what)
- Preconditions (valid state before action)
- Postconditions (expected state after action)
- Error conditions (invalid inputs, empty state)
- Acceptance criteria (measurable outcomes)

### Phase 4: Acceptance Criteria Validation

For each feature, verify acceptance criteria are:

1. **Specific**: Not vague or ambiguous
2. **Measurable**: Can verify pass/fail
3. **Achievable**: Possible within Phase I scope
4. **Relevant**: Maps to user value
5. **Time-bound**: Achievable in hackathon time

**Example Valid AC:**
```
Given: User has 2 pending tasks
When: User marks task #1 as complete
Then: Task #1 status changes to "complete"
And: Task #2 remains "pending"
And: List shows 1 pending, 1 complete
```

### Phase 5: Edge Case Definition Check

Validate explicit edge cases are defined:

| Edge Case | Should Be Defined |
|-----------|-------------------|
| Empty task list | Behavior when listing with no tasks |
| Duplicate task titles | Allow or reject? Validation rules |
| Invalid task ID | Error handling for non-existent task |
| Empty title | Validation (reject vs auto-generate) |
| Special characters | Input sanitization expectations |
| Long inputs | Truncation or limit behavior |
| Concurrent modifications | If applicable to in-memory model |

### Phase 6: Scope Purity Check

Ensure spec contains ONLY Phase I elements:

**Forbidden (Phase II+):**
- [ ] Database persistence (SQLite, file I/O)
- [ ] User authentication/accounts
- [ ] API endpoints or networking
- [ ] AI/ML features
- [ ] Export functionality (JSON, CSV)
- [ ] Tags, categories, or advanced filtering
- [ ] Due dates with notifications
- [ ] Search functionality
- [ ] Undo/redo operations
- [ ] Multiple lists or projects

**Warning (Avoid Unless Justified):**
- Complex data structures
- Custom classes beyond basic Task entity
- Input parsing beyond simple string handling

### Phase 7: Clarity and Traceability Check

1. **Language Clarity**
   - Technical terms are defined or obvious
   - No jargon without context
   - Consistent terminology throughout

2. **User Traceability**
   - Each user scenario maps to features
   - Acceptance criteria trace to requirements
   - Edge cases cover real user situations

3. **Demo Readiness**
   - Core workflow can be demonstrated in 5 minutes
   - Happy path is clear and compelling
   - Error cases are graceful, not confusing

### Phase 8: Generate Audit Report

Output structured report:

```
## Specification Completeness Audit Report

### Summary
- Constitution: FOUND | MISSING
- Spec File: READABLE | NOT FOUND
- Phase I Scope: COMPLIANT | VIOLATIONS
- Overall Result: PASS | FAIL | WARN

### Phase 1 Constraints Check
- [x] Python only
- [x] Console application
- [x] In-memory storage
- [x] No external dependencies

### Required Features Status
| Feature | Defined | ACs Complete | Edge Cases |
|---------|---------|--------------|------------|
| Add task | ✅ | ✅ | ✅ |
| List tasks | ✅ | ✅ | ✅ |
| Update task | ✅ | ✅ | ✅ |
| Complete task | ✅ | ✅ | ✅ |
| Delete task | ✅ | ✅ | ✅ |

### Critical Gaps (Must Fix)
1. [Feature] Missing acceptance criteria
   - Location: Section X
   - Required: Clear pass/fail conditions

2. [Feature] Edge case not defined
   - Location: Section Y
   - Required: Explicit handling for [case]

### Warnings (Should Improve)
1. [Area] Ambiguous language
   - Issue: "User should manage tasks"
   - Suggestion: "User can add, list, update, complete, delete tasks"

### Scope Creep Detected
- [Item] Database mentioned
- [Item] Authentication referenced
- [Item] Export functionality proposed

### Recommendations
1. Remove scope violations before /sp.plan
2. Add missing acceptance criteria
3. Define edge cases for all features
```

## Failure Handling

| Scenario | Handling |
|----------|----------|
| Constitution missing | Fail with error; constitution required |
| Spec file missing | Fail with error; spec required |
| Missing core feature | FAIL; all 5 features required |
| Missing acceptance criteria | FAIL; ACs must be complete |
| Scope creep detected | FAIL; remove Phase II+ items |
| Minor gaps only | WARN; proceed with caution |
| All checks pass | PASS; ready for /sp.plan |

## Owned By

**todo-spec-manager** - Primary auditor for specification quality and Phase I compliance

## Reusability

This skill is deterministic:
- Same constitution + spec always produces same audit result
- Phase I constraints are fixed (cannot be bypassed)
- Pass/Fail criteria are objective
- Warning vs critical classification is consistent

## Examples

### Full Audit
```
Skill: sp.audit-spec-completeness
Constitution: .specify/memory/constitution.md
Spec: specs/todo-app/spec.md
Strict: true
```

### Quick Compliance Check
```
Skill: sp.audit-spec-completeness
Spec: specs/todo-app/spec.md
Strict: false
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
