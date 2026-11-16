from docslint.lint import lint_markdown

GOOD = "# Title\n\n## Section\n\nText.\n"


def test_good_document():
    assert lint_markdown(GOOD) == []


def test_two_h1():
    rules = {i.rule for i in lint_markdown("# A\n\n# B\n")}
    assert "single-h1" in rules


def test_heading_skip():
    rules = {i.rule for i in lint_markdown("# A\n\n### Deep\n")}
    assert "heading-skip" in rules


def test_trailing_whitespace_and_final_newline():
    rules = {i.rule for i in lint_markdown("# A\n\nText.  \n\n")}
    assert "trailing-whitespace" in rules
    assert "final-newline" in rules
