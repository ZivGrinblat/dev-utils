import os
import sys

def count_lines(filepath):
    with open(filepath) as f:
        return len(f.readlines())

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    for filename in os.listdir(target_dir):
        if filename.endswith(".txt"):
            full_path = os.path.join(target_dir, filename)
            print(f"{filename}: {count_lines(full_path)} lines")
