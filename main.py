def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = ""
        for i in f:
            text += i
    return text
    # do something with f (the file) here

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    print(text)
    print(f"{num_words} words found in the document")


main()
