---
description: Review Python CLI code against project constitution and SDD standards. Validates Phase 1 constraints, code quality, and architecture compliance.
---

Your task is to perform a comprehensive code review against the project's constitution, SDD standards, and Phase 1 constraints.

# Code Review Skill for Todo App Phase 1

## Purpose

Validate that Python CLI code adheres to:
- Project constitution principles (`.specify/memory/constitution.md`)
- Phase 1 constraints (Python, console app, in-memory, no external dependencies)
- SDD quality gates and acceptance criteria
- Code references and code review standards from CLAUDE.md

## When to Use

Invoke this skill when:
- Preparing to commit or PR code
- After completing implementation tasks
- Before running `/sp.analyze` on implementation
- During code review checkpoints in the workflow
- When verifying task completion before marking tasks done

## Inputs

| Parameter | Required | Description |
|-----------|----------|-------------|
| `files` | Yes | Python files to review (glob pattern or list) |
| `focus` | No | Specific area: `constitution`, `phase1`, `quality`, `security`, `all` |
| `strict` | No | `true` = fail on minor violations; `false` = warnings only (default: true) |

## Step-by-Step Process

### Phase 1: Pre-Flight Checks

```bash
# Verify review prerequisites
1. Check constitution exists at `.specify/memory/constitution.md`
2. Identify files to review via glob pattern
3. Read constitution file to extract current standards
```

**Failure Handling:**
- If constitution missing: Warn and proceed with default Phase 1 constraints
- If no files match pattern: Return error "No files to review"

### Phase 2: Gather Context

```bash
# Collect code and context
1. Read all target Python files
2. Extract imports to identify dependencies
3. Identify CLI patterns (argparse, sys.argv, input loops)
4. Check for data storage patterns (in-memory vs external)
```

**Failure Handling:**
- If file read fails: Skip file, log warning, continue with others

### Phase 3: Constitution Compliance Review

Check against constitution principles:

1. **Code Quality Standards**
   - Functions have single responsibility
   - Variables have descriptive names
   - Code is self-documenting or has necessary comments
   - No dead code or unused imports

2. **Testing Standards**
   - Functions are testable (no hidden dependencies)
   - Input validation exists for user inputs
   - Error messages are user-friendly

3. **Performance Standards**
   - No unnecessary loops or O(n²) patterns where avoidable
   - Memory usage is reasonable for in-memory storage

### Phase 4: Phase 1 Constraints Verification

Validate non-negotiable Phase 1 constraints:

| Constraint | Check Method | Violation = FAIL |
|------------|--------------|------------------|
| Python only | Import statements | `import` non-Python libs |
| Console app | No GUI imports (tkinter, PyQt) | GUI framework detected |
| In-memory storage | No file I/O, database, network | `open()`, `sqlite3`, `requests` |
| No external dependencies | `import` statements | Third-party packages (not stdlib) |

### Phase 5: CLI Quality Review

Validate CLI-specific patterns:

1. **Input Validation**
   - User inputs are validated before processing
   - Invalid inputs produce clear error messages
   - Edge cases handled (empty strings, whitespace, special chars)

2. **Menu/Loop Quality**
   - Clear exit conditions (q, quit, exit)
   - User-friendly prompts
   - No infinite loops without exit path
   - Graceful handling of KeyboardInterrupt (Ctrl+C)

3. **Error Handling**
   - Try/except where appropriate
   - Exceptions don't expose internals to users
   - System exit codes are meaningful

### Phase 6: SDD Artifact Compliance

1. **Code References**
   - Code changes reference task IDs where applicable
   - No unrelated refactoring (smallest viable change)
   - No hardcoded secrets or tokens

2. **Architecture Alignment**
   - Functions match planned architecture from `plan.md`
   - No architectural drift from specification

### Phase 7: Generate Review Report

Output structured report:

```
## Code Review Report

### Summary
- Files reviewed: N
- Violations: N (critical: C, warning: W, info: I)
- Result: PASS | FAIL

### Critical Violations (Must Fix)
1. [File:Line] Description
   - Impact: Blast radius
   - Fix: Recommended approach

### Warnings (Should Fix)
1. [File:Line] Description
   - Impact: Potential issue
   - Suggestion: Improvement

### Info (Nice to Have)
1. [File:Line] Description
   - Suggestion: Optional improvement

### Constitution Compliance
- [x] Code quality principles followed
- [x] Testing standards met
- [x] Performance standards met

### Phase 1 Constraints
- [x] Python only
- [x] Console application
- [x] In-memory storage
- [x] No external dependencies
```

## Failure Handling

| Scenario | Handling |
|----------|----------|
| Constitution file missing | Proceed with hardcoded Phase 1 defaults, warn |
| File read error | Skip file, log warning, continue review |
| Import error (stdlib vs external) | Use strict stdlib check; flag non-stdlib |
| Syntax error in target file | Flag as critical violation |
| No target files | Return error, no review performed |
| All files pass | Return PASS with summary |
| Critical violations found | Return FAIL with list |

## Owned By

**python-cli-agent** - Primary reviewer for Python CLI quality

## Reusability

This skill is deterministic:
- Same inputs always produce same review results
- Constitution check adapts to loaded constitution file
- Phase 1 constraints are fixed (cannot be bypassed)
- Warning vs critical classification is consistent

## Examples

### Basic Review
```
Skill: sp.code-review
Files: src/**/*.py
Focus: all
Strict: true
```

### Quick Phase 1 Check
```
Skill: sp.code-review
Files: todo.py
Focus: phase1
Strict: true
```

### Constitution Compliance Only
```
Skill: sp.code-review
Files: "*.py"
Focus: constitution
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
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.
