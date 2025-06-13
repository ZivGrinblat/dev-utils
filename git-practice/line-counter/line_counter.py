# line_counter.py

import os

for filename in os.listdir():
    if filename.endswith(".txt"):
        with open(filename) as f:
            lines = f.readlines()
            print(f"{filename}: {len(lines)} lines")
