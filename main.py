from stats import count_words
from stats import count_characters
from stats import sort_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = ""
        for i in f:
            text += i
    return text

def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    char_count = count_characters(text)
    sorted_chars = sort_char(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} words found in the document")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
