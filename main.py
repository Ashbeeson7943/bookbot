import sys
from stats import get_word_count, get_character_count, sort_character_count

def get_book_text(book_filepath):
    book_contents = ""
    with open(book_filepath) as book:
        book_contents = book.read()
    return book_contents 

def display_report(word_count, sorted_character_count):
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {word_count} total words\n--------- Character Count -------")
    for count in sorted_character_count:
        print(f"{count["char"]}: {count["num"]}")
    print(f"============= END ===============")


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_filepath = sys.argv[1] 

    book_text = get_book_text(book_filepath)

    word_count = get_word_count(book_text)

    character_count = get_character_count(book_text)
    sorted_character_count = sort_character_count(character_count)

    display_report(word_count, sorted_character_count)


main()