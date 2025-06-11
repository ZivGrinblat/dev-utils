import random

quotes = [
    "The only limit is the one you set yourself.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Simplicity is the soul of efficiency."
]

def print_random_quote(uppercase=False):
    quote = random.choice(quotes)
    if uppercase:
        quote = quote.upper()
    print(quote)

def print_quotes_with(word):
    print(f"Quotes containing the word '{word}':")
    found = False
    for sentence in quotes:
        if word.lower() in sentence.lower():
            print("--", sentence)
            found = True
    if not found:
        print("No matching quotes found.")

def print_sorted_quotes(reverse=False):
    sorted_quotes = sorted(quotes, reverse=reverse)
    print("Sorted quotes:" if not reverse else "Reverse sorted quotes:")
    for quote in sorted_quotes:
        print("-", quote)

def count_quotes():
    return len(quotes)

if __name__ == "__main__":
    print_random_quote()
    print_random_quote(uppercase=True)
    print_quotes_with("code")
    print_sorted_quotes()
    print("Quote count:", count_quotes())
