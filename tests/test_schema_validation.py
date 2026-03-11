from pathlib import Path

from scripts.validate_examples import run_validation


def test_all_examples_and_fixtures_validate_as_expected() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    summary = run_validation(repo_root)
    assert summary["failed"] == 0
    assert summary["passed"] == summary["checked"]
