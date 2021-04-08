import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

# This prints a list of all titles in the bookshelf
for book in bookshelf:
    print(book['title_lower'])
    

