import sys
from stats import get_num_words, get_num_characters, sorted_dictionaries

def get_book_text(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        content = get_book_text(file_path)
        num_words = get_num_words(content)
        print(f"Found {num_words} total words")
        num_characters = get_num_characters(content)
        sorted_dictionary = sorted_dictionaries(num_characters)
        print("--------- Character Count -------")
        for item in sorted_dictionary:
            if item["char"].isalpha():
                print(f'{item["char"]}: {item["num"]}')
        print("============= END ===============")
        
main()