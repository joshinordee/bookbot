def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text):
    lower_text = text.lower()
    s = {}
    for i in lower_text:
        if i not in s:
            s[i] = 1
        else:
            s[i] += 1
    return s
