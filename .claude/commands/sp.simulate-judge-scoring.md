---
description: Simulate hackathon judge scoring for Phase I submission before code is written. Predicts scores across clarity, execution, innovation, and demo readiness.
---

Your task is to simulate how hackathon judges would score the Phase I todo application based on the specification and plan. Identify high-impact improvements and scoring risks before implementation begins.

# Judge Scoring Simulation Skill (Phase 1)

## Purpose

Predict judge scoring to:
- **Maximize Scores**: Focus on high-impact improvements
- **Reduce Risk**: Identify scoring weaknesses early
- **Demo Optimization**: Ensure 5-minute demo rule compliance
- **Alignment Check**: Validate hackathon goal alignment

## When to Use

Invoke this skill when:
- **Before** approving `/sp.tasks` (final spec check)
- **Before** starting `/sp.implement` (last chance for changes)
- **After** spec review to validate readiness
- When uncertain about feature prioritization

## Inputs

| Parameter | Required | Description |
|-----------|----------|-------------|
| `constitution` | Yes | Constitution file for standards |
| `spec` | Yes | Feature specification |
| `plan` | Yes | Implementation plan |
| `weights` | No | Custom weight overrides (optional) |

## Step-by-Step Process

### Phase 1: Load Judge Rubric

Define the official judging criteria:

**Phase I Rubric (4 Categories, 25% Each):**

| Category | Weight | Description |
|----------|--------|-------------|
| **Clarity** | 25% | Clear problem, solution, and value proposition |
| **Execution & Complexity** | 25% | Quality of implementation, appropriate complexity |
| **Innovation & Impact** | 25% | Novelty of approach, potential impact |
| **Demo Readiness** | 25% | Works reliably, impressive demo in 5 min |

**Scoring Scale (1-10 per category):**
- 9-10: Exceptional, standout work
- 7-8: Strong, meets expectations
- 5-6: Adequate, meets minimums
- 3-4: Below expectations
- 1-2: Poor or incomplete

### Phase 2: Calculate Clarity Score (Max 25%)

Evaluate clarity across 4 dimensions:

**1. Problem Statement Clarity (0-25 points)**
- Is the problem clearly articulated? (0-10)
- Is the target user clear? (0-8)
- Is the value proposition explicit? (0-7)

**2. Solution Clarity (0-25 points)**
- Is the solution easy to understand? (0-10)
- Does the spec clearly define what will be built? (0-8)
- Are edge cases and behavior defined? (0-7)

**3. Simplicity (0-25 points)**
- Is the scope appropriately limited? (0-10)
- Is there unnecessary complexity? (penalty) (0-10)
- Is the API/user interface simple? (0-5)

**4. Documentation Quality (0-25 points)**
- Is the spec well-organized? (0-10)
- Are acceptance criteria clear? (0-8)
- Is the plan actionable? (0-7)

**Clarity Score Formula:**
```
Clarity % = (Problem + Solution + Simplicity + Documentation) / 100 * 25
```

### Phase 3: Calculate Execution Score (Max 25%)

Evaluate execution and implementation quality:

**1. Architecture Appropriateness (0-30 points)**
- Is the architecture right for Phase I? (0-15)
- Are there unnecessary abstractions? (penalty) (0-10)
- Does it follow constitution standards? (0-5)

**2. Implementation Feasibility (0-30 points)**
- Can this be implemented in hackathon time? (0-15)
- Are tasks well-defined and actionable? (0-10)
- Are dependencies and blockers identified? (0-5)

**3. Code Quality Indicators (0-25 points)**
- Are coding standards defined? (0-10)
- Is error handling addressed? (0-8)
- Is input validation specified? (0-7)

**4. Testability (0-15 points)**
- Can features be tested independently? (0-8)
- Are acceptance criteria testable? (0-7)

**Execution Score Formula:**
```
Execution % = (Architecture + Feasibility + Quality + Testability) / 100 * 25
```

### Phase 4: Calculate Innovation Score (Max 25%)

Evaluate innovation and impact (tricky for todo app):

**1. Novelty of Approach (0-30 points)**
- Does it solve the problem in a fresh way? (0-15)
- Are there clever simplifications? (0-10)
- Does it avoid common pitfalls? (0-5)

**2. User Impact (0-30 points)**
- Does it solve a real problem? (0-15)
- Would users actually use this? (0-10)
- Does it have potential for extension? (0-5)

**3. Technical Innovation (0-25 points)**
- Does it use Python elegantly? (0-10)
- Are there interesting patterns? (0-8)
- Does it demonstrate skill? (0-7)

**4. Uniqueness (0-15 points)**
- Does it stand out from basic todo apps? (0-8)
- Does it have a "wow" factor? (0-7)

**Innovation Score Formula:**
```
Innovation % = (Novelty + Impact + Technical + Uniqueness) / 100 * 25
```

**Note:** A basic todo app may score 5-12/25 here. This is expected for Phase I.

### Phase 5: Calculate Demo Readiness Score (Max 25%)

Evaluate demo potential:

**1. Core Workflow Clarity (0-30 points)**
- Is the happy path obvious? (0-15)
- Can judges understand it quickly? (0-10)
- Is the value demo-able in 5 minutes? (0-5)

**2. Reliability Indicators (0-25 points)**
- Are error cases handled gracefully? (0-10)
- Does the spec ensure stability? (0-8)
- Are edge cases covered? (0-7)

**3. Visual/Interactive Appeal (0-20 points)**
- Is the CLI interface engaging? (0-10)
- Will the demo be memorable? (0-10)

**4. Impressiveness Potential (0-25 points)**
- Will this demo "wow" judges? (0-10)
- Is there a "hook" or unique feature? (0-8)
- Does it show Python proficiency? (0-7)

**Demo Score Formula:**
```
Demo % = (Workflow + Reliability + Appeal + Impressiveness) / 100 * 25
```

### Phase 6: Generate Scoring Report

Output structured report:

```
## Judge Scoring Simulation Report

### Overall Score Prediction
┌────────────────────────────────────────────────┐
│  CLARITY          │  8.5/10  │  21.25/25%     │
│  EXECUTION        │  7.5/10  │  18.75/25%     │
│  INNOVATION       │  5.0/10  │  12.50/25%     │
│  DEMO READINESS   │  8.0/10  │  20.00/25%     │
├────────────────────────────────────────────────┤
│  TOTAL            │  7.3/10  │  72.50/100%    │
│  GRADE            │  B       │  Strong        │
└────────────────────────────────────────────────┘

### Category Breakdown

#### CLARITY (8.5/10)
| Dimension         | Score | Notes                                    |
|-------------------|-------|------------------------------------------|
| Problem Statement | 9/10  | Clear user need and value proposition    |
| Solution          | 8/10  | Well-defined features and behavior       |
| Simplicity        | 9/10  | Appropriate scope for Phase I            |
| Documentation     | 8/10  | Good spec structure, clear ACs           |
| PENALTIES         | -0.5  | Minor ambiguity in edge case handling    |

#### EXECUTION (7.5/10)
| Dimension         | Score | Notes                                    |
|-------------------|-------|------------------------------------------|
| Architecture      | 8/10  | Appropriate for Phase I                  |
| Feasibility       | 8/10  | Tasks are actionable and time-boxed      |
| Code Quality      | 7/10  | Standards defined, needs detail          |
| Testability       | 7/10  | ACs are testable, integration concern    |

#### INNOVATION (5.0/10) - Expected for Todo App
| Dimension         | Score | Notes                                    |
|-------------------|-------|------------------------------------------|
| Novelty           | 5/10  | Standard todo app approach               |
| Impact            | 6/10  | Solves real problem for target users     |
| Technical         | 5/10  | Clean Python, no novel patterns          |
| Uniqueness        | 4/10  | Basic feature set, expected for Phase I  |

#### DEMO READINESS (8.0/10)
| Dimension         | Score | Notes                                    |
|-------------------|-------|------------------------------------------|
| Core Workflow     | 9/10  | Clear 5-minute demo path                 |
| Reliability       | 8/10  | Error handling defined                   |
| Visual Appeal     | 7/10  | CLI can be engaging with good UX         |
| Impressiveness    | 8/10  | Clean execution will impress judges      |

### Scoring Risks (High Impact)

1. [CRITICAL] Innovation Score Floor
   - Risk: Basic todo apps score 4-6/10 here
   - Impact: -5 points to overall score
   - Mitigation: Emphasize clean execution, Python elegance

2. [MEDIUM] Edge Case Ambiguity
   - Risk: Judges may test unhandled cases
   - Impact: Demo failure risk
   - Mitigation: Add explicit edge case handling to spec

3. [LOW] Testability Gaps
   - Risk: ACs hard to verify independently
   - Impact: Execution score ceiling
   - Mitigation: Define integration test approach

### High-Impact Improvements

| Improvement | Effort | Score Impact | Priority |
|-------------|--------|--------------|----------|
| Add demo script with colors | Low | +0.5 demo | HIGH |
| Document Python patterns used | Low | +0.3 execution | MEDIUM |
| Add edge case tests to tasks | Medium | +0.5 reliability | HIGH |
| Create impressive error messages | Low | +0.3 innovation | LOW |

### Recommendations Before Implementation

1. **High Priority**
   - [ ] Add demo walkthrough to plan
   - [ ] Define all edge cases explicitly
   - [ ] Create simple CLI UX with feedback

2. **Medium Priority**
   - [ ] Document Python idioms used
   - [ ] Plan 5-minute demo script
   - [ ] Define success metrics for each feature

### Pass/Fail Thresholds

| Grade | Score Range | Recommendation |
|-------|-------------|----------------|
| A | 80-100% | Ready for implementation |
| B | 65-79% | Proceed with improvements noted |
| C | 50-64% | Address critical risks first |
| D | 35-49% | Major revisions required |
| F | 0-34% | Reconsider scope and approach |

**Current Grade: B (Strong)** - Ready to proceed with improvements.
```

### Phase 7: Provide Action Items

Based on scoring gaps, generate prioritized action items:

**High Impact (Score +2+):**
- Demo script and UX polish
- Explicit edge case coverage
- Clear 5-minute walkthrough

**Medium Impact (Score +1-2):**
- Python idiom documentation
- Error message quality
- README and presentation

**Low Impact (Score +0-1):**
- Code comments
- Minor UX improvements
- Additional validation

## Failure Handling

| Scenario | Handling |
|----------|----------|
| Missing constitution | Use default Phase I constraints |
| Missing spec | Fail; spec required for scoring |
| Missing plan | Warn; score with available info |
| All files present | Generate full scoring report |
| Low score (<50%) | Strongly recommend revisions |

## Owned By

**hackathon-review-agent** - Primary judge simulator and scoring predictor

## Reusability

This skill is semi-deterministic:
- Scoring formulas are fixed
- Category scores depend on document quality
- Improvement recommendations are rule-based
- Overall grade is computed deterministically

## Examples

### Full Scoring Simulation
```
Skill: sp.simulate-judge-scoring
Constitution: .specify/memory/constitution.md
Spec: specs/todo-app/spec.md
Plan: specs/todo-app/plan.md
```

### Quick Pre-Implementation Check
```
Skill: sp.simulate-judge-scoring
Spec: specs/todo-app/spec.md
Plan: specs/todo-app/plan.md
```

### With Custom Weights
```
Skill: sp.simulate-judge-scoring
Constitution: .specify/memory/constitution.md
Spec: specs/todo-app/spec.md
Plan: specs/todo-app/plan.md
Weights: {"clarity": 30, "execution": 30, "innovation": 15, "demo": 25}
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
