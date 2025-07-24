class Library:
    def __init__(self):
       self.no_of_books  = 0
       self.books = {}
    
    def print_books(self):
        print("Books:")
        for book, category in self.books.items():
            print("book name: ", book, "Category:", category)

    def add_book(self, book, category):
        self.books[book] = category
        self.no_of_books += 1

    def get_no_of_books(self):
        return self.no_of_books
    

library1 = Library()
print("Initial number of books: ", library1.get_no_of_books())

while True:
        book = input( "Enter a book name (enter 'q' to exit and get the total info): ")
        if book == 'q':
            break
        category = input(  "Enter the category of the book: ")
        library1.add_book(book, category)

print("Final number of books:", library1.get_no_of_books())
       
       
library1.print_books()

