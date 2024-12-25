import unittest
from library import Library  

class TestLibrary(unittest.TestCase):
    def setUp(self):
        pass
        self.library = Library()  

    def test_add_book(self):
        book = {
            "isbn": "1234567890",
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "publication_year": 1925,
        }
        result = self.library.add_book(book)

        # Check if the book was added successfully
        self.assertTrue(result)  
        # Here we are checking isbn of the book  
        self.assertEqual(self.library.books[len(self.library.books)-1]["isbn"], "1234567890")  


if __name__ == "__main__":
    unittest.main()