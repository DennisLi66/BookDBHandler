#pip install mysql-connector-python

import mysql.connector
import mySQLgenre as genre
import mySQLsales as sales
import mySQLrating as rate

def produceConnection(fileName):
    """ Take a file name and extract the information required to return a mysql
    connection. """
    file = open(fileName);
    host = "";
    user = "";
    pwd = "";
    try:
        for line in file.readlines():
            x = line.strip();
            if (x[0:5] == "host=" and host == ""):
                host = x[5:];
            elif (x[0:5] == "user=" and user == ""):
                user = x[5:];
            elif (x[0:9] == "password=" and pwd==""):

                pwd = x[9:]
        #print(host + user+pwd);
    except:
        file.close();
        raise ValueError("Not all of the values were properly registered.");  
    file.close();
    if (host == "" or pwd == "" or user == ""):
        raise ValueError("Not all of the values were properly registered.");
    conn = mysql.connector.connect(
      host=host,
      user=user,
      password=pwd,
      database = "bookhandler"
        )
    return conn;

def findBookByDatabaseNumber(conn,num):
    query = """select generalInfo.title,generalInfo.dBNumber,formats.formatType,formats.ISBN,formats.lang,formats.publisher,formats.length,ratingsTotal.avgRating,ratingsTotal.raterCount
from generalInfo left join formats on generalInfo.dbNumber = formats.dbNumber 
left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber 
and ratingsTotal.dbNumber = formats.dbNumber WHERE generalInfo.dbNumber = %s;"""
    cursor = conn.cursor(prepared=True);
    cursor.execute(query,(str(num)));
    res = cursor.fetchall();
    # for x in res:
    #     print(x);
    return res;

if __name__ == '__main__':
    print("Connecting...");
    conn = produceConnection("config.txt");
    findBookByDatabaseNumber(conn,1);
    genre.searchByGenre(conn,"Textbook");
    # genre.addGenre(conn,"Bestseller",4)# works
    rate.addRating(conn,1,1,5)
    print("Finished");
