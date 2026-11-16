"""CLI: lint Markdown files passed as arguments; exit 1 on any issue."""

from __future__ import annotations

import sys

from .lint import lint_markdown


def main(argv: list[str] | None = None) -> int:
    paths = sys.argv[1:] if argv is None else argv
    if not paths:
        print("usage: docslint <file.md> [...]", file=sys.stderr)
        return 2
    failed = False
    for path in paths:
        with open(path, encoding="utf-8") as fh:
            issues = lint_markdown(fh.read())
        for issue in issues:
            failed = True
            print(f"{path}:{issue.line}: [{issue.rule}] {issue.message}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
