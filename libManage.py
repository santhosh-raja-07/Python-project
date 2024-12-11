class libary():
    def __init__(self , lists):
        self.book_list = lists
        self.available_book_list = lists[:]
        self.books_lent = {}
        
    def display_available_books(self):
       for book in self.available_book_list:
           print(book)
    def display_all_books(self):
        for books in self.book_list:
            print(books)
    def books_lend(self , name , book):
        if book not in self.book_list:
            print("Incorrect book name. Please check the book list")
            return
        if book in self.book_list:
            lib.books_lent.update({book : name})
            lib.available_book_list.remove(book)
            print("You can take the book")
        else:
            print("The book is already taken by" + self.books_lent[book])
    def return_book(self , book):
        del self.books_lent[book]
        self.available_book_list.append(book)
    
if __name__ == "__main__":
    lib = libary(["To Kill a Mockingbird" , "The Great Gatsby" , "The Alchemist" , "Harry Potter and the Sorcerer’s Stone" , "The Hobbit" , "Becoming"])
    print("Welcome to Libary. Enter an option. ")
    
    while True:
        print("1 = Display available books")
        print("2 = Display all books")
        print("3 = Borrow a book")
        print("4 = Return a book")
        print("5 = Quit")
        
        user_inp = int(input())
        if user_inp == 1:
            lib.display_available_books()
        elif user_inp == 2:
            lib.display_all_books()
        elif user_inp == 3:
            name = input("Enter Your Name : ")
            book = input("Enter Book Name : ")
            lib.books_lend(name,book)
        elif user_inp == 4:
            book = input("Enter Book Name : ")
            lib.return_book(book)
        elif user_inp == 5:
            break
        else:
            print("invalid input")