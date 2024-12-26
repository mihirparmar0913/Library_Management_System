import unittest
from library import Library  

class TestBorrowBook(unittest.TestCase):
    def setUp(self):
        self.library = Library()

        book ={
                "isbn": "1234567890",
                "title": "Namste India",
                "author": "swami keshavdas",
                "publication_year": 1995,
              }
        book1 = {
                "isbn": "2341576890",
                "title": "Lords of ring",
                "author": "lord petricks",
                "publication_year": 1949,
              }
        book2 = {
                "isbn": "2341576897", 
                "title": " shikshapatri",
                "author": "Mahant",
                "publication_year": 1960,
              }
        self.library.add_book(book)
        self.library.add_book(book1)
        self.library.add_book(book2)

    #Here we are borrow an available book
    def test_borrow_book_success(self):
        result, message = self.library.borrow_book("1234567890")
        self.assertTrue(result)
        self.assertEqual(message, "Book borrowed successfully.")
        self.assertFalse(self.library.books[0]["available"])
            
    #Here will try to borrow a book that doesn't exist
    def test_borrow_book_not_found(self):
        result, message = self.library.borrow_book("1111111111")
        self.assertFalse(result)
        self.assertEqual(message, "Book not found.")  
          
    #Here we will borrow an available book first
    def test_borrow_unavailable_book(self):
        self.library.borrow_book("1234567890")
        # Try to borrow the same book again
        result, message = self.library.borrow_book("1234567890")
        self.assertFalse(result)
        self.assertEqual(message, "Book is already borrowed.")
        
if __name__ == "__main__":  
    unittest.main()