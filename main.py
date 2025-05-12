import sys
from stats import char_count
from stats import word_count
from stats import sorted_characters

def get_book_text(book):
    with open(book) as f:
    	file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text =  get_book_text(sys.argv[1])

    count = word_count(book_text)

    characters = char_count(book_text)

    sorted_chars = sorted_characters(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        num = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

main()

