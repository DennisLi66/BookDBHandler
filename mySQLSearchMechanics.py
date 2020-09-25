import mysql.connector
import mySQLScripts as connector

#search by database
def findBookByDatabaseNumber(conn,num):
    query = """select generalInfo.title,generalInfo.dBNumber,formats.formatType,formats.ISBN,formats.lang,formats.publisher,formats.length,ratingsTotal.avgRating,ratingsTotal.raterCount,price
from generalInfo left join formats on generalInfo.dbNumber = formats.dbNumber 
right join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber 
and ratingsTotal.dbNumber = formats.dbNumber
left join pricing on formats.versionNumber = pricing.versionNumber AND pricing.dbNumber = formats.dbNumber
WHERE generalInfo.dbNumber = %s;"""
    cursor = conn.cursor(prepared=True);
    cursor.execute(query,(str(num)));
    res = cursor.fetchall();
    # for x in res:
    #     print(x);
    return res;


#search by title
def findBookByTitle(conn,title):
    query = """select generalInfo.title,generalInfo.dBNumber,formats.formatType,formats.ISBN,formats.lang,formats.publisher,formats.length,ratingsTotal.avgRating,ratingsTotal.raterCount,price
        from generalInfo 
        right join formats ON formats.dbNumber = generalInfo.dbNumber 
        left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber and ratingsTotal.dbNumber = formats.dbNumber
        left join pricing on formats.versionNumber = pricing.versionNumber AND pricing.dbNumber = formats.dbNumber
        WHERE title LIKE %s;"""
    cursor = conn.cursor(prepared = True);
    cursor.execute(query,tuple(['%' + title + '%' ]));
    res = cursor.fetchall();
    return res; 
#genres has search by genres

#search by author
def findBookByContributor(conn,cont):
    query = """
select generalInfo.dbNumber,title,lang,publisher,length,releaseDate,avgRating,price
from contributors right join generalInfo on generalInfo.dbNumber = contributors.dbNumber 
left join formats ON formats.dbNumber = contributors.dbNumber AND formats.versionNumber = contributors.versionNumber 
left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber and ratingsTotal.dbNumber = formats.dbNumber
left join pricing on formats.versionNumber = pricing.versionNumber AND pricing.dbNumber = formats.dbNumber
WHERE personName LIKE %s
    """
    cursor = conn.cursor(prepared = True);
    cursor.execute(query,tuple(["%" + cont + "%"]));
    res = cursor.fetchall();
    return res;

#search by publisher
def findBookByPublisher(conn,publisher):
    query = """
        select generalInfo.dbNumber,title,lang,publisher,length,releaseDate,avgRating,price
        from  generalInfo 
        right join formats ON formats.dbNumber = generalInfo.dbNumber 
        left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber and ratingsTotal.dbNumber = formats.dbNumber
        left join pricing on formats.versionNumber = pricing.versionNumber AND pricing.dbNumber = formats.dbNumber
        WHERE publisher LIKE %s
    """
    cursor = conn.cursor(prepared = True);
    cursor.execute(query,tuple(["%" + publisher + "%"]));
    res = cursor.fetchall();
    return res; 


#search by rating
def findBookByRating(conn,low = 0,high = 5):
    query = """
    select generalInfo.dbNumber,title,lang,publisher,length,releaseDate,avgRating,price
    from  generalInfo 
    right join formats ON formats.dbNumber = generalInfo.dbNumber 
    left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber and ratingsTotal.dbNumber = formats.dbNumber
    left join pricing on formats.versionNumber = pricing.versionNumber AND pricing.dbNumber = formats.dbNumber WHERE avgRating >= %s
    AND avgRating <= %s ORDER BY avgRating DESC
    """;
    if (low > 5):
        raise KeyError("Low cannot be that high");
    elif (high < 1):
        raise KeyError("High cannot be that low");
    cursor = conn.cursor(prepared = True);
    cursor.execute(query,(str(low),str(high)))
    res = cursor.fetchall();
    return res;

def findBookBySeries(conn,series):
    query = """
    select generalInfo.dbNumber,title,lang,publisher,length,releaseDate,avgRating,price
    from  generalInfo 
    right join formats ON formats.dbNumber = generalInfo.dbNumber 
    left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber and ratingsTotal.dbNumber = formats.dbNumber
    left join pricing on formats.versionNumber = pricing.versionNumber AND pricing.dbNumber = formats.dbNumber
    right join series on series.dbNumber = formats.dbNumber
    WHERE seriesName LIKE %s;
    """
    cursor = conn.cursor(prepared = True);
    cursor.execute(query,tuple(["%" + series + "%"]));
    res = cursor.fetchall();
    return res; 

def advSearch(conn,title= "",genre = "", series = "", cont = "", pub = "", low = None, high = None):
    listOfString = [];
    listOfComps = [];
    listOfFactors = [];
    # exec code
    if (title):
        listOfComps.append("title LIKE %s");
        listOfFactors.append('%' + title + '%');
    if (genre):
        listOfString.append("right join genres ON genres.dbNumber = genres.dbNumber")
        listOfComps.append("genre = %s");
        listOfFactors.append('%' + genre + '%');
    if (series):
        listOfString.append("right join series ON series.dbNumber = formats.dbNumber")
        listOfComps.append("seriesName = %s");
        listOfFactors.append('%' + series + '%');
    if (cont):
        listOfString.append("right join contributors ON contributors.dbNumber = formats.dbNumber AND contributors.versionNumber = formats.versionNumber")
        listOfComps.append("contributors.personName LIKE %s");
        listOfFactors.append('%' + cont + '%');
    if (pub):
        listOfComps.append("publisher LIKE &s");
        listOfFactors.append('%' + pub + '%');
    if (low):
        listOfComps.append("avgRating >= %s");
        listOfFactors.append(str(low));
    if (high):
        listOfComps.append("avgRating <= %s");
        listOfFactors.append(str(high));
    query = """
        select * from generalInfo 
        right join formats on formats.dbNumber = generalInfo.dbNumber 
        left join ratingsTotal on ratingsTotal.dbNumber = formats.dbNumber AND formats.versionNumber = ratingsTotal.versionNumber
        left join pricing on formats.dbNumber = pricing.dbNumber AND formats.versionNumber = pricing.versionNumber
    """
    query += " ".join(listOfString);
    if (len(listOfComps) > 0):
        query += " WHERE ";
        query += " AND ".join(listOfComps);
    cursor = conn.cursor(prepared = True);
    # print(query)
    # print(listOfFactors)
    cursor.execute(query,tuple(listOfFactors));
    res = cursor.fetchall();
    return res;
        
if __name__ == '__main__':
    conn = connector.produceConnection("config.txt");
    results = findBookByDatabaseNumber(conn,1)
    print("TEST 1:\n")
    for x in results:
        print(x)
    print("TEST 2:\n")
    results = findBookByTitle(conn,"Astrophysics")
    for x in results:
        print(x)
    print("TEST 3:\n")
    results = findBookByContributor(conn,"Sherman")
    for x in results:
        print(x)   
    print("TEST 4:\n")
    results = findBookByPublisher(conn,"Kodansha")
    for x in results:
        print(x)
    print("TEST 5:\n")
    results = findBookBySeries(conn,"The 39 Clues")
    for x in results:
        print(x)
    print("TEST 6:\n")
    results = advSearch(conn,title = "Nothing",cont="Avi")
    for x in results:
        print(x)
