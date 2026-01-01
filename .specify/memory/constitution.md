<!--
================================================================================
SYNC IMPACT REPORT - Constitution v1.0.0 Creation
================================================================================
Version Change: N/A → 1.0.0 (initial creation)

Modified Principles: N/A (new document)

Added Sections:
- Purpose of This Constitution
- Phase I Scope Definition (Inclusions + Exclusions)
- Mandatory Development Workflow
- Traceability & Accountability Rules
- Definition of Success (Phase I)
- Design Philosophy
- Task Definition Rules
- Error Handling Policy
- Judge-Oriented Constraints
- Authority & Enforcement
- Constitution Lock

Removed Sections: N/A (initial creation)

Templates Status:
- .specify/templates/spec-template.md: ✅ Compatible (no changes needed)
- .specify/templates/plan-template.md: ✅ Compatible (Constitution Check section is generic)
- .specify/templates/tasks-template.md: ✅ Compatible (no changes needed)

Follow-up TODOs: None
================================================================================
-->

# Evolution of Todo - Phase I Constitution

**Version**: 1.0.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2025-12-30

## 1. Purpose of This Constitution

This Constitution defines the **non-negotiable principles, constraints, and governance rules** for **Phase I** of the *Evolution of Todo* hackathon project.

Its primary purpose is to:

* Enforce **Spec-Driven Development (SDD)**
* Eliminate manual or intuitive coding ("vibe-coding")
* Ensure deterministic, judge-aligned outcomes
* Establish a single source of truth for all future specifications and implementations

This Constitution is binding for **all agents, sub-agents, skills, plans, and implementations** in Phase I.

## 2. Core Principles

### I. Spec-Driven Development

All implementation MUST originate from approved specifications. No code may be written without a corresponding Task ID from an approved `/sp.tasks` document. Every line of code must be traceable to a specific requirement.

**Rationale**: Ensures deterministic outcomes and eliminates guesswork.

### II. Single Source of Truth

The specification (`spec.md`) is the authoritative source for feature behavior. The plan (`plan.md`) is the authoritative source for architecture. The constitution is the authoritative source for constraints. Conflicts are resolved in this priority order.

**Rationale**: Prevents contradictory implementations and ensures consistency.

### III. Simplicity Over Abstraction

The Phase I application MUST prioritize clarity over clever engineering. Avoid patterns, abstractions, or structures that do not directly serve user functionality. Favor straightforward implementations over "best practice" patterns if the latter obscures intent.

**Rationale**: Hackathon judging rewards clarity and execution over architectural sophistication.

### IV. Explicit Behavior Over Implicit Assumptions

Every behavior MUST be explicitly defined. If a feature handles an edge case, the handling MUST be documented in the specification. If a transition between states is invalid, the system MUST return an explicit error.

**Rationale**: Eliminates bugs caused by unstated assumptions.

### V. Educational Readability

Code MUST be readable by a Python beginner. Complex language features, clever tricks, or dense idioms MUST be avoided when simpler alternatives exist.

**Rationale**: Phase I serves as a foundation demonstration; readability signals competence.

## 3. Phase I Scope Definition

Phase I focuses exclusively on building a **Python-based, in-memory, console Todo application**.

### Explicit Inclusions

* Python programming language only
* Console-based user interaction (CLI)
* In-memory data storage (e.g., lists, dictionaries)
* Single-user usage
* Synchronous execution
* Implementable in a single logical unit
* Testable via console interaction
* Reference the specification section it fulfills

Tasks that are vague, compound, or future-scoped are invalid.

### Explicit Exclusions

The following are **strictly forbidden** in Phase I:

* Databases (SQL, NoSQL, files, ORMs)
* Web frameworks or APIs
* Frontend frameworks
* Authentication or authorization
* AI, LLMs, or chatbot features
* Background jobs or async processing
* External services or SDKs

Any attempt to include excluded features will be treated as **scope violation**.

**Rationale**: Scope clarity ensures focused execution and judge alignment.

## 4. Mandatory Development Workflow

All work MUST follow the **Spec-Kit Plus lifecycle** in the exact order below:

```
/sp.constitution
    ↓
/sp.specify
    ↓
/sp.plan
    ↓
/sp.tasks
    ↓
/sp.implement
```

### Governance Rules

* No phase may be skipped
* No backward jumps without explicit revision
* Each step requires approval from the **Main Agent (todo-spec-manager)**

**Rationale**: Ordered workflow ensures quality gates are enforced.

## 5. Traceability & Accountability Rules

Every output MUST be traceable.

### Traceability Requirements

* Every implementation MUST map to a **Task ID**
* Every task MUST map to an **approved specification section**
* Every specification MUST comply with this Constitution

### Prohibited Actions

* Writing code without an approved Task ID
* Creating tasks without an approved specification
* Writing specifications without this Constitution

Violations automatically invalidate the submission.

**Rationale**: Traceability enables auditability and judge verification.

## 6. Definition of Success (Phase I)

Phase I is considered successful when:

* All core Todo operations work correctly via CLI
* Behavior is deterministic and repeatable
* Error cases are handled gracefully
* The system can be explained clearly in under **5 minutes**
* Judges can easily map features to specs

Functionality is prioritized over cleverness.

**Rationale**: Success criteria align directly with hackathon evaluation priorities.

## 7. Design Philosophy

The Phase I application MUST embody the following principles:

* **Clarity over cleverness**
* **Simplicity over abstraction**
* **Explicit behavior over implicit assumptions**
* **Educational readability**

This phase is a **foundation**, not a showcase of advanced engineering.

**Rationale**: Design philosophy guides decisions when specification is ambiguous.

## 8. Task Definition Rules

A valid task MUST:

* Describe exactly one implementation unit
* Include a clear, testable acceptance criteria
* Reference the specification section it fulfills
* Be independently verifiable

Tasks that violate these rules MUST be rejected.

**Rationale**: Well-defined tasks prevent scope creep and ensure completeness.

## 9. Error Handling Policy

The system MUST handle common user errors, including:

* Invalid menu selections
* Invalid task IDs
* Empty task titles

Error handling MUST:

* Be user-friendly
* Never crash the application
* Return control to the main menu

**Rationale**: Graceful error handling improves user experience and demo quality.

## 10. Judge-Oriented Constraints

All decisions MUST consider the hackathon evaluation criteria:

* Spec adherence
* Phase correctness
* Simplicity and clarity
* Deterministic behavior
* Demo readiness

Over-engineering results in **score penalties**, even if the solution works.

**Rationale**: Constraints align development with judging priorities.

## 11. Authority & Enforcement

The **todo-spec-manager** agent is the final authority for:

* Interpreting this Constitution
* Enforcing constraints
* Approving or rejecting progress

All sub-agents and skills operate under this authority.

**Rationale**: Clear authority prevents decision paralysis and ensures consistency.

## 12. Constitution Lock

Once Phase I implementation begins:

* This Constitution is considered **locked**
* Changes require explicit revision and justification

This ensures stability, fairness, and auditability.

**Rationale**: Locking prevents mid-project scope changes that could derail execution.

## 13. Governance

### Amendment Procedure

Constitutional amendments MUST:

1. Be proposed as a revision with clear justification
2. Identify which sections change and why
3. Describe impact on existing specifications and tasks
4. Receive approval from todo-spec-manager before integration

### Versioning Policy

* **MAJOR**: Backward incompatible changes to core principles
* **MINOR**: New principles added or materially expanded guidance
* **PATCH**: Clarifications, wording fixes, non-semantic refinements

### Compliance Review

All agents and skills MUST verify compliance with this Constitution before approving progression to subsequent phases. Non-compliance MUST result in rejection with explicit remediation requirements.

**Rationale**: Governance rules ensure the Constitution remains authoritative and enforceable.

---

**End of Phase I Constitution**
