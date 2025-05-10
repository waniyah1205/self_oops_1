class Book:
    total_books = 0  # Class variable to track total books
    
    @classmethod
    def increment_book_count(cls):
        # Class method to increment the count of total books
        cls.total_books += 1
        print(f"Total books: {cls.total_books}")

# Add a new book
Book.increment_book_count()  # Output: Total books: 1
Book.increment_book_count()  # Output: Total books: 2
