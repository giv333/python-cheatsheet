from library.book import Book, BorrowedBook

# Create normal book
book1 = Book("1984", "George Orwell", 1949)
book1.display_info()

# Create borrowed book
borrowed = BorrowedBook("The Alchemist", "Paulo Coelho", 1988, "DeboX")
borrowed.display_borrower()
