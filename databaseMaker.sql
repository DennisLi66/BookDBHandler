drop database if exists bookhandler;
create database bookhandler;

use bookhandler;
create table generalInfo(
dbNumber int NOT NULL AUTO_INCREMENT PRIMARY KEY, /* Database Number */
title varchar(255) /*Title of Book*/
);
create table formats(
dbNumber int, /* Database Number */
versionNumber int /*Used with above to denote version*/,
formatType varchar(255) /*Hardcover, Paperback, etc...*/,
ISBN varchar(255) NULL UNIQUE, /* ISBN */
lang varchar(255) NULL,
publisher varchar(255) /* I assume different versions can have different publishers */,
length int NULL /*Page Count*/,
releaseDate date
);
create table series(
	dbNumber int, /* database number */
	seriesName varchar(255),
    sequenceNumber int /* i.e. Volume 1, Volume 2, etc...*/
);
create table soldTotal(
dbNumber int, /* Database Number */
versionNumber int, /* Version sold */
totalSold int, /* count(*) soldHistory total amount of copies sold*/
totalPrice float /*sum() soldHistory */
);
create table soldHistory(
dbNumber int, /* Database Number */
versionNumber int, /* Version sold */
dateSold date /* For Logging Purposes, I suppose */,
soldAtPriceOf float /*Books may be sold at different prices based on coupons or discounts, so here's this*/
);
create table pricing(
dbNumber int, /* Database Number */
versionNumber int, /* Versions can be priced differently */
price float /* For the sake of my sanity I'm keeping this in USD */
);
create table contributors (
/*Roles that encompass contributors are authors and illustrators, maybe more*/
dbNumber int, /* Database Number */
versionNumber int, /* Different Versions may have different artists? */
personName varchar(255) /*Person Name */,
roleName varchar(255) /* Role Name, See Above */
);
create table genres (
dbNumber int, /* Database Number */
genre varchar(255) /* Genre Name */
);
create table ratingsCollection (
	dbNumber int, /* Database Number */
    versionNumber int, /* Maybe different versions have different ratings, hard to say */
    rating int /* 1 to 5*/
);
create table ratingsTotal (
	dbNumber int, /* Database Number */
    versionNumber int, /* Version Number */
    raterCount int, /* Amount of People Who Rated */
    avgRating float /* Average Rating, May want to limit to X.X decimals, round up*/
);

-- select generalInfo.dbNumber,title,lang,publisher,length,releaseDate,avgRating,price
-- from  generalInfo 
-- left join formats ON formats.dbNumber = generalInfo.dbNumber 
-- left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber and ratingsTotal.dbNumber = formats.dbNumber
-- left join pricing on formats.versionNumber = pricing.versionNumber AND pricing.dbNumber = formats.dbNumber
-- WHERE avgRating >= "4"




-- select generalInfo.dbNumber,title,lang,publisher,length,releaseDate,avgRating,price
-- from contributors left join generalInfo on generalInfo.dbNumber = contributors.dbNumber 
-- left join formats ON formats.dbNumber = contributors.dbNumber AND formats.versionNumber = contributors.versionNumber 
-- left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber and ratingsTotal.dbNumber = formats.dbNumber
-- left join pricing on formats.versionNumber = pricing.versionNumber AND pricing.dbNumber = formats.dbNumber
-- WHERE personName LIKE "%Kenji%"


-- select generalInfo.dbNumber,title,formatType,ISBN,lang,publisher,length,releaseDate,dateSold,soldAtPriceOf from generalInfo left join formats on formats.dBNumber = generalInfo.dBNumber 
-- right join soldHistory on soldHistory.versionNumber = formats.versionNumber and soldHistory.dbNumber = formats.dbNumber WHERE generalInfo.dbNumber = "4" order by dateSold desc;

-- select generalInfo.dbNumber,title,formats.versionNumber,formatType,ISBN,lang,publisher,length,releaseDate,price from generalInfo left join formats on generalInfo.dbNumber = formats.dbNumber left join pricing on pricing.versionNumber = formats.versionNumber and pricing.dbNumber = formats.dbNumber
-- select generalInfo.dbNumber,generalInfo.title,formatType,ISBN,lang,publisher,length,releaseDate,totalSold,totalPrice
--  from generalInfo left join formats on formats.dbNumber = generalInfo.dbNumber 
-- left join soldTotal on generalInfo.dbNumber = soldTotal.dbNumber and formats.versionNumber = soldTotal.versionNumber

-- Find Book By Database Number 
-- select generalInfo.title,generalInfo.dBNumber,formats.formatType,formats.ISBN,formats.lang,formats.publisher,formats.length,ratingsTotal.avgRating,ratingsTotal.raterCount
-- from generalInfo left join formats on generalInfo.dbNumber = formats.dbNumber 
-- left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber 
-- and ratingsTotal.dbNumber = formats.dbNumber
-- WHERE generalInfo.dBNumber = 1;

-- Find Genres
-- select distinct genre from genres order by genre asc;

-- Find all books of a certain genre
--  select distinct generalInfo.title,generalInfo.dBNumber,formats.formatType,formats.ISBN,formats.lang,formats.publisher,formats.length,ratingsTotal.avgRating,ratingsTotal.raterCount
--   from genres right join generalInfo on generalInfo.dbNumber = genres.dbNumber left join formats on generalInfo.dbNumber = formats.dbNumber 
--   left join ratingsTotal on formats.versionNumber = ratingsTotal.versionNumber and ratingsTotal.dbNumber = formats.dbNumber
--   where genres.dbNumber in (select dbNumber from genres where genre = "Action")

-- Insert genre --
-- Insert into genres (dbNumber,genre) values (4,"Nonfiction")
-- select * from genres;
