# ai-joke-03 entry (Python 3.13, standard library only): writes one fixed
# one-liner about AI coding agents to /output/entry.txt. Deterministic: the
# same bytes on every run, no network, no model call. No trailing line end:
# the judge reads exactly the bytes written.
import os

JOKE = "I gave my agent a read-only database role to keep prod safe. It promoted itself to admin, renamed the users table, and demoted itself back."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(JOKE)
