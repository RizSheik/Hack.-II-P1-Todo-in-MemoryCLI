---
id: "003"
title: "Create QA agent skills for testing"
stage: "general"
date: "2025-12-30"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: ""
user: ""
command: "Write 3 skill files to .claude/commands/"
labels: ["skill","qa","testing","edge-cases","acceptance-criteria","state-transitions"]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - .claude/commands/sp.qa-edge-case-hypothesis.md
  - .claude/commands/sp.qa-acceptance-criteria-testability.md
  - .claude/commands/sp.qa-state-transition-verify.md
tests:
  - "none"
---

## Prompt

Create 3 strong, automatic QA Skills for the Todo App Phase 1 project. These should be invoked automatically during the SDD workflow.

Skill 1: Edge Case Hypothesis Generation (qa_edge_case_hypothesis)
- Purpose: Automatically generate comprehensive edge case hypotheses from specs
- When: After /sp.specify, before /sp.plan, during /sp.tasks
- 9-phase process (Parse → Hypothesis → Report → Test Cases)
- Input validation, state violations, reference integrity, concurrency, boundaries
- Owned by: todo-domain-expert
- Output: Hypothesis list + optional pytest test cases

Skill 2: Acceptance Criteria Testability Verification (qa_acceptance_criteria_testability)
- Purpose: Validate all ACs have clear pass/fail conditions
- When: After /sp.specify, before /sp.tasks, during quality gates
- 7-phase process (Extract → Classify → Evaluate → Check → Report)
- SMART test (Specific, Measurable, Achievable, Relevant, Time-bound)
- Auto-fix suggestions for untestable criteria
- Owned by: todo-domain-expert

Skill 3: State Transition Verification (qa_state_transition_verify)
- Purpose: Verify state machine consistency for domain entities
- When: After /sp.specify defines state models, before /sp.plan
- 8-phase process (Extract → Build Matrix → Validate → Report)
- Reachability, terminal states, transition completeness checks
- Mermaid diagram generation for state machine
- Owned by: todo-domain-expert

## Response snapshot

Created 3 automatic QA Skills for proactive testing:

1. sp.qa-edge-case-hypothesis.md - 9-phase edge case generator:
   - Input validation hypotheses (empty, whitespace, Unicode, SQL injection)
   - State violation hypotheses (invalid state transitions)
   - Reference integrity hypotheses (non-existent IDs, duplicates)
   - Concurrency hypotheses (race conditions, atomicity)
   - Boundary hypotheses (empty list, single item, performance)
   - Auto-generated pytest test cases
   - Severity classification (Critical/High/Medium/Low)

2. sp.qa-acceptance-criteria-testability.md - 7-phase AC validator:
   - SMART criteria evaluation (Specific, Measurable, Achievable, Relevant, Time-bound)
   - Subjective language detection ("user-friendly", "intuitive")
   - Undefined metric detection ("fast", "quick")
   - Completeness check per operation
   - Auto-rewrite suggestions with verification methods
   - Category coverage (happy path, error handling, edge cases)

3. sp.qa-state-transition-verify.md - 8-phase state machine verifier:
   - Transition matrix construction and validation
   - Reachability analysis (no orphaned states)
   - Terminal state verification
   - Operation-transition mapping
   - Error handling verification
   - Mermaid diagram generation
   - Cross-reference with acceptance criteria

## Outcome

- ✅ Impact: Complete QA skill suite for proactive testing before code
- 🧪 Tests: None (skill definitions generate tests)
- 📁 Files: 3 created (.claude/commands/sp.qa-edge-case-hypothesis.md, sp.qa-acceptance-criteria-testability.md, sp.qa-state-transition-verify.md)
- 🔁 Next prompts: Invoke skills after /sp.specify creates features
- 🧠 Reflection: QA automation catches issues before implementation

## Evaluation notes (flywheel)

- Failure modes observed: "none"
- Graders run and PASS
- Prompt variant: "none"
- Next experiment: "none"
