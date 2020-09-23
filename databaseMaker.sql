drop database if exists bookhandler;
create database bookhandler;

use bookhandler;
create table generalInfo(
dBNumber int NOT NULL AUTO_INCREMENT , /* Database Number */
title varchar(255) /*Title of Book*/
);
create table formats(
dBNumber int, /* Database Number */
versionNumber int /*Used with above to denote version*/,
formatType varchar(255) /*Hardcover, Paperback, etc...*/,
ISBN int NULL UNIQUE, /* ISBN */
lang varchar(255) NULL,
publisher varchar(255) /* I assume different versions can have different publishers */,
length int NULL /*Page Count*/,
releaseDate date,
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
    email varchar(255) unique, /* User Email, tied to rating, can be null */
    rating int /* 1 to 5*/
);
create table ratingsTotal (
	dbNumber int, /* Database Number */
    versionNumber int, /* Version Number */
    raterCount int, /* Amount of People Who Rated */
    avgRating float /* Average Rating, May want to limit to X.X decimals, round up*/
)