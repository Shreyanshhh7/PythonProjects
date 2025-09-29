class library:
    def __init__(self,no_of_books):
        self.no_of_books = 0
        self.books =[]
    
    def add_books(self, book , n):
        for i in range(n):
            self.books.append(book)
            self.no_of_books+=1
    
    def print_books(self):
        for i in range(self.no_of_books):
            print(self.books)
    
    def get_no_of_books(self):
        print(self.no_of_books)

a= library(0)
a.add_books(input("enter your book"))
a.print_books()
a.get_no_of_books()
