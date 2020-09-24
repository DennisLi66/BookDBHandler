import mysql.connector



def addPurchase(conn,db,vnum,dateSold,soldAt):
    query = """INSERT INTO 
            """;
    return;

def searchPurchases(conn,db):
    return;

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
    cursor.execute(query,(string(db)))
    return cursor.fetchall();
