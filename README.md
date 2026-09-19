# FTP_MachLe — Machine Learning practical works

## Structure

```
FTP_MachLe/
├── README.md              # this file
├── .gitignore             # shared, covers every PW
└── PW1/                   # one folder per PW = one deliverable
    ├── README.md          # what this PW covers, how to run it
    ├── pyproject.toml     # declared dependencies for THIS PW
    ├── uv.lock            # exact resolved versions
    ├── .python-version    # Python version for THIS PW
    ├── pw1.ipynb          # the report
    └── pw_resources/      # assignment PDF, datasets, provided notebooks
```

Each PW pins its own dependencies.

## Getting started

```bash
git clone <this repo>
cd FTP_MachLe/PW1
uv sync            # creates .venv, installs the exact locked versions
uv run jupyter lab # or point your IDE at PW1/.venv/bin/python
```

`uv sync` installs the right Python version too.

## Daily commands

| Task | Command |
|---|---|
| Add a library | `uv add scikit-learn` |
| Remove one | `uv remove scikit-learn` |
| Run something in the env | `uv run jupyter lab` / `uv run python script.py` |
| Restore the env from the lock | `uv sync` |
| See what is installed and why | `uv tree` |

Always run these from inside the PW folder — that is what selects which project you
are touching. Never `pip install` into `.venv` by hand: it is not recorded in the lock.

## Starting a new PW

```bash
mkdir PW2 && cd PW2
uv init --bare --python 3.13   # minimal pyproject.toml, no packaging scaffolding
uv python pin 3.13             # writes .python-version
uv add ipykernel matplotlib numpy pandas
mkdir pw_resources
```

## Handing in a PW

The notebook is usually the deliverable. A grader must be able to read it **without running it**, which means every
cell executed in order and every figure embedded in the `.ipynb`.

```bash
cd PW1
# Kernel -> Restart Kernel and Run All Cells, save, then:
uv run python ../check_report.py pw1.ipynb
```

`check_report.py` refuses a notebook whose cells were not all run in order, whose
plotting cells stored no image, or that asks for a backend other than `%matplotlib
inline`.

If a runnable environment is also requested:

- Graders using uv: `uv.lock` is already committed — `uv sync` reproduces it exactly.
- Graders using pip: export a compatibility file first.

```bash
uv export --format requirements.txt --no-hashes -o requirements.txt
```
