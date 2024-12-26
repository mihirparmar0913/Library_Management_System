'''
Hear we have created one library class which will be responsible for handling all library related task .
1.Add Book
'''
class Library:
    def __init__(self):
        # Hear we are taking an array of book which give all information about book.
        self.books = []   
  
    # This function is responsible for adding new book in the library. 
    def add_book(self, book):
       required_fields = {"isbn", "title", "author", "publication_year"}
       if not all(field in book for field in required_fields):
            return False, "Missing required book information."
       #checking all information which type  
       if not isinstance(book["isbn"], str) or not book["isbn"]:
            return False, "Invalid ISBN."
       if not isinstance(book["title"], str) or not book["title"]:
            return False, "Invalid title."
       if not isinstance(book["author"], str) or not book["author"]:
            return False, "Invalid author."
       if not isinstance(book["publication_year"], int) or book["publication_year"] <= 0:
            return False, "Invalid publication year."
       # Here we are Checking for duplicate ISBN
       if any(b["isbn"] == book["isbn"] for b in self.books):
            return False, "ISBN already exists."
       # Here we are making this book available as it is just added
       book["available"] = True
       self.books.append(book)  
       return True,"Book added successfully."

    def view_book(self):
         if len(self.books)==0:
              return False ,"Currently no book available"
         return self.books,"Book is available"
    
    def borrow_book(self, isbn):
        for book in self.books:
            if book["isbn"] == isbn:
                # Here will check book is available or not
                if not book["available"]:
                    return False, "Book is already borrowed."
                # Mark this book as not availbale
                book["available"] = False
                return True, "Book borrowed successfully."

        return False, "Book not found."
     
     
    
