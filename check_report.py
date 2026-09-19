"""Pre-submission check for a PW notebook.

Verifies the notebook is actually readable by a grader who never runs it:
every cell executed, in order, and every figure embedded in the file.

Usage: uv run python ../check_report.py pw1.ipynb
"""

import json
import re
import sys


def check(path):
    nb = json.load(open(path))
    code = [c for c in nb["cells"] if c["cell_type"] == "code"]
    problems = []

    backends = [
        (i, m.group(1))
        for i, c in enumerate(code)
        for m in re.finditer(r"^\s*%matplotlib\s+(\S+)", "".join(c["source"]), re.M)
    ]
    wrong = [f"cell {i}: %matplotlib {b}" for i, b in backends if b != "inline"]
    if wrong:
        problems.append(
            f"non-inline matplotlib backend ({', '.join(wrong)}) - only %matplotlib "
            "inline stores the figures in the file"
        )

    unrun = [i for i, c in enumerate(code) if c.get("execution_count") is None]
    if unrun:
        problems.append(f"{len(unrun)} code cell(s) never executed: index {unrun}")

    counts = [c["execution_count"] for c in code if c.get("execution_count") is not None]
    if counts != sorted(counts):
        problems.append(
            "cells were executed out of order "
            f"(execution_count: {counts}) - restart the kernel and run all"
        )

    draws = re.compile(
        r"(?<![\w.])(?:plt|ax|axes|fig)\s*[\.\[]|"
        r"\.(?:plot|hist|scatter|imshow|bar|boxplot|pie)\s*\(|"
        r"scatter_matrix\s*\("
    )
    plotting = [
        i
        for i, c in enumerate(code)
        if draws.search(
            "\n".join(
                l for l in "".join(c["source"]).splitlines()
                if not l.lstrip().startswith(("import ", "from ", "#"))
            )
        )
    ]
    missing = [
        i
        for i in plotting
        if not any("image/png" in (o.get("data") or {}) for o in code[i].get("outputs", []))
    ]
    if missing:
        problems.append(
            f"cell(s) {missing} look like they draw a figure but stored no image "
            "- check that %matplotlib inline is set"
        )

    figures = sum(
        1
        for c in code
        for o in c.get("outputs", [])
        if "image/png" in (o.get("data") or {})
    )

    print(f"{path}: {len(code)} code cells, {figures} embedded figure(s)")
    for p in problems:
        print(f"  PROBLEM: {p}")
    if not problems:
        print("  OK - a grader can read this without running it")
    return not problems


if __name__ == "__main__":
    targets = sys.argv[1:] or ["pw1.ipynb"]
    sys.exit(0 if all(check(t) for t in targets) else 1)
