import mySQLScripts as connector
import mySQLSearchMechanics as searching





def main():
    print("Welcome to the simple version of Book Handler.")
    conn = connector.produceConnection("config.txt");
    while True:
        print("""Please enter the number corresponding to the action you want to perform.
[1]: Search for a book by title
[2]: Search for a book by contributor (author/illustrator/etc...)
[3]: Search for a book by publisher
[4]: Search for a book by series
[5]: Search for a book by rating
                """)
        action = input();
        if (action == "1"):
            print("What is the title of the book you're looking for? (Press Enter without typing anything to cancel)");
            search = input();
            if search:
                results = searching.findBookByTitle(conn,search);
                for x in results:
                    print(x);
        elif (action == "2"):
            print("What is the name of the person you are looking for? (Press Enter without typing anything to cancel)");
            search = input();
            if search:
                results = searching.findBookByContributor(conn,search);
                for x in results:
                    print(x);           
        elif (action == "3"):
            print("What's the name of the publisher you're looking for? (Press Enter without typing anything to cancel)");
            search = input();
            if search:
                results = searching.findBookByPublisher(conn,search);
                for x in results:
                    print(x);            
        elif (action == "4"):
            print("What's the name of the series you're looking for? (Press Enter without typing anything to cancel)");
            search = input();
            if search:
                results = searching.findBookBySeries(conn,search);
                for x in results:
                    print(x);                  
        elif(action == "5"):
            print("What is the lowest star rating you'll acccept? (1-5) (Press Enter without typing anything to cancel)")
if __name__ == '__main__':
    main()
