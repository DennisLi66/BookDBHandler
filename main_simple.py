import mySQLScripts as connector
import mySQLSearchMechanics as searching





def main():
    print("Welcome to the simple version of Book Handler.")
    conn = connector.produceConnection("config.txt");
    while True:
        print("""Please enter the number corresponding to the action you want to perform.
[1]: Search for a book by title
                """)
        action = input();
        if (action == "1"):
            print("What is the title of the book you're looking for? (Press Enter without typing anything to cancel)");
            search = input();
            if search:
                results = searching.findBookByTitle(conn,search);
                for x in results:
                    print(x);
                
        
if __name__ == '__main__':
    main()
