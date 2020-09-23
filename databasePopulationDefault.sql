use bookHandler;
/*General Info*/
TRUNCATE TABLE generalInfo;
insert into generalInfo(title) values ("the gods lie.");
insert into generalInfo(title) values ("Grand Blue Dreaming Volume 1");
insert into generalInfo(title) values ("The Absolutely True Diary of a Part-Time Indian");
insert into generalInfo(title) values ("Astrophysics for People in a Hurry");
insert into generalInfo(title) values ("Nothing But The Truth");
insert into generalInfo(title) values ("Grand Blue Dreaming Volume 2");
insert into generalInfo(title) values ("The 39 Clues: The Maze of Bones");
insert into generalInfo(title) values ("The 39 Clues: One False Note");
insert into generalInfo(title) values ("The 39 Clues: The Sword Thief");
insert into generalInfo(title) values ("Distributed Algorithms: An Intuitive Approach, 2nd Edition");
/*Version Info*/
TRUNCATE TABLE formats;
insert into formats(dBNumber,versionNumber,formatType,ISBN,lang,publisher,length,releaseDate) values (1,1,"Paperback",9781942993360,"English","Vertical Comics",216,2016-04-19);
/*Series Info*/
TRUNCATE TABLE series;
/*genres*/
TRUNCATE TABLE genres;
insert into genres(dbNumber,genre) values (1,"Romance"),(1,"Manga"),(1,"Slice of Life"),(1,"Fiction"),
											(2,"Slice of Life"),(2,"Comedy"),(2,"Manga"),(2,"Fiction"),
                                            (3,"Fiction"),(3,"Comedy"),(3,"Graphic Novel"),
                                            (4,"Scientific"),(5,"Fiction"),(5,"Historical"),(6,"Comedy"),(6,"Manga"),(6,"Fiction"),
                                            (7,"Action"),(7,"Adventure"),(7,"Mystery"),(7,"Fiction"),
                                            (8,"Action"),(8,"Adventure"),(8,"Mystery"),(8,"Fiction"),
                                            (9,"Action"),(9,"Adventure"),(9,"Mystery"),(9,"Fiction"),
                                            (10,"Textbook"),(10,"Programming");
/*contributors*/
TRUNCATE TABLE contributors;
/*pricing*/
TRUNCATE TABLE pricing;
insert into pricing (dbNumber,versionNumber,price) values (1,1,12.99),(2,1,9.99),(3,1,14.99),(4,16.99),(5,1,9.99),(6,1,9.99),(7,1,7.99),(8,1,7.99),(9,1,7.99),(10,1,79.99);
/*soldHistory and soldTotal*/
TRUNCATE TABLE soldHistory;
TRUNCATE Table soldTotal;
/*ratingsCollection , ratingsTotal*/
TRUNCATE TABLE ratingsCollection;
TRUNCATE TABLE ratingsTotal;