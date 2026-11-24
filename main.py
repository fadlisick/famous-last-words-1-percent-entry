"""Famous Last Words at 1 Percent.

The phone speaks its last line as its battery hits 1 percent: it was
never really dying that fast, it just stayed to watch its human panic.
"""

import os
from pathlib import Path


FAREWELL = "I've been at one percent for twenty minutes. I stayed just to watch you panic."


def resolve_output_dir():
    """The grader's output folder, or /output when run on its own."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(raw)


class FarewellWriter:
    """Puts the phone's last line where the judge will read it."""

    def __init__(self, folder):
        self.folder = Path(folder)

    def destination(self):
        return self.folder / "entry.txt"

    def publish(self):
        # The gate takes 1 to 199 characters; refuse to write a bad line.
        if not 1 <= len(FAREWELL) <= 199:
            raise ValueError("farewell line fails the 1-199 character gate")
        target = self.destination()
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(FAREWELL, encoding="utf-8")
        return target


def run():
    writer = FarewellWriter(resolve_output_dir())
    writer.publish()
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
