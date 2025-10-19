import sys
from stats import get_num_words, get_num_chars, get_list_dict

def main():
    #book_path = "books/prideandprejudice.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #print(f"Found {num_words} total words")
    num_chars = get_num_chars(text)
#    print(num_chars)
    char_list = get_list_dict(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_list.sort(reverse=True, key=sort_on)
    for dictionary in char_list:
        print(f"{dictionary['char']}: {dictionary['num']}") 
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(items):
    return items["num"]

if __name__ == "__main__":
    main()
