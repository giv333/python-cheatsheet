# Python File Scanner

A beginner-friendly tool to scan a folder and find all `.py` files using `pathlib`.

---

##  What It Does

- Asks the user to enter a folder name
- Searches that folder for Python (`.py`) files — including all subfolders
- Lists each file and counts how many were found

---

##  What You’ll Practice

| Concept            | Description                                 |
|--------------------|---------------------------------------------|
| `pathlib.Path()`   | Handles paths like objects                  |
| `path.exists()`    | Checks if a folder or file exists           |
| `path.is_dir()`    | Makes sure it's a directory                 |
| `path.rglob('*.py')`| Recursively finds all `.py` files in folder |
| `file.name`        | Gets the name of each file only             |

---

##  How to Run

```bash
python scanner.py
