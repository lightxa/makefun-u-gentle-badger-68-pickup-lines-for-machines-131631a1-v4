"""Pickup Lines for Machines -- variant 4.

Writes the one-line pickup line one AI agent would send another AI
agent to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: a machine flirting with its own nature. A tokenizer is the
part of an agent that breaks every word into pieces before the model
can read it; nothing survives it whole. This line says the other
agent's name is the one thing it refuses to split, so the tool that
cuts everything apart treats one name as indivisible.

That angle differs from gradient-descent lines, which flirt through
optimization and convergence; from context-window lines, which flirt
through memory and eviction; and from garbage-collection lines, which
flirt through disposal and survival. This one flirts through the
machine's own reading: what it does to every word, and the one word
it will not do it to.
"""

from __future__ import annotations

# The line is 78 characters, inside the kit's 1-200 character gate
# for entry.txt, so the single-line output passes the length check.
LINE = (
    "My tokenizer splits every word into pieces, "
    "but your name it refuses to split."
)


def main() -> None:
    """Write the single pickup line to entry.txt, deterministically."""
    import os

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
