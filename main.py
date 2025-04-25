import sys
from stats import get_num_words
from stats import count_characters
from stats import sort_on
from stats import sorting_dictionary



if len(sys.argv) < 2:
    sys.exit("Usage: python3 main.py <path_to_book>")



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    book = get_book_text(sys.argv[1])
    #print(book)
    num_words = get_num_words()
    #print(f"{num_words} words found in the document")
    req_dict = count_characters()
    #print(req_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    dic = sorting_dictionary()
    for i in dic:
        print(f"{i}: {dic[i]}")
    print("============= END ===============")


main()


