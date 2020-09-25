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
    cursor = execute(query,(str(db),str(vn),name,role));
    conn.commit();

def addToSeries(conn,db,series,order):
    cQuery = "SELECT * FROM series WHERE dbNumber = %s AND seriesName = %s AND sequenceNumber = %s";
    cursor = conn.cursor(prepared = True);
    cursor = execute(query,(str(db),series,str(order)));
    if not cursor.rowcount:
        query = "INSERT INTO series (dbNumber,seriesName,sequenceNumber) VALUES (%s,%s,%s)"
        cursor.execute(query,(str(db),series,str(order)));
        conn.commit();
        return True;
    else:
        return False;
        #Something of that sequence was already there

def addFormat(conn,db,vn,formatType,publisher,length,releaseDate,ISBN = "NULL",lang="English"):
    iQuery = """INSERT INTO formats (databaseNumber,versionNumber,formatType,publisher,length,releaseDate,ISBN,lang)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
             """;
    cursor = conn.cursor(prepared = True);
    cursor = execute(iQuery,(str(db),str(vn),formatType,publisher,str(length),releaseDate,ISBN,lang))
    conn.commit();
    return;

def addBook(conn,title,formatType,publisher,length,releaseDate,ISBN = "NULL",lang = "English"):
    iQuery = """INSERT INTO generalInfo(title) VALUES (&s) """;
    sQuery = """SELECT dbNumber FROM generalInfo ORDER BY dbNumber DESC """;
    cursor = conn.cursor(prepared = True);
    cursor = execute(iQuery,(title))
    cursor.commit();
    cursor.execute(sQuery);
    llist = cursor.fetchall();
    for x in llist:
        db = x[0];
        addFormat(conn,str(db),str(1),formatType,publisher,str(length),releaseDate,ISBN,lang);
        return;

def getContributor(conn,db,vn):
    sQuery = """SELECT * from contributors WHERE dbNumber = %s AND versionNumber = %s"""
    cursor = conn.cursor(prepared = True);
    cursor = execute(sQuery,(str(db),str(vn)));
    if not cursor.rowcount:
        return False;
    return cursor.fetchall()




        
