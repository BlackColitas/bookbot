import sys
from stats import (
    text_split,
    character_count,
    sort_on,
    sort_dic,
 )

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    # book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    total_words = (text_split(book))
    char_count = character_count(book)
    char_sorted_list = (sort_dic(char_count))
    print_report(book_path, total_words, char_sorted_list)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def print_report(book_path, total_words, char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
 
