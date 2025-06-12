import random
quotes = open("quotes.txt").read().splitlines()
print(random.shuffle(quotes))