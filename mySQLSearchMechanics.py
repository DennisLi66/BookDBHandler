import mysql.connector

#search by database
def findBookByDatabaseNumber(conn,num):
    query = """select generalInfo.title,generalInfo.dBNumber,formats.formatType,formats.ISBN,formats.lang,formats.publisher,formats.length,ratingsTotal.avgRating,ratingsTotal.raterCount,price
from generalInfo left join formats on generalInfo.dbNumber = formats.dbNumber 
left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber 
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
from contributors left join generalInfo on generalInfo.dbNumber = contributors.dbNumber 
left join formats ON formats.dbNumber = contributors.dbNumber AND formats.versionNumber = contributors.versionNumber 
left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber and ratingsTotal.dbNumber = formats.dbNumber
left join pricing on formats.versionNumber = pricing.versionNumber AND pricing.dbNumber = formats.dbNumber
WHERE personName LIKE %s
    """
    cursor = conn.cursor(prepared = True);
    cursor.execute(query,("%" + cont + "%"));
    res = cursor.fetchall();
    return res;

#search by rating
#search by title
#search by publisher
def findBookBy
