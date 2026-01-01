---
description: Detect and prevent scope creep that would reduce hackathon scores by over-engineering or including Phase II+ features.
---

Your task is to scan specifications and plans for scope creep - features, patterns, or decisions that violate Phase I constraints or over-engineer the solution beyond hackathon requirements.

# Scope Creep Detection Skill (Phase 1)

## Purpose

Prevent accidental over-engineering that:
- Violates Phase I constraints (Python, console, in-memory, no deps)
- Adds unnecessary complexity for hackathon demo
- Risks implementation time overruns
- Reduces judges' perception of clarity and simplicity

## When to Use

Invoke this skill when:
- **During** `/sp.specify` review (before approval)
- **Before** approving `/sp.plan`
- **During** `/sp.tasks` generation (validate task scope)
- **Any time** scope clarity is in question

## Inputs

| Parameter | Required | Description |
|-----------|----------|-------------|
| `target` | Yes | File to scan (spec.md, plan.md, or tasks.md) |
| `phase` | No | Phase to validate against (default: "phase1") |
| `strict` | No | `true` = flag all potential issues; `false` = critical only (default: true) |

## Step-by-Step Process

### Phase 1: Load Phase Constraints

Load and parse the applicable constraint set:

**Phase I Hard Constraints (Must Not Violate):**
- Language: Python only
- Application Type: Console application only
- Storage: In-memory only (no file I/O, no database)
- Dependencies: Standard library only (no pip packages)

**Phase I Anti-Patterns (Avoid):**
- Unnecessary abstractions (classes for simple data)
- Over-engineered error handling
- Complex data structures for simple problems
- Factory patterns, strategy patterns, etc. for Phase I
- Configuration files or environment-based behavior
- Modularization beyond simple file separation

### Phase 2: Pattern Definition

Define detection patterns for common scope creep:

**Forbidden Patterns (Immediate Flag):**
```
DATABASES:
  - sqlite, SQL, database, persistence, save, load, file I/O
  - Patterns: "save to", "load from", "persist", "database"

AUTHENTICATION:
  - login, sign in, sign up, password, user, account, auth, token
  - Patterns: "user account", "authentication", "authorization"

NETWORKING:
  - api, http, request, endpoint, server, client, socket, url
  - Patterns: "API call", "HTTP", "REST", "web", "network"

AI/ML:
  - ai, ml, machine learning, gpt, openai, model, train, predict
  - Patterns: "AI", "LLM", "generative", "classifier"

EXTERNAL SERVICES:
  - cloud, aws, azure, google, external, third-party, api key
  - Patterns: "external API", "cloud service", "SaaS"
```

**Warning Patterns (Scrutinize):**
```
OVER-ENGINEERING:
  - interface, abstract, base class, factory, singleton, builder
  - Patterns: "Factory pattern", "strategy pattern", "OOP design"

CONFIGURATION:
  - config, settings, environment, env var, yaml, json config
  - Patterns: "configuration file", "environment variable", ".env"

COMPLEX STRUCTURES:
  - linked list, tree, graph, hash map (use list/dict instead)
  - Patterns: "custom data structure", "linked structure"

ADVANCED FEATURES:
  - search, filter, sort, export, import, undo, redo, history
  - Patterns: "search functionality", "export to", "undo operation"
```

### Phase 3: Text Analysis

Scan the target document:

```bash
# Pattern matching
1. Convert document to lowercase for matching
2. Apply forbidden pattern regex
3. Apply warning pattern regex
4. Record all matches with context (line numbers)
5. Categorize by severity (critical, warning, info)
```

**Failure Handling:**
- File read error: Fail with clear error message
- Encoding error: Attempt UTF-8, fail on decode error

### Phase 4: Context Validation

For each detected pattern, validate context:

1. **Is it truly scope creep?**
   - Check surrounding text for justification
   - Some "forbidden" words may appear innocently (e.g., "database" in "not using a database")

2. **What's the actual feature?**
   - Extract the feature being proposed
   - Map to Phase I or Phase II+

3. **Severity Assessment:**
   - Critical: Violates hard constraint (fail the review)
   - Warning: Adds unnecessary complexity (recommend removal)
   - Info: Potential future concern (document only)

### Phase 5: Generate Scope Report

Output structured report:

```
## Scope Creep Detection Report

### Summary
- Target File: [path]
- Phase: Phase I
- Critical Violations: N
- Warnings: N
- Result: PASS | FAIL | WARN

### Critical Violations (Must Remove)
1. [Pattern]: "[matched text]"
   - Location: Line X
   - Context: "..."
   - Issue: Violates Phase I constraint
   - Recommendation: Remove feature or defer to Phase II

2. [Pattern]: "[matched text]"
   - Location: Line Y
   - Context: "..."
   - Issue: Violates Phase I constraint
   - Recommendation: Remove feature or defer to Phase II

### Warnings (Should Reconsider)
1. [Pattern]: "[matched text]"
   - Location: Line Z
   - Context: "..."
   - Issue: Adds unnecessary complexity
   - Recommendation: Simplify or justify necessity

### Phase I Alignment
| Constraint | Status | Evidence |
|------------|--------|----------|
| Python only | ✅ | No non-Python mentioned |
| Console app | ✅ | No GUI/web mentioned |
| In-memory | ❌ | "save to file" at line 42 |
| No external deps | ✅ | No pip packages mentioned |

### Recommendations
1. Remove all critical violations before approval
2. Justify or remove warning items
3. Stay within 5 core features (Add/List/Update/Complete/Delete)

### Pass/Fail Criteria
- PASS: No critical violations, minimal warnings
- FAIL: Any critical violations detected
- WARN: Only warnings, no critical violations
```

### Phase 6: Block or Approve

Based on results:

| Result | Action |
|--------|--------|
| FAIL | Block progression; require scope cleanup |
| WARN | Proceed with scope creep warnings noted |
| PASS | Approve; no scope concerns detected |

## Failure Handling

| Scenario | Handling |
|----------|----------|
| Target file missing | Fail with error; file required |
| File unreadable | Fail with encoding/permission error |
| Critical violations found | FAIL; block progression |
| Warnings only | WARN; document, allow progression |
| No issues found | PASS; clear for next phase |

## Owned By

**hackathon-review-agent** - Primary detector of scope creep and over-engineering

## Reusability

This skill is deterministic:
- Same target document always produces same detection results
- Pattern matching is consistent
- Severity classification is rule-based
- Results are reproducible across runs

## Examples

### Scan Specification
```
Skill: sp.detect-scope-creep
Target: specs/todo-app/spec.md
Phase: phase1
Strict: true
```

### Quick Plan Check
```
Skill: sp.detect-scope-creep
Target: specs/todo-app/plan.md
Strict: false
```

### Validate Tasks Scope
```
Skill: sp.detect-scope-creep
Target: specs/todo-app/tasks.md
Strict: true
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
