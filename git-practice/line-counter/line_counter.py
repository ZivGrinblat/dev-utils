import sys
import os
from scanner import scan_folder

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    if not os.path.isdir(target_dir):
        print(f"Error: '{target_dir}' is not a valid directory.")
        sys.exit(1)

    results, total = scan_folder(target_dir)
    for name, count in results:
        print(f"{name}: {count} lines")
    print(f"\nTotal lines: {total}")
