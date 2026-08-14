"""Core logic for lunar-prism."""
from dataclasses import dataclass


@dataclass
class Result:
    ok: bool = True
    message: str = ""


def run() -> Result:
    """Run the main operation."""
    return Result()
