#Class Book
class Book:
    def __init__(self, title, author, publication_year, borrowed):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = True, False

    # The function that returns True if a book is borrowed
    def borrow_book(self): Book
        borrowed_book: bool = True
        return True

    # The function that returns False if a book is not returned or nor borrowed
    def Return_book(self) -> Book
        borrowed_book: bool = False
        return False
    
    def Display_info(self):  #The function will display the information on the status of the book
        print("Title for the books:"+str( list(["Python Programming","Multimedia Systems","Computer Science","Software Engineering"  ])))
        print("Author:E.LAMBO")
        print("Year of Publication:2023")
        print("Borrowed status:Unknown")
        
class LibraryMember(Book):
    def __init__(self,title,author,publication_year,borrowed,member_id, name, borrowed_books):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books
        super().__init__(title,author,publication_year,borrowed)
        
    def Borrowed_books(self,book:Academ):   #The function that returns the book borrowed
       borrowed_book = self.borrowed_book
       return (list(borrowed_book))
        
    def Return_books(self,book):   #The function that returns the book is returned
       returned_book=returned_book.remove[x,y,z]
       return returned_book 
       
    def display_info(self):   #The function  returns the basic details concerning the library member
       print("Member ID:16748")
       print("Name:ELAINE LAMBO")
       print("Borrowed books:"+str (borrowed_book))
       print("Borrowing Status : True")

#The objects of  the class
print("~A sample of a Library Management System containing books; \n")
obj=Book(["Python Programming","Multimedia Systems","Computer Science","Software Engineering"],"E.LAMBO",2023,None)
print(obj.Display_info())

borrowed_book=input("Enter the title of the book from the list given above to borrow: ")

obj_1=LibraryMember(["Python Programming","Networking"],"E.LAMBO",2023, True,16748,"ELAINE LAMBO",borrowed_book)
print(obj_1.display_info())
 
