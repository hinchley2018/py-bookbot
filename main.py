import sys
from stats import num_word_usage, num_words
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    # print(sys.argv)
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_arg = sys.argv[1]
    s = get_book_text(file_arg)
    total_words = num_words(s)
    char_usages = num_word_usage(s)

    print(f'''============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {total_words} total words
--------- Character Count -------
''')
    for c,v in char_usages.items():
        print(f"{c}: {v}")
    print('============= END ===============')
main()
