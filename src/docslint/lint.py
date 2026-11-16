"""Structural checks for Markdown text. Pure functions, no I/O.

Checks:
- exactly one H1 heading
- heading levels never skip (e.g. H1 -> H3)
- no trailing whitespace
- file ends with exactly one newline
"""

from __future__ import annotations

import re
from dataclasses import dataclass

_HEADING = re.compile(r"^(#{1,6})\s+\S")


@dataclass(frozen=True)
class Issue:
    line: int
    rule: str
    message: str


def lint_markdown(text: str) -> list[Issue]:
    issues: list[Issue] = []
    lines = text.split("\n")
    h1_count = 0
    prev_level = 0
    for i, line in enumerate(lines, start=1):
        if line != line.rstrip():
            issues.append(Issue(i, "trailing-whitespace", "Line has trailing whitespace."))
        m = _HEADING.match(line)
        if m:
            level = len(m.group(1))
            if level == 1:
                h1_count += 1
            if prev_level and level > prev_level + 1:
                issues.append(
                    Issue(i, "heading-skip", f"Heading level jumps from {prev_level} to {level}.")
                )
            prev_level = level
    if h1_count != 1:
        issues.append(Issue(1, "single-h1", f"Document must have exactly one H1 (found {h1_count})."))
    if not text.endswith("\n") or text.endswith("\n\n"):
        issues.append(Issue(len(lines), "final-newline", "File must end with exactly one newline."))
    return issues
