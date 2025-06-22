from stats import count_words
from stats import count_characters

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
    print(text)
    print(f"{num_words} words found in the document")
    char_count = count_characters(text)
    print(char_count)



main()
