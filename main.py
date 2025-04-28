import sys

from stats import get_num_char, get_num_words, sort_dict


def main():
    file_path = "/home/thomas/github/workspace/github.com/Thomas-Lec/bookbot/books/frankenstein.txt"
    file_path = check_if_book_is_provided(sys.argv)
    content = get_book_text(file_path)
    num_words = get_num_words(content)
    num_char = get_num_char(content)
    sorted_dict = sort_dict(num_char)

    # Print the header
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    # Print the word count section
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Print the character count section
    print("--------- Character Count -------")
    # Here you'd loop through your characters and print them
    for i in sorted_dict:
        char = i["char"]
        num = i["num"]
        print(f"{char}: {num}")

    # Print the footer
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def check_if_book_is_provided(cmd_command):
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    book_path = sys.argv[1]

    return book_path

main()

