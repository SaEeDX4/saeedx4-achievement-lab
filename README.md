# saeedx4-achievement-lab

A GitHub Achievements research lab — and home of `docslint`, a small,
tested Markdown documentation linter.

## What this is

- **Achievement research & tracking.** `ACHIEVEMENTS.md` and
  `ELIGIBILITY-MATRIX.md` record, with evidence, which GitHub Achievements
  exist, what they require, and this account's verified status. GitHub does
  not publish official thresholds and offers no Achievements API; community
  figures are always labelled unofficial, and a badge is only ever recorded
  as earned when it is observed on the profile.
- **Genuine development.** `docslint` is developed here through real issues
  and pull requests. No activity is manufactured to trigger badges: no fake
  issues, no artificial pull requests, no fabricated collaborators, no
  purchased or traded stars.
- **Discussions** are enabled for real technical questions that arise from
  this work.

## Automation transparency

Automated activity here is disclosed in commit metadata, pull request
descriptions and the `automation` label, and operates on behalf of the
repository owner under his standing authorization for this repository and
`saeedx4-contribution-engine` only.

## Development

```bash
python -m venv .venv && . .venv/bin/activate
pip install pytest
PYTHONPATH=src python -m pytest
PYTHONPATH=src python -m docslint.cli README.md
```
