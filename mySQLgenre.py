import mysql.connector


def searchByGenre(conn,genre):
    query = """ select distinct generalInfo.title,generalInfo.dBNumber,formats.formatType,formats.ISBN,formats.lang,formats.publisher,formats.length,ratingsTotal.avgRating,ratingsTotal.raterCount
  from genres right join generalInfo on generalInfo.dbNumber = genres.dbNumber left join formats on generalInfo.dbNumber = formats.dbNumber 
  left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber and ratingsTotal.dbNumber = formats.dbNumber
  where genres.dbNumber in (select dbNumber from genres where genre = '""" + genre + """');"""
    cursor = conn.cursor();
    cursor.execute(query);
    res = cursor.fetchall();
    # for x in res:
    #     print(x);
    return res;

def getGenres(conn):
    query = "select distinct genre from genres order by genre asc;";
    cursor = conn.cursor();
    cursor.execute(query)
    return cursor.fetchall();

def addGenre(conn,genre,dbNumber):
    query = "INSERT INTO genres (dbNumber,genre) values (%s,%s)";
    cursor = conn.cursor(prepared = True);
    cursor.execute(query,(dbNumber,genre));
    conn.commit();

    
