import os
import csv
import tempfile
from solution_task2 import write_beasts_csv


def test_write_beasts_csv():
    d = {"А": 12, "Б": 5, "В": 7}
    with tempfile.NamedTemporaryFile(
        delete=False, mode="w", encoding="utf-8", newline=""
    ) as tmp:
        fname = tmp.name
    try:
        write_beasts_csv(d, fname)
        with open(fname, encoding="utf-8") as f:
            rows = list(csv.reader(f))
        assert rows == [["А", "12"], ["Б", "5"], ["В", "7"]]
    finally:
        os.remove(fname)


if __name__ == "__main__":
    test_write_beasts_csv()
    print("Test passed.")
