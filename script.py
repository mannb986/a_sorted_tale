import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

# This prints a list of all titles in the bookshelf
# for book in bookshelf:
#     print(book['title_lower'])

bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

# Defining different comparison sort function 
def by_title_ascending(book_a, book_b):
    if book_a['title_lower'] > book_b['title_lower']:
        return True
    else:
        return False

def by_author_ascending(book_a, book_b):
    if book_a["author_lower"] > book_b['author_lower']:
        return True
    else:
        return False

# def by_total_length()

# Running the different sort alogrithms with different comparison functions
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
    print(book['title_lower'])

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort_2:
    print(book['author_lower'])

sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1, by_author_ascending)
for book in bookshelf_v2:
    print(book['author_lower'])


