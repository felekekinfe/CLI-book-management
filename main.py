def main():
    booklist=[]
    file=open('books.txt','r')
    line=file.readline()

     

    
    choice=0
    while choice!=4:
        print("** Books Manager **")
        print('1) Add a book')
        print('2) Lookup book')
        print('3) Display books')
        print('4) Quit')
        choice=int(input())

        if choice==1:
            print("Adding a book...")
            book_name=input("Enter the name of the Book >>>")
            author=input("Enter the name of the Author >>>")
            pages=int(input("Enter the number of pages >>>"))

            booklist.append([book_name,author,pages])
        elif choice==2:
            print('Looking up for a book...')
            keyword=input('Enter name of the book')

            for book in booklist:
                if keyword in book:
                    print(book)
        elif choice==3:
            print('Display all books...')
            for book in booklist:
                print(book)
        elif choice==4:
            print("Quitting Program")
    print("program Terminated")

    with open("/home/tor/Desktop/CLI Book management app/books.txt",'w') as booksfile:
        for books in booklist:
            booksfile.write(','.join(book)+'\n')



    

if __name__=="__main__":
    main()