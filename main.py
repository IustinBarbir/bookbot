from stats import get_num_words
from stats import get_count
from stats import get_sorted_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file = sys.argv[1]

def main():
    get_num_words(file)
    sorted_count = get_sorted_count(file)
    for item in sorted_count:
        print(f'{item["char"]}: {item["num"]}')

main ()