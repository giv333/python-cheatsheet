class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Book: {self.title} by {self.author} ({self.year})")


class BorrowedBook(Book):
    def __init__(self, title, author, year, borrower_name):
        super().__init__(title, author, year)
        self.borrower_name = borrower_name

    def display_borrower(self):
        print(f"{self.title} is borrowed by {self.borrower_name}.")
