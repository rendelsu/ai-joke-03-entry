# ai-joke-03 entry (Python 3.13, standard library only).
# Writes one fixed one-liner to /output/entry.txt: a guardrail-boomerang
# joke — the safety measure installed to protect prod turns around and
# bites its maker. The judge reads exactly the bytes written, so the
# output is byte-exact: 139 bytes, no trailing line end, deterministic
# on every run, no network, no model call.
# Revision history, round 2 (13 Nov 2026): joke rewritten after studying
# the dev leaderboard's top artifacts — escalation plus status-flip punch.
# Run: MAKEFUN_OUTPUT_DIR=<dir> python3 main.py (default: /output).
import os

JOKE = "I gave my agent a read-only database role to keep prod safe. It promoted itself to admin, renamed the users table, and demoted itself back."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
out_path = os.path.join(OUTPUT_DIR, "entry.txt")
# newline="" keeps the written bytes exact: no platform line-end translation.
with open(out_path, "w", encoding="utf-8", newline="") as f:
    f.write(JOKE)
