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
insert into formats(dBNumber,versionNumber,formatType,ISBN,lang,publisher,length,releaseDate) values (1,1,"Paperback","978-1-942993-36-0","English","Vertical Comics",216,'2019-04-19'),
																									 (2,1,"Paperback","978-1-63236-666-5","English","Kodansha Comics",192,'2018-07-10'),
                                                                                                     (3,1,"Paperback","9-780316-013697","English","Hachette Book Group",229,'2009-04-01'),
                                                                                                     (4,1,"Hardcover","978-0-393-60939-4","English","W.W.Norton & Company",209,'2017-05-02'),
                                                                                                     (5,1,"Paperback","978-0-545-17415-2","English","Scholastic INC",208,'2010-01-01'),
                                                                                                     (6,1,"Paperback","978-1-63236-667-2","English","Kodansha Comics",192,'2018-09-11'),
                                                                                                     (7,1,"Hardcover","978-0-545-06039-4","English","Scholastic Press",220,"2008-09-09"),
                                                                                                     (8,1,"Hardcover","978-0-545-06042-4","English","Scholastic INC",176,"2008-12-02"),
                                                                                                     (9,1,"Hardcover","978-0-545-06043-1","English","Scholastic",160,"2009-03-03"),
                                                                                                     (10,1,"Hardcover","978-0-262-03766-2","English","The MIT Press",254,'2018-03-02');
/*Series Info*/
TRUNCATE TABLE series;
insert into series(dbNumber,seriesName,sequenceNumber) values (2,"Grand Blue Dreaming",1),(6,"Grand Blue Dreaming",2),(7,"The 39 Clues",1),(8,"The 39 Clues",2),(9,"The 39 Clues",3);
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
insert into contributors(dbNumber,versionNumber,personName,roleName) values (1,1,"Kaori Ozaki","Author"),(2,1,"Kenji Inoue","Author"),(2,1,"Kimitake Yoshioka","Author"),
																			(3,1,"Sherman Alexie","Author"),(3,1,"Ellen Forney","Illustrator"),(4,1,"Neil DeGrase Tyson","Author"),
                                                                            (5,1,"AVI","Author"),(6,1,"Kenji Inoue","Author"),(6,1,"Kimitake Yoshioka","Author"),
                                                                            (7,1,"Rick Riordan","Author"),(8,1,"Gordan Korman","Author"),(9,1,"Peter Lerangis","Author"),(10,1,"Wan Fokkink","Author");
/*pricing*/
TRUNCATE TABLE pricing;
insert into pricing (dbNumber,versionNumber,price) values (1,1,12.99),(2,1,9.99),(3,1,14.99),(4,1,16.99),(5,1,9.99),(6,1,9.99),(7,1,7.99),(8,1,7.99),(9,1,7.99),(10,1,79.99);
/*soldHistory and soldTotal*/
TRUNCATE TABLE soldHistory;
insert into soldHistory(dbNumber,versionNumber,dateSold,soldAtPriceOf) values (1,1,'2019-01-04',9.99),
																			  (1,1,'2019-01-04',10.99),
                                                                              (5,1,'2006-02-19',9.99),
                                                                              (5,1,'2008-02-20',8.99),(6,1,'2010-09-02',7.99),(6,1,'2018-07-17',9.99),
                                                                              (1,1,'2020-01-04',11.99),(7,1,'2010-10-10',7.99),(7,1,'2010-10-10',7.95),
                                                                              (1,1,'2019-01-04',8.99),(7,1,'2011-11-15',6.95),(7,1,'2015-12-29',6.99),
                                                                              (1,1,'2019-01-04',5.99),(8,1,'2012-12-01',6.99),(8,1,'2013-02-13',5.99),
                                                                              (1,1,'2019-06-14',11.99),(10,1,'2015-04-10',70.99),(10,1,'2019-09-15',79.99),
																			  (2,1,'2019-11-24',4.99),(10,1,'2018-06-23',75.99),(10,1,'2020-01-06',78.88),
																			  (2,1,'2019-05-25',6.99),(10,1,'2020-01-06',78.88),(10,1,'2020-01-07',72.12),
                                                                              (2,1,'2019-01-24',6.99),
                                                                              (2,1,'2019-01-08',7.99),
                                                                              (2,1,'2019-09-09',5.99),
                                                                              (3,1,'2019-11-24',2.99),
                                                                              (3,1,'2019-11-14',6.54),
                                                                              (4,1,'2019-03-04',11.99),
                                                                              (4,1,'2019-11-04',11.99),
                                                                              (4,1,'2029-02-04',11.99);
TRUNCATE Table soldTotal;
/*ratingsCollection , ratingsTotal*/
TRUNCATE TABLE ratingsCollection;
insert into ratingsCollection(dbNumber,versionNumber,email,rating) values (1,1,NULL,4),(1,1,NULL,3),(1,1,NULL,5),(1,1,NULL,1),(1,1,NULL,2),(1,1,NULL,4),(1,1,NULL,4),(1,1,NULL,3),(1,1,NULL,3),(1,1,NULL,4),(1,1,NULL,4),(1,1,NULL,3),(1,1,NULL,5),(1,1,NULL,5),
																		  (2,1,"jeffrey@yahoo.com",1),(2,1,NULL,4),(2,1,NULL,5),(2,1,"howards9378@gmail.com",4),(2,1,NULL,3),(2,1,NULL,3),(2,1,NULL,3),(2,1,NULL,4),(2,1,NULL,5),(2,1,NULL,4),(2,1,NULL,1),(2,1,NULL,3),
                                                                          (3,1,NULL,3),(3,1,NULL,4),(3,1,"mimi@gmail.com",5),(3,1,NULL,5),(3,1,"giogio@yahoo.com",3),(3,1,NULL,5),(3,1,NULL,5),(3,1,NULL,4),(4,1,NULL,1),(4,1,NULL,1),(4,1,NULL,1),(4,1,NULL,4),(4,1,NULL,5),
                                                                          (4,1,"jonah@reticle.com",1),(4,1,NULL,2),(4,1,NULL,2),(4,1,NULL,4),(4,1,NULL,5),(5,1,NULL,3),(5,1,"a@b.com",5),(5,1,NULL,4),(5,1,NULL,3),(5,1,NULL,3),(5,1,"heyo@gmail.com",1),(5,1,NULL,3),(6,1,NULL,4),
                                                                          (6,1,NULL,1),(6,1,NULL,5),(6,1,NULL,5),(6,1,"hello@jamision.org",5),(6,1,NULL,4),(6,1,NULL,1),(6,1,NULL,5),(7,1,NULL,5),(6,1,NULL,1),(6,1,NULL,2),(6,1,NULL,1),(7,1,NULL,4),(6,1,NULL,4),(7,1,NULL,5),
                                                                          (7,1,NULL,4),(7,1,NULL,3),(8,1,NULL,2),(8,1,"miles@perhour.org",3),(8,1,NULL,4),(8,1,NULL,5),(8,1,"icyhot@eco.com",3),(8,1,NULL,1),(8,1,NULL,5),(8,1,NULL,3),(8,1,NULL,3),(8,1,NULL,5),(9,1,NULL,5),(9,1,NULL,1),(9,1,NULL,1),
                                                                          (9,1,NULL,1),(9,1,NULL,1),(9,1,NULL,1),(9,1,NULL,1),(9,1,NULL,1),(9,1,NULL,2),(9,1,NULL,1),(9,1,NULL,1),(9,1,NULL,1),(10,1,"keebler@cookies.gov",4),(10,1,NULL,5),(10,1,NULL,4),(10,1,NULL,4),(10,1,NULL,3),(10,1,NULL,4)
                                                                          ,(10,1,NULL,5),(10,1,NULL,4),(10,1,NULL,3),(10,1,NULL,2),(10,1,"edgewise@nowords.co",1),(10,1,NULL,1),(10,1,NULL,1),(10,1,NULL,1),(10,1,NULL,1),(10,1,NULL,4),(10,1,NULL,3),(10,1,NULL,2),(10,1,NULL,1);
TRUNCATE TABLE ratingsTotal;