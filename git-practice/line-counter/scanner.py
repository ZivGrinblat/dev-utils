import os
from utils import is_valid_file, count_lines

def scan_folder(directory):
    results = []
    total = 0
    for filename in os.listdir(directory):
        if is_valid_file(filename):
            path = os.path.join(directory, filename)
            lines = count_lines(path)
            results.append((filename, lines))
            total += lines
    return results, total
