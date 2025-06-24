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

def sort_char(char_dict):
    list_dict = []
    for char in char_dict:
        if char.isalpha():
            count = char_dict[char]
            list_dict.append({"char": char, "num": count})
    list_dict.sort(reverse=True, key=lambda x: x["num"])
    return list_dict

def common_word_count(text):
    words = text.lower().split()
    common_words = {"said", "more", "man", "other"}
    count = 0
    for word in words:
        clean_word = word.strip(".,?!'/")
        if clean_word in common_words:
            count += 1
    return count

def top_word(text):
    counted_words = {}
    words = text.lower().split()
    for word in words:
        clean_word = word.strip(".,?!'/")
        if clean_word in counted_words:
            counted_words[clean_word] += 1
        else:
            counted_words[clean_word] = 1
    return max(counted_words, key=lambda x: counted_words.get(x))