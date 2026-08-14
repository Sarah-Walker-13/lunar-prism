"""Tests for lunar-prism."""
from lunar.core import run


def test_run():
    result = run()
    assert result.ok
