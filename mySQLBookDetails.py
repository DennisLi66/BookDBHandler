import mysql.connector

def addContributor(conn,db,vn,name,role):
    #Check if db and vn combo exists
    # cQuery = """SELECT * FROM contributors WHERE dbNumber = %s AND
    #          versionNumber = %s
    #          """;
    # cursor = conn.cursor(preprared = True);
    # cursor.execute(cQuery,(db,vn));
    # conn.commit();
    # if not cursor.rowcount:
    #     
    # else:
    #Make it so it would be impossible not to use correct values
    query = """INSERT INTO contributors (dbNumber,versionNumber,personName,roleName)
    VALUES (%s,%s,%s,%s)""";
    cursor = conn.cursor(prepared = True);
    cursor = execute(query,(db,vn,name,role));
    conn.commit();

def addToSeries(conn,db,series,order):
    cQuery = "SELECT * FROM series WHERE dbNumber = %s AND seriesName = %s AND sequenceNumber = %s";
    cursor = conn.cursor(prepared = True);
    cursor = execute(query,(db,series,order));
    if not cursor.rowcount:
        query = "INSERT INTO series (dbNumber,seriesName,sequenceNumber) VALUES (%s,%s,%s)"
        cursor.execute(query,(db,series,order));
        conn.commit();
        return True;
    else:
        return False;
        #Something of that sequence was already there

def addFormat(conn,db,vn,formatType,publisher,length,releaseDate,ISBN = "NULL",lang="English")
    iQuery = """INSERT INTO formats (databaseNumber,versionNumber,formatType,publisher,length,releaseDate,ISBN,lang)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
             """;
    cursor = conn.cursor(prepared = True);
    cursor = execute(iQuery,(db,vn,formatType,publisher,length,releaseDate,ISBN,lang))
    conn.commit();
    return;