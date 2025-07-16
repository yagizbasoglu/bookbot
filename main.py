import sys
from stats import number_words
from stats import get_book_text
from stats import count_characters
from stats import sorting



def main():


    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        book_path = sys.argv[1]





    n = get_book_text(book_path)
    y = number_words(n)

    print (f"{y} words found in the document")

    z = count_characters(n)

    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}...")
    print ("----------- Word Count ----------")
    print (f"Found {y} total words")
    print ("--------- Character Count -------")

    k = sorting(z)
    for x in k:
        print(f"{x['char']}: {x['num']}")
        



    print("============= END ===============")

main()