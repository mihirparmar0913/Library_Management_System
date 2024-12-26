import unittest
from library import Library  

class TestAddBook(unittest.TestCase):
    def setUp(self):
        self.library = Library()  
      
    def test_add_valid_book(self):
          #Here we are checking test case for valid book  
          book = {
              "isbn": "1234567890",
              "title": "Mystic India",
              "author": "swami harischandra",
              "publication_year": 1925,
          }
          result, message = self.library.add_book(book)
          self.assertTrue(result)
          self.assertEqual(message, "Book added successfully.")
          self.assertEqual(len(self.library.books), 1)
          self.assertEqual(self.library.books[0]["isbn"],"1234567890")

        
    def test_add_book_missing_information(self):
            #Here we are checking test case for missing fields of book
            book = {
                  "isbn": "987654021",
                  "title": "Lost World",
                  }
            result, message = self.library.add_book(book)
            self.assertFalse(result)
            self.assertEqual(message, "Missing required book information.")

    #Here we are checking test case for invalid ISBN of book
    def test_add_book_invalid_isbn(self):
       
        book = {
            "isbn": "", 
            "title": "Holy",
            "author": "Scott ",
            "publication_year": 1956,
        }
        result, message = self.library.add_book(book)
        self.assertFalse(result)
        self.assertEqual(message, "Invalid ISBN.")
    def test_duplicate_isbn(self):
        #Here we are Adding two books with the same ISBN
        book1 = {
            "isbn": "2341576890",
            "title": "Satya na prayogo",
            "author": "Mahatma Gandhi",
            "publication_year": 1949,
        }
        book2 = {
            "isbn": "2341576890", 
            "title": "The Great India",
            "author": "Mahat",
            "publication_year": 1960,
        }
        result1, _ = self.library.add_book(book1)
        result2, message = self.library.add_book(book2)
        self.assertTrue(result1)
        self.assertFalse(result2)
        self.assertEqual(message, "ISBN already exists.") 

    

if __name__ == "__main__":  
    unittest.main()