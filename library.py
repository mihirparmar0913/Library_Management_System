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
        self.books.append(book)  
        return True  
