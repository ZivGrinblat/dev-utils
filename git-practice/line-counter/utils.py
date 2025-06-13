def is_valid_file(filename):
    return filename.endswith((".txt", ".py"))

def count_lines(filepath):
    with open(filepath) as f:
        return len(f.readlines())
