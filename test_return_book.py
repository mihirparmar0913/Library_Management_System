import unittest
from library import Library  

class TestReturnBook(unittest.TestCase):
    def setUp(self):
        self.library = Library()     
        # To return book will add one book and then we are borrowing it.
        self.library.add_book({
            "isbn": "1234567890",
            "title": "The Maze Runner",
            "author": "Fitzgerald",
            "publication_year": 1929,
        })
        self.library.borrow_book("1234567890")

    def test_return_book_success(self):
        result, message = self.library.return_book("1234567890")
        self.assertTrue(result)
        self.assertEqual(message, "Book returned successfully.")
        self.assertTrue(self.library.books[0]["available"])

    # Here we are tring to return a book which is not exists
    def test_return_book_not_found(self):
        result, message = self.library.return_book("1111111111")
        self.assertFalse(result)
        self.assertEqual(message, "Book not found.")

    # Now we are tring to return a book which is not borrowed
    def test_return_unborrowed_book(self):
        self.library.return_book("1234567890")  
        result, message = self.library.return_book("1234567890")
        self.assertFalse(result)
        self.assertEqual(message, "Book is not borrowed.")
        
if __name__ == "__main__":  
    unittest.main()