class liberary:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict = {}
    def displayBooks(self):
        print(f"we have books in a liberary: {self.name}")
        for book in self.booklist:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lender book database has updated. You can take the book")
        else:
            print(f"book is alredy being used by {self.lendDict[book]}")
    def addBook(self,book):
        self.booklist.append(book)
        print("Book has been added in book list")

    def returnBook(self,book):
        self.lendDict.pop(book)


if __name__ == '__main__':

    Rk = liberary(['python','HTML','CSS','JAVA','Bad boy'],"RK")

    while(True):
        print(f"Welcome to the {Rk.name} liberary")
        print("1. Display books")
        print("2. Lend books")
        print("3. Add books")
        print("4. Return books")
        print("Enter your choice")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("plz enter right choice")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice==1:
            Rk.displayBooks()
        elif user_choice==2:
            book = input("enter the name of book you land:")
            user = input("enter your name")
            Rk.lendBook(user,book)

        elif user_choice==3:
            book = input("enter the name of book you want to add:")
            Rk.addBook(book)
        elif user_choice==4:
            book = input("enter the name of book you want to return:")
            Rk.returnBook(book)

        else:
            print("Not valid option")

        print("Press q to quit and  C to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 =="q":
                exit()
            elif user_choice2 =="c":
                continue