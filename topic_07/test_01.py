class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"


# Використання
obj = Book("Test", "Alex")
print(obj)          
print(repr(obj)) 
