---
id: "002"
title: "Create Phase 1 quality gate skills"
stage: "general"
date: "2025-12-30"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: ""
user: ""
command: "Write 3 skill files to .claude/commands/"
labels: ["skill","quality-gate","phase1","spec-audit","scope-creep","judge-scoring"]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - .claude/commands/sp.audit-spec-completeness.md
  - .claude/commands/sp.detect-scope-creep.md
  - .claude/commands/sp.simulate-judge-scoring.md
tests:
  - "none"
---

## Prompt

Create 3 quality gate skills for the Todo App Phase 1 project:

Skill 1: Specification Completeness Audit (audit_spec_completeness_phase1)
- Purpose: Ensure Phase I spec is complete, deterministic, and judge-ready
- When: After /sp.specify, before /sp.plan
- Inputs: constitution, spec file
- 8-phase audit process (Pre-Flight → Report)
- Owned by: todo-spec-manager

Skill 2: Scope Creep Detection (detect_scope_creep_phase1)
- Purpose: Prevent over-engineering that reduces hackathon scores
- When: During spec review, before approving plan
- Inputs: target file (spec/plan/tasks)
- Pattern-based detection for Phase I violations
- Owned by: hackathon-review-agent

Skill 3: Judge Scoring Simulation (simulate_judge_scoring_phase1)
- Purpose: Predict judge scores before code is written
- When: Before /sp.tasks, before /sp.implement
- Inputs: constitution, spec, plan
- Rubric-based scoring (Clarity/Execution/Innovation/Demo)
- Owned by: hackathon-review-agent

## Response snapshot

Created 3 production-quality quality gate skills:

1. sp.audit-spec-completeness.md - 8-phase audit:
   - Constitution compliance
   - Required features check (Add/List/Update/Complete/Delete)
   - Acceptance criteria validation
   - Edge case definition check
   - Scope purity check
   - Clarity and traceability check

2. sp.detect-scope-creep.md - 6-phase detection:
   - Phase I constraint loading
   - Forbidden pattern database (databases, auth, networking, AI)
   - Warning pattern scanner (over-engineering, config)
   - Text analysis with context validation
   - Scope report generation

3. sp.simulate-judge-scoring.md - 7-phase simulation:
   - Judge rubric loading (4 categories, 25% each)
   - Clarity score calculation (problem/solution/simplicity/docs)
   - Execution score calculation (architecture/feasibility/quality/testability)
   - Innovation score calculation (novelty/impact/technical)
   - Demo readiness score calculation
   - Comprehensive scoring report with grade

## Outcome

- ✅ Impact: Complete quality gate suite for Phase I SDD workflow
- 🧪 Tests: None (skill definitions, not implementation)
- 📁 Files: 3 created (.claude/commands/sp.audit-spec-completeness.md, sp.detect-scope-creep.md, sp.simulate-judge-scoring.md)
- 🔁 Next prompts: Use skills during spec/plan review phases
- 🧠 Reflection: Quality gates prevent costly rework and improve judge scores

## Evaluation notes (flywheel)

- Failure modes observed: "none"
- Graders run and PASS
- Prompt variant: "none"
- Next experiment: "none"
