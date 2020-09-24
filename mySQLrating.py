import mysql.connector

def addRating(conn,db,vnum,rating):
    query = "";
    iTuple = None;
    #update both ratings tables
    query = """INSERT INTO ratingsCollection (dbNumber,versionNumber,rating)
            VALUES (%s,%s,%s)""";
    iTuple = (db,vnum,rating);
    cursor = conn.cursor(prepared=True);
    cursor.execute(query,iTuple);
    conn.commit();

    #pull the ratingsTotal so we can get some info
    query2 = """ SELECT raterCount,avgRating FROM ratingsTotal
                 WHERE dbNumber = %s AND versionNumber = %s
             """
    cursor.execute(query2,(db,vnum));
    res = cursor.fetchall();

    for x in res:
        totalRaters = int(x[0]);
        avgRating = float(x[1]);
        avgRating = ((avgRating * totalRaters)+ rating)/(totalRaters + 1);
        totalRaters += 1;
        query3 = "UPDATE ratingsTotal SET raterCount = %s, avgRating = %s WHERE dbNumber = %s AND versionNumber = %s";
        cursor.execute(query3,(totalRaters,avgRating,db,vnum))
        conn.commit()
        return;


