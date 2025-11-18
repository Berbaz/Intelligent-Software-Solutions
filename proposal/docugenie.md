
# DocuGenie — AI Automated Documentation Assistant

## Purpose
DocuGenie automatically generates and updates software documentation from code, tests, and commit history. It ensures documentation always stays aligned with the current state of the codebase.

## Key Features
- Extracts function/class signatures and examples.
- Generates API references, guides, and architecture diagrams (Mermaid).
- Posts documentation diffs on pull requests.
- Integrates with CI/CD pipelines.

## Workflow
1. Developer opens a pull request.
2. CI runs DocuGenie and scans modified files.
3. Draft documentation is generated automatically.
4. Team reviews and approves documentation updates.
5. Docs are published on merge.

## Impact
- Reduces documentation debt.
- Improves onboarding for new developers.
- Keeps technical knowledge consistent across teams.
