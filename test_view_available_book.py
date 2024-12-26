import unittest
from library import Library

class TestViewAvailableBooks(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.add_book({
            "isbn": "1234567890",
            "title": "The Show man",
            "author": "Miss Mathur",
            "publication_year": 2004,
        })
        self.library.add_book({
            "isbn": "9876543210",
            "title": "The door",
            "author": "Jems",
            "publication_year": 2005,
        })
        self.library.borrow_book("1234567890")

    def test_view_available_books(self):
        # View the list of available books
        available_books = self.library.view_available_books()        
        self.assertEqual(available_books[0]["isbn"], "9876543210")  # Validate the available book

    #Here are borrowing all the books and checkking that no book is available.
    def test_view_no_available_books(self):
        # Borrow all books to make none available
        self.library.borrow_book("9876543210")
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 0) 

if __name__ == "_main_":
    unittest.main()