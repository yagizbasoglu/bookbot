from stats import number_words
from stats import get_book_text
from stats import count_characters


def main():

    n = get_book_text("books/frankenstein.txt")
    y = number_words(n)

    print (f"{y} words found in the document")

    z = count_characters(n)

    print (z)
   

main()