---
name: architecture-enforcement
description: Enforces reading arch.md before coding and updating it on structural changes.
---

# Architecture Enforcement Skill

## Guidelines

1. **Always Read First**: Before you make ANY modifications to the codebase (especially when writing new features, refactoring, or changing the structure), you MUST read the `arch.md` file located at the root of the project to understand the current architecture and design patterns.
2. **Keep Architecture Updated**: If your code modifications introduce a structural change (e.g., adding a new core module, changing the data flow, introducing a new database, or altering the deployment process), you MUST update `arch.md` to reflect these changes before concluding your task.

## Execution Steps
1. Upon receiving a task to modify the codebase, check if `arch.md` exists in the project root.
2. If it exists, read the contents of `arch.md` to align with the project's architectural guidelines.
3. Implement the necessary code changes according to the user's request.
4. Evaluate if the implemented changes affected the architecture described in `arch.md`.
5. If there are structural changes, edit `arch.md` to document the new structure or flow.
