# string_utils.py

def reverse_string(text):
    """Return the string in reverse order."""
    return text[::-1]


def count_vowels(text):
    """Count the number of vowels in a string."""
    return sum(1 for char in text.lower() if char in 'aeiou')


def capitalize_words(text):
    """Capitalize the first letter of each word."""
    return text.title()


# Demo (optional)
if __name__ == "__main__":
    sample = "hello world"
    print("Original:", sample)
    print("Reversed:", reverse_string(sample))
    print("Vowel count:", count_vowels(sample))
    print("Capitalized:", capitalize_words(sample))
