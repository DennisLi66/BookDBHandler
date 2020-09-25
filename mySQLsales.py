import mysql.connector



def addPurchase(conn,db,vnum,dateSold,soldAt):
    query = """INSERT INTO soldHistory (dbNumber,versionNumber,dateSold,soldAtPriceOf)
            VALUES (%s,%s,%s,%s) 
            """;
    cursor = conn.cursor(prepared=True);
    cursor.execute(query,(str(db),str(vnum),str(dateSold),str(soldAt)));
    conn.commit();

    query2 = """
            SELECT totalSold, totalPrice * from soldTotal WHERE
            dbNumber = %s AND versionNumber = %s;
             """
    cursor.execute(query2,(str(db),str(vnum)));
    if not cursor.rowcount:
        query4 = """INSERT INTO soldTotal (dbNumber,versionNumber,totalSold,totalPrice)
                VALUES (%s,%s,1,%s)
        """
        cursor.execute(query4,(str(db),str(vnum),str(soldAt)));
        conn.commit();
        return;
    res = cursor.fetchall();
    for x in res:
        sold = int(x[0]) + 1;
        price = float(x[1]) + float(soldAt);
        query3 = "UPDATE soldTotal (dbNumber,versionNumber,totalSold,totalPrice) VALUES (%s,%s,%s,%s)"
        cursor.execute(query3,(str(db),str(vnum),str(sold),str(price)));
        conn.commit();
        return;


def changePrice(conn,db,vnum,price):
    #look at pricing and change it if it exists
    query = "SELECT * FROM pricing WHERE dbNumber = %s AND versionNumber = %s";
    cursor = conn.cursor(prepared = True);
    cursor.execute(query,(str(db),str(vnum)));
    if not cursor.rowcount:
        #insert
        query2 = "INSERT INTO pricing (dbNumber,versionNumber,price) VALUES (%s,%s,%s)";
        cursor.execute(query2,(str(db),str(vnum),str(price)))
        cursor.commit();
        return;
    else:
        #Update
        query3 = "UPDATE pricing SET price = %s WHERE dbNumber = %s AND versionNumber = %s"
        cursor.execute(query3,(str(price),str(db),str(vnum)));
        conn.commit()
        return;
        
    
def searchPurchases(conn,db):
    query = """
select generalInfo.dbNumber,title,formatType,ISBN,lang,publisher,length,releaseDate,dateSold,soldAtPriceOf from generalInfo left join formats on formats.dBNumber = generalInfo.dBNumber 
right join soldHistory on soldHistory.versionNumber = formats.versionNumber and soldHistory.dbNumber = formats.dbNumber WHERE generalInfo.dbNumber = %s order by dateSold desc;
            """;
    cursor = conn.cursor(prepared = True);
    cursor.execute(query,str(db))
    return cursor.fetchall();

def viewTotalSales(conn):
    query = """select generalInfo.dbNumber,generalInfo.title,formatType,ISBN,lang,publisher,length,releaseDate,totalSold,totalPrice
 from generalInfo left join formats on formats.dbNumber = generalInfo.dbNumber 
left join soldTotal on generalInfo.dbNumber = soldTotal.dbNumber and formats.versionNumber = soldTotal.versionNumber
            """
    cursor = conn.cursor();
    cursor.execute(query);
    return cursor.fetchall();

def getPriceInfo(conn,db):
    query = """select generalInfo.dbNumber,title,formats.versionNumber,formatType,ISBN,lang,publisher,length,releaseDate,price
            from generalInfo left join formats on generalInfo.dbNumber = formats.dbNumber
            left join pricing on pricing.versionNumber = formats.versionNumber and pricing.dbNumber = formats.dbNumber
            WHERE generalInfo.dbNumber = %s
            """
    cursor = conn.cursor(prepared = True);
    cursor.execute(query,(str(db)))
    return cursor.fetchall();
