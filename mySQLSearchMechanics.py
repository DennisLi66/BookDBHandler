import mysql.connector

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
    cursor.execute(query,("%" + cont + "%"));
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
    cursor.execute(query,("%" + publisher + "%"));
    res = cursor.fetchall();
    return res; 

#search by title
def findBookByTitle(conn,title):
    query = """
        select generalInfo.dbNumber,title,lang,publisher,length,releaseDate,avgRating,price
        from  generalInfo 
        right join formats ON formats.dbNumber = generalInfo.dbNumber 
        left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber and ratingsTotal.dbNumber = formats.dbNumber
        left join pricing on formats.versionNumber = pricing.versionNumber AND pricing.dbNumber = formats.dbNumber
        WHERE title LIKE %s
    """
    cursor = conn.cursor(prepared = True);
    cursor.execute(query,("%" + title + "%"));
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
    right join series on formats.versionNumber = series.versionNumber AND series.dbNumber = formats.dbNumber
    WHERE series LIKE &s;
    """
    cursor = conn.cursor(prepared = True);
    cursor.execute(query,("%" + series + "%"));
    res = cursor.fetchall();
    return res; 

def advSearch(conn,title= "",genre = "", series = "", cont = "", pub = "", low = None, high = None):
    listOfString = [];
    listOfComps = [];
    listOfFactors = [];
    # exec code
    if (title):
        listOfComps.append("title LIKE %s");
        listOfFactors.append(title);
    if (genre):
        listOfString.append("right join contributors ON contributors.dbNumber = formats.dbNumber AND contributors.versionNumber = formats.versionNumber")
        listOfComps.append("genre = %s");
        listOfFactors.append(genre);
    if (series):
        listOfString.append("right join series ON series.dbNumber = formats.dbNumber AND series.versionNumber = formats.versionNumber")
        listOfComps.append("series = %s");
        listOfFactors.append(series);
    if (cont):
        listOfString.append("right join contributors ON contributors.dbNumber = formats.dbNumber AND contributors.versionNumber = formats.versionNumber")
        listOfComps.append("contributors LIKE %s");
        listOfFactors.append(cont);
    if (pub):
        listOfComps.append("publisher LIKE &s");
        listOfFactors.append(pub);
    if (low):
        listOfComps.append("avgRating >= %s");
        listOfFactors.append(low);
    if (high):
        listOfComps.append("avgRating <= %s");
        listOfFactors.append(high);
    query = """
        select * from generalInfo 
        right join formats on formats.dbNumber = generalInfo.dbNumber 
        left join ratingsTotal on ratingsTotal.dbNumber = formats.dbNumber AND formats.versionNumber = ratingsTotal.versionNumber
        left join pricing on formats.dbNumber = pricing.dbNumber AND formats.versionNumber = pricing.versionNumber
    """
    query += string.join(listOfString);
    if (len(listOfComps) > 1):
        query += " WHERE ";
        query += " AND ".join(listOfComps);
    cursor = conn.cursor(prepared = True);
    cursor.execute(query,tuple(listOfFactors));
    res = cursor.fetchall();
    return res;
        

    

