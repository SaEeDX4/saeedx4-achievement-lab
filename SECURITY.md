# Security

Same policy as `saeedx4-contribution-engine`: least-privilege workflow
permissions declared per workflow, one fine-grained token scoped to exactly
the two project repositories (no Workflows permission), third-party actions
pinned by full SHA, no secrets in code or logs, and an `AUTOMATION_PAUSED`
emergency stop. Automation never deletes repositories, force-pushes, changes
permissions, adds collaborators, or spends money.
