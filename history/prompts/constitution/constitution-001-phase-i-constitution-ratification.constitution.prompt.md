---
id: "constitution-001"
title: "Phase I Constitution ratification"
stage: "constitution"
date: "2025-12-30"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: ""
user: ""
command: "/sp.constitution"
labels: ["constitution","phase1","governance","principles"]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - .specify/memory/constitution.md
tests:
  - "none"
---

## Prompt

# Phase I Constitution - Evolution of Todo (Console App)

## 1. Purpose of This Constitution

This Constitution defines the non-negotiable principles, constraints, and governance rules for Phase I of the Evolution of Todo hackathon project.

Primary purposes:
- Enforce Spec-Driven Development (SDD)
- Eliminate manual or intuitive coding ("vibe-coding")
- Ensure deterministic, judge-aligned outcomes
- Establish a single source of truth for all future specifications and implementations

## 2. Phase I Scope Definition

Phase I focuses exclusively on building a Python-based, in-memory, console Todo application.

### Explicit Inclusions
- Python programming language only
- Console-based user interaction (CLI)
- In-memory data storage (e.g., lists, dictionaries)
- Single-user usage
- Synchronous execution
- Be implementable in a single logical unit
- Be testable via console interaction
- Reference the specification section it fulfills

### Explicit Exclusions (Strictly Forbidden)
- Databases (SQL, NoSQL, files, ORMs)
- Web frameworks or APIs
- Frontend frameworks
- Authentication or authorization
- AI, LLMs, or chatbot features
- Background jobs or async processing
- External services or SDKs

## 3. Mandatory Development Workflow
/constitution → /sp.specify → /sp.plan → /sp.tasks → /sp.implement

## 4. Traceability & Accountability Rules
- Every implementation MUST map to a Task ID
- Every task MUST map to an approved specification section
- Every specification MUST comply with this Constitution

## 5. Definition of Success (Phase I)
- All core Todo operations work correctly via CLI
- Behavior is deterministic and repeatable
- Error cases are handled gracefully
- The system can be explained clearly in under 5 minutes
- Judges can easily map features to specs

## 6. Design Philosophy
- Clarity over cleverness
- Simplicity over abstraction
- Explicit behavior over implicit assumptions
- Educational readability

## 7. Task Definition Rules
A valid task MUST describe exactly one implementation unit...

## 8. Error Handling Policy
Must handle invalid menu selections, invalid task IDs, empty task titles with user-friendly messages, never crash, return to main menu.

## 9. Judge-Oriented Constraints
All decisions must consider: Spec adherence, Phase correctness, Simplicity and clarity, Deterministic behavior, Demo readiness. Over-engineering results in score penalties.

## 10. Authority & Enforcement
The todo-spec-manager agent is the final authority.

## 11. Constitution Lock
Once Phase I implementation begins, this Constitution is locked.

## Response snapshot

Created Phase I Constitution at `.specify/memory/constitution.md` with 13 sections:

1. Purpose of This Constitution - SDD enforcement, eliminate vibe-coding
2. Core Principles (I-V) - Spec-Driven Development, Single Source of Truth, Simplicity Over Abstraction, Explicit Behavior Over Implicit Assumptions, Educational Readability
3. Phase I Scope Definition - Inclusions (Python, CLI, in-memory) + Exclusions (databases, web, auth, AI, etc.)
4. Mandatory Development Workflow - /sp.constitution → /sp.specify → /sp.plan → /sp.tasks → /sp.implement
5. Traceability & Accountability Rules - Task ID requirement, spec compliance
6. Definition of Success (Phase I) - 5 criteria including 5-minute demo rule
7. Design Philosophy - Clarity, Simplicity, Explicit Behavior, Educational Readability
8. Task Definition Rules - Single unit, testable acceptance criteria, reference spec section
9. Error Handling Policy - User-friendly errors, no crashes, return to menu
10. Judge-Oriented Constraints - 5 criteria, over-engineering penalties
11. Authority & Enforcement - todo-spec-manager as final authority
12. Constitution Lock - Locked after implementation begins
13. Governance - Amendment procedure, versioning policy, compliance review

Sync Impact Report included at top documenting version change N/A→1.0.0.

## Outcome

- ✅ Impact: Complete governance framework for Phase I SDD workflow
- 🧪 Tests: None (governance document)
- 📁 Files: 1 modified (.specify/memory/constitution.md)
- 🔁 Next prompts: /sp.specify to create feature specification
- 🧠 Reflection: Constitution enables deterministic, judge-aligned development

## Evaluation notes (flywheel)

- Failure modes observed: "none"
- Graders run and PASS
- Prompt variant: "none"
- Next experiment: "none"
