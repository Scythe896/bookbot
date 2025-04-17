from stats import words_amount, get_book_text, get_chars, report
import sys

def main():
    # Check for 2 arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Initialise variables
    path = sys.argv[1]
    words = words_amount(get_book_text(path))
    sorted_list = report(get_chars(get_book_text(path)))

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

main()