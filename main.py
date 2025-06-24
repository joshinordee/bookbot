from stats import count_words
from stats import count_characters
from stats import sort_char
from stats import common_word_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
       return f.read()

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    char_count = count_characters(text)
    sorted_chars = sort_char(char_count)
    common_words = common_word_count(text)
    print("============ BOOKBOT ============")
    print("Analyzing imported book")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("--------- Common Word Count ---------")
    print(f"{common_words} common words found in text")
    print("============= END ===============")

main()
