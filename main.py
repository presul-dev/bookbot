import sys
from stats import get_num_words, get_char_count, get_sorted_counts

def get_book_text(fp) :
    with open(fp) as f:
        return f.read()

def main():
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    words = get_num_words(book)
    char_count = get_char_count(book)
    sorted_char = get_sorted_counts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char in sorted_char:
        print(f"{char["char"]}: {char["num"]}")
    
if len(sys.argv)==1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()