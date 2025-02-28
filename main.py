import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]
from stats import char_report
from stats import get_book_text
from stats import get_num_words
book_text = get_book_text(filepath)
char_counts = char_report(book_text)
numwords = get_num_words(book_text)
print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------\nFound {numwords} total words\n--------- Character Count -------")
for char_dict in char_counts:
    character = char_dict["char"]
    count = char_dict["count"]
    print(f"{character}: {count}")
print("============= END ===============")