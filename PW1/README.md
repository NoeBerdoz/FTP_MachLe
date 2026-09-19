# PW1 — Let's get started (2026-09-15)

Students: Noé Berdoz & Michael Strefeler

Assignment: [`pw_resources/ML-PW-01.pdf`](pw_resources/ML-PW-01.pdf)

## Content

| Exercise | Topic | Where |
|---|---|---|
| 1 | Python installation | environment setup, nothing to hand in |
| 2 | Python language in a nutshell | `pw_resources/intro-python-3.ipynb` |
| 3 | Data visualization (Iris pairwise scatter plot) | `pw1.ipynb` |
| 4 | Own examples of ML tasks | `pw1.ipynb` |
| 5 | Review questions | `pw1.ipynb` |
| 6 | Reading assignments | `pw1.ipynb` |

## Run

```bash
uv sync
uv run jupyter lab   # then open pw1.ipynb
```

Or point your IDE's interpreter at `.venv/bin/python`.

The notebook sets `%matplotlib inline`. If you switch it to `%matplotlib auto` to get
interactive windows while working (PyCharm), switch it back and re-run all cells before
committing: `auto` renders into a separate window and stores **no image** in the `.ipynb`,
so the grader would read a report without figures. Check before handing in:

```bash
uv run python ../check_report.py pw1.ipynb
```

## Data

`pw_resources/iris.txt` — 150 rows, tab-separated, with a header. Nine columns: the 4
features used in the assignment (sepal length/width, petal length/width), the `Species`
label, plus 4 derived columns (`Sepal.Area`, `Petal.Area`, `Sepal.Ratio`, `Petal.Ratio`)
that Figure 4 does not use.
