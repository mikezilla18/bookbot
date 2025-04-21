# stats.py

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    result = {}
    for char in text.lower():
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def sort_letters(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():  # Skip non-alphabetical characters
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=lambda d: d["num"])
    return sorted_list  # Fixed the typo here
