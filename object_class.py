class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def describe(self):
        return f"{self.title} has {self.pages} pages"

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"


book1 = Book("The Great Gatsby", 180)
book2 = Book("Half of a Yellow Sun", 400)
book3 = Book("Moby Dick", 635)
book4 = Book("Great Expectations", 505)

books = [book1, book2, book3, book4]

for book in books:
    print(book.describe())
