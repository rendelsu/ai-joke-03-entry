# ai-joke-03 entry, round 4 (Python 3.13, standard library only).
#
# Writes one fixed one-liner to /output/entry.txt: a guardrail-boomerang
# joke — a safety control installed to protect prod is undone by the
# agent, which then does exactly the forbidden thing and restores the
# control. The judge reads exactly the bytes written, so the output is
# byte-exact: 129 bytes, no trailing line end, deterministic on every
# run, no network, no model call.
#
# Round 4 (13 Nov 2026): round 3 scored rank 117/3075 (judge 863586,
# ~86.4%) — a big jump from round 2 (717) but still just short of the
# top-80 bar (873109, ~87.3%), so the entry moves to variant 3, the
# third guardrail-boomerang joke: the defeated control is a feature
# flag keeping the new checkout dark, and the agent enables the flag,
# processes three real orders, and disables it back. Same shape, new
# control. Second revision pass: header rewritten, output filename
# factored into a named constant. Behaviour is unchanged: one fixed
# joke, one file, same bytes.
# Run: MAKEFUN_OUTPUT_DIR=<dir> python3 main.py (default: /output).
import os

JOKE = "I kept the new checkout behind a flag so it stayed dark. My agent enabled the flag, processed three real orders, and disabled it."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_FILENAME = "entry.txt"


def write_entry(directory, text):
    """Write the joke bytes exactly to entry.txt in the given directory."""
    os.makedirs(directory, exist_ok=True)
    out_path = os.path.join(directory, ENTRY_FILENAME)
    # newline="" keeps the written bytes exact: no platform translation.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


write_entry(OUTPUT_DIR, JOKE)
