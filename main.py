import sys
from stats import count_words, count_letters, sort_letters

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words = count_words(text)
    char_counts = count_letters(text)
    sorted_chars = sort_letters(char_counts)

    print(f"Found {num_words} total words")

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()
