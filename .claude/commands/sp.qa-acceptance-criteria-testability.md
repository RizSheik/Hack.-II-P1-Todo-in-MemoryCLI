---
description: Automatically validate that all acceptance criteria are testable with clear pass/fail conditions. Identifies and fixes untestable requirements.
---

Your task is to analyze acceptance criteria and ensure each one can be verified through testing. Flag vague, untestable, or ambiguous criteria and suggest specific improvements.

# QA Acceptance Criteria Testability Skill (Phase 1)

## Purpose

Ensure acceptance criteria are:
- **Testable**: Each criterion has clear pass/fail outcome
- **Verifiable**: Can be confirmed via automated or manual testing
- **Unambiguous**: No subjective interpretation required
- **Complete**: All user scenarios have corresponding criteria

## When to Use

Invoke this skill automatically when:
- **After** `/sp.specify` defines new acceptance criteria
- **Before** `/sp.tasks` to ensure testability
- **During** quality gates (sp.audit-spec-completeness)
- **Any time** acceptance criteria are modified

## Inputs

| Parameter | Required | Description |
|-----------|----------|-------------|
| `spec` | Yes | Path to spec.md file |
| `strictness` | No | `strict` (default) or `lenient` - how to flag issues |

## Step-by-Step Process

### Phase 1: Extract All Acceptance Criteria

Parse the specification for acceptance criteria:

```python
# Automated extraction
1. Read spec.md file
2. Find all ## Acceptance Criteria sections
3. Extract individual criteria (bullet points, numbered items)
4. Associate each criterion with its parent feature/operation
5. Build criteria inventory
```

**Failure Handling:**
- Spec file missing: Fail; specification required
- No ACs found: Warn; specification may lack acceptance criteria

### Phase 2: Classify Each Criterion

Categorize by testability type:

**Testable Types (Good):**
| Type | Example | Verification Method |
|------|---------|---------------------|
| State change | "Task status changes to 'completed'" | Assert state == 'completed' |
| Output match | "Display shows 'No tasks'" | Assert output == 'No tasks' |
| Count assertion | "List shows 3 tasks" | Assert len(tasks) == 3 |
| Error condition | "Error message shown" | Assert exception raised |
| Property assertion | "Task has title 'Buy milk'" | Assert task.title == 'Buy milk' |

**Potentially Untestable Types (Flag):**
| Type | Example | Issue |
|------|---------|-------|
| Vague quality | "User-friendly error messages" | Subjective |
| Performance claim | "Fast response time" | Undefined threshold |
| Completeness claim | "All cases handled" | Can't verify |
| Preference-based | "Intuitive interface" | Subjective |
| Future-proofing | "Easy to extend" | Not testable now |

### Phase 3: Evaluate Each Criterion

Apply the SMART test:

**S - Specific:**
| Criterion | Specific? | Issue |
|-----------|-----------|-------|
| "Task is saved" | No | What does "saved" mean? |
| "New task appears in list" | Yes | Observable behavior |

**M - Measurable:**
| Criterion | Measurable? | Issue |
|-----------|-------------|-------|
| "Error message shown" | Yes | Boolean check |
| "User understands error" | No | Can't measure understanding |

**A - Achievable:**
| Criterion | Achievable? | Issue |
|-----------|-------------|-------|
| "System responds instantly" | No | Hardware-dependent |
| "Task completes in <1s" | Yes | Timing assertion |

**R - Relevant:**
| Criterion | Relevant? | Issue |
|-----------|-----------|-------|
| "User is happy" | No | Subjective |
| "Task is marked done" | Yes | Business requirement |

**T - Time-bound:**
| Criterion | Time-bound? | Issue |
|-----------|-------------|-------|
| "Task is available" | No | For how long? |
| "Display updates immediately" | No | Define "immediately" |

### Phase 4: Check Completeness

Verify each operation has complete coverage:

**Minimum ACs per Operation:**

| Operation | Required ACs |
|-----------|--------------|
| Add Task | 3+ (empty title, valid input, duplicate handling) |
| List Tasks | 2+ (empty list, non-empty list) |
| Update Task | 3+ (valid update, invalid ID, empty fields) |
| Complete Task | 2+ (valid ID, invalid ID) |
| Delete Task | 2+ (valid ID, invalid ID) |

**AC Categories Coverage:**
| Category | Required | Check |
|----------|----------|-------|
| Happy path | 1+ | Main success scenario covered? |
| Error handling | 1+ | Failure modes have ACs? |
| Edge cases | 1+ | Boundary conditions covered? |
| Validation | 1+ | Input validation specified? |

### Phase 5: Identify Specific Issues

For each untestable criterion, identify the problem:

**Issue Categories:**

1. **Subjective Language:**
   - "user-friendly", "intuitive", "easy to use", "clean"
   - Fix: Replace with observable behaviors

2. **Undefined Metrics:**
   - "fast", "quick", "immediate", "efficient"
   - Fix: Define specific thresholds (e.g., "<100ms")

3. **Incomplete Specifications:**
   - "appropriate response", "valid input"
   - Fix: Define what "appropriate" and "valid" mean

4. **Unverifiable Claims:**
   - "all cases handled", "no edge cases missed"
   - Fix: List specific cases instead

5. **Missing Preconditions:**
   - "System responds correctly"
   - Fix: Define precondition and expected response

### Phase 6: Generate Testability Report

Output structured report:

```
## Acceptance Criteria Testability Report

### Summary
- Total Criteria: N
- Testable: T (T%) | Untestable: U (U%) | Warning: W (W%)
- Result: PASS | WARN | FAIL

### Testable Criteria (Approved)
1. [Add Task] "New task appears in list"
   - Verification: `assert task in todo.list_tasks()`
   - Status: ✅ APPROVED

2. [Complete Task] "Error shown for invalid ID"
   - Verification: `pytest.raises(TaskNotFoundError)`
   - Status: ✅ APPROVED

### Untestable Criteria (Must Fix)
1. [List Tasks] "User-friendly message shown for empty list"
   - Issue: Subjective language ("user-friendly")
   - Original: "User-friendly message shown for empty list"
   - Fix: "System displays 'No tasks' message"
   - Verification: `assert "No tasks" in output`
   - Severity: CRITICAL

2. [Update Task] "Update happens quickly"
   - Issue: Undefined metric ("quickly")
   - Original: "Update happens quickly"
   - Fix: "Update completes in <100ms"
   - Verification: `assert duration < 0.1`
   - Severity: HIGH

3. [Delete Task] "System handles deletion appropriately"
   - Issue: Incomplete ("appropriately")
   - Original: "System handles deletion appropriately"
   - Fix: "Deleted task no longer appears in list"
   - Verification: `assert task_id not in tasks`
   - Severity: HIGH

### Warnings (Should Improve)
1. [Add Task] "Title is validated"
   - Warning: What constitutes validation?
   - Suggestion: Specify validation rules

### Completeness Assessment
| Operation | ACs Found | Min Required | Status |
|-----------|-----------|--------------|--------|
| Add Task | 4 | 3 | ✅ COMPLETE |
| List Tasks | 2 | 2 | ✅ COMPLETE |
| Update Task | 3 | 3 | ✅ COMPLETE |
| Complete Task | 2 | 2 | ✅ COMPLETE |
| Delete Task | 2 | 2 | ✅ COMPLETE |

### Category Coverage
| Category | Coverage | Status |
|----------|----------|--------|
| Happy path | 5/5 | ✅ |
| Error handling | 5/5 | ✅ |
| Edge cases | 3/5 | ⚠️ INCOMPLETE |
| Input validation | 4/5 | ⚠️ INCOMPLETE |

### Recommended Fixes
1. Replace "user-friendly" with specific output text
2. Replace "quickly" with "<100ms" threshold
3. Replace "appropriately" with specific behavior
4. Add edge case criteria for list boundaries
5. Specify exact validation rules for titles

### Pass/Fail Criteria
- PASS: All criteria testable, completeness met
- WARN: All critical criteria testable, some warnings
- FAIL: Critical untestable criteria found
```

### Phase 7: Auto-Generate Fix Suggestions

For each untestable criterion, generate a rewrite:

**Before/After Examples:**

| Original | Fixed Version |
|----------|---------------|
| "User-friendly error" | "Error message is 'Task not found: {id}'" |
| "Quick response" | "Response time < 100ms" |
| "Intuitive input" | "Press 1-5 or q to select" |
| "All inputs validated" | "Empty title rejected; title length max 200 chars" |
| "Clear display" | "Tasks displayed as numbered list with status" |

## Failure Handling

| Scenario | Handling |
|----------|----------|
| Spec file missing | Fail; specification required |
| No ACs found | Warn; no criteria to analyze |
| All ACs untestable | FAIL; spec needs revision |
| Some ACs untestable | WARN; proceed with fixes |
| Completeness gap | WARN; note missing ACs |

## Owned By

**todo-domain-expert** - Primary validator of acceptance criteria quality

## Reusability

This skill is deterministic:
- Same specification always produces same analysis
- Issue classification follows fixed rules
- Fix suggestions are template-based
- Pass/fail determination is rule-based

## Examples

### Standard Analysis
```
Skill: sp.qa-acceptance-criteria-testability
Spec: specs/todo-app/spec.md
Strictness: strict
```

### Lenient Analysis (Fewer Flags)
```
Skill: sp.qa-acceptance-criteria-testability
Spec: specs/todo-app/spec.md
Strictness: lenient
```

### Pre-Tasks Validation
```
Skill: sp.qa-acceptance-criteria-testability
Spec: specs/todo-app/spec.md
Strictness: strict
# Blocks /sp.tasks until untestable ACs are fixed
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
     - Allocate an ID; compute the output path based to stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.
