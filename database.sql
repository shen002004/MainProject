BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Admin_tbl_admin" (
	"id"	integer NOT NULL,
	"admin_name"	varchar(30) NOT NULL,
	"admin_email"	varchar(30) NOT NULL,
	"admin_contact"	varchar(30) NOT NULL,
	"admin_password"	varchar(30) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Admin_tbl_bhk" (
	"id"	integer NOT NULL,
	"bhk_name"	varchar(30) NOT NULL,
	"propertytype_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("propertytype_id") REFERENCES "Admin_tbl_propertytype"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "Admin_tbl_category" (
	"id"	integer NOT NULL,
	"category_name"	varchar(30) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Admin_tbl_district" (
	"id"	integer NOT NULL,
	"district_name"	varchar(30) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Admin_tbl_furnish" (
	"id"	integer NOT NULL,
	"furnish_name"	varchar(30) NOT NULL,
	"propertytype_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("propertytype_id") REFERENCES "Admin_tbl_propertytype"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "Admin_tbl_place" (
	"id"	integer NOT NULL,
	"place_name"	varchar(50) NOT NULL,
	"district_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("district_id") REFERENCES "Admin_tbl_district"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "Admin_tbl_propertytype" (
	"id"	integer NOT NULL,
	"propertytype_name"	varchar(30) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Admin_tbl_subcategory" (
	"id"	integer NOT NULL,
	"subcategory_name"	varchar(30) NOT NULL,
	"category_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("category_id") REFERENCES "Admin_tbl_category"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "Guest_tbl_renter" (
	"id"	integer NOT NULL,
	"renter_name"	varchar(30) NOT NULL,
	"renter_email"	varchar(30) NOT NULL,
	"renter_contact"	varchar(30) NOT NULL,
	"renter_address"	varchar(100) NOT NULL,
	"renter_photo"	varchar(100) NOT NULL,
	"renter_proof"	varchar(100) NOT NULL,
	"renter_password"	varchar(30) NOT NULL,
	"place_id"	bigint NOT NULL,
	"renter_status"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("place_id") REFERENCES "Admin_tbl_place"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "Guest_tbl_seller" (
	"id"	integer NOT NULL,
	"seller_name"	varchar(30) NOT NULL,
	"seller_email"	varchar(30) NOT NULL,
	"seller_contact"	varchar(30) NOT NULL,
	"seller_address"	varchar(100) NOT NULL,
	"seller_photo"	varchar(100) NOT NULL,
	"seller_proof"	varchar(100) NOT NULL,
	"seller_password"	varchar(30) NOT NULL,
	"place_id"	bigint NOT NULL,
	"seller_status"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("place_id") REFERENCES "Admin_tbl_place"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "Guest_tbl_user" (
	"id"	integer NOT NULL,
	"user_name"	varchar(30) NOT NULL,
	"user_email"	varchar(30) NOT NULL,
	"user_contact"	varchar(30) NOT NULL,
	"user_address"	varchar(100) NOT NULL,
	"user_photo"	varchar(100) NOT NULL,
	"user_password"	varchar(30) NOT NULL,
	"place_id"	bigint NOT NULL,
	"user_status"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("place_id") REFERENCES "Admin_tbl_place"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "Seller_tbl_gallery" (
	"id"	integer NOT NULL,
	"gallery_photo"	varchar(100) NOT NULL,
	"property_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("property_id") REFERENCES "Seller_tbl_property"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "Seller_tbl_property" (
	"id"	integer NOT NULL,
	"property_name"	varchar(30) NOT NULL,
	"property_description"	varchar(30) NOT NULL,
	"property_price"	varchar(30) NOT NULL,
	"property_photo"	varchar(100) NOT NULL,
	"property_status"	integer NOT NULL,
	"category_id_id"	bigint NOT NULL,
	"place_id_id"	bigint NOT NULL,
	"seller_id_id"	bigint,
	"property_date"	date NOT NULL,
	"property_typestatus"	integer,
	"renter_id_id"	bigint,
	"propertytype_id_id"	bigint,
	"bhk_id_id"	bigint,
	"furnish_id_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("bhk_id_id") REFERENCES "Admin_tbl_bhk"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id_id") REFERENCES "Admin_tbl_category"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("furnish_id_id") REFERENCES "Admin_tbl_furnish"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("place_id_id") REFERENCES "Admin_tbl_place"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("propertytype_id_id") REFERENCES "Admin_tbl_propertytype"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("renter_id_id") REFERENCES "Guest_tbl_renter"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("seller_id_id") REFERENCES "Guest_tbl_seller"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "User_tbl_complaint" (
	"id"	integer NOT NULL,
	"complaint_title"	varchar(100) NOT NULL,
	"complaint_content"	varchar(300) NOT NULL,
	"complaint_status"	integer NOT NULL,
	"complaint_date"	date NOT NULL,
	"complaint_reply"	varchar(300) NOT NULL,
	"renter_id_id"	bigint,
	"seller_id_id"	bigint,
	"user_id_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("renter_id_id") REFERENCES "Guest_tbl_renter"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("seller_id_id") REFERENCES "Guest_tbl_seller"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id_id") REFERENCES "Guest_tbl_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "User_tbl_feedback" (
	"id"	integer NOT NULL,
	"feedback_content"	varchar(300) NOT NULL,
	"renter_id_id"	bigint,
	"seller_id_id"	bigint,
	"user_id_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("renter_id_id") REFERENCES "Guest_tbl_renter"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("seller_id_id") REFERENCES "Guest_tbl_seller"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id_id") REFERENCES "Guest_tbl_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "User_tbl_propertybooking" (
	"id"	integer NOT NULL,
	"propertybooking_date"	date NOT NULL,
	"propertybooking_fromdate"	date,
	"propertybooking_amount"	varchar(30) NOT NULL,
	"propertybooking_status"	integer NOT NULL,
	"property_id_id"	bigint NOT NULL,
	"user_id_id"	bigint NOT NULL,
	"propertybooking_todate"	date,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("property_id_id") REFERENCES "Seller_tbl_property"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id_id") REFERENCES "Guest_tbl_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "User_tbl_propertybookingpayment" (
	"id"	integer NOT NULL,
	"propertybookingpayment_date"	date NOT NULL,
	"propertybookingpayment_amount"	varchar(30) NOT NULL,
	"propertybookingpayment_status"	integer NOT NULL,
	"propertybooking_id_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("propertybooking_id_id") REFERENCES "User_tbl_propertybooking"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "User_tbl_propertybuing" (
	"id"	integer NOT NULL,
	"propertybuying_date"	date NOT NULL,
	"propertybuying_amount"	varchar(30) NOT NULL,
	"propertybuying_status"	integer NOT NULL,
	"property_id_id"	bigint NOT NULL,
	"user_id_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("property_id_id") REFERENCES "Seller_tbl_property"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id_id") REFERENCES "Guest_tbl_user"("id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "Admin_tbl_admin" VALUES (1,'Shen','shenbobby@gmail.com','7766885544','123');
INSERT INTO "Admin_tbl_admin" VALUES (2,'Genesis','genesis@gmail.com','8799554532','223');
INSERT INTO "Admin_tbl_admin" VALUES (4,'Adith','Adith@gmail.com','7456443811','adith@123');
INSERT INTO "Admin_tbl_bhk" VALUES (1,'1BHK',2);
INSERT INTO "Admin_tbl_bhk" VALUES (4,'2BHK',2);
INSERT INTO "Admin_tbl_bhk" VALUES (5,'3BHK',2);
INSERT INTO "Admin_tbl_bhk" VALUES (6,'4BHK',2);
INSERT INTO "Admin_tbl_bhk" VALUES (7,'5BHK',2);
INSERT INTO "Admin_tbl_category" VALUES (5,'sell');
INSERT INTO "Admin_tbl_category" VALUES (6,'rent');
INSERT INTO "Admin_tbl_district" VALUES (1,'Ernakulam');
INSERT INTO "Admin_tbl_district" VALUES (2,'Kollam');
INSERT INTO "Admin_tbl_district" VALUES (3,'Pathanamthitta');
INSERT INTO "Admin_tbl_district" VALUES (6,'Alappuzha');
INSERT INTO "Admin_tbl_district" VALUES (8,'idukkii');
INSERT INTO "Admin_tbl_district" VALUES (11,'Thrissur ');
INSERT INTO "Admin_tbl_district" VALUES (12,'Thiruvananthapuram');
INSERT INTO "Admin_tbl_district" VALUES (13,'Kottayam');
INSERT INTO "Admin_tbl_district" VALUES (14,'Palakkad');
INSERT INTO "Admin_tbl_district" VALUES (15,'Malappuram');
INSERT INTO "Admin_tbl_district" VALUES (16,'Kozhikode');
INSERT INTO "Admin_tbl_district" VALUES (17,'Wayanad');
INSERT INTO "Admin_tbl_district" VALUES (18,'Kannur');
INSERT INTO "Admin_tbl_district" VALUES (19,'Kasaragod');
INSERT INTO "Admin_tbl_furnish" VALUES (1,'Furnished',2);
INSERT INTO "Admin_tbl_furnish" VALUES (2,' Semi Furnished ',2);
INSERT INTO "Admin_tbl_furnish" VALUES (3,'Unfurnished',2);
INSERT INTO "Admin_tbl_place" VALUES (1,'edathua',6);
INSERT INTO "Admin_tbl_place" VALUES (2,'Muvattupuzha',1);
INSERT INTO "Admin_tbl_place" VALUES (5,'Anaprampal',6);
INSERT INTO "Admin_tbl_place" VALUES (6,'Karunagappally',2);
INSERT INTO "Admin_tbl_place" VALUES (7,'Kottarakkara',2);
INSERT INTO "Admin_tbl_place" VALUES (8,'Kothamangalam',1);
INSERT INTO "Admin_tbl_place" VALUES (9,'Aluva',1);
INSERT INTO "Admin_tbl_place" VALUES (10,'Fort Kochi',1);
INSERT INTO "Admin_tbl_place" VALUES (11,'Munnar',8);
INSERT INTO "Admin_tbl_place" VALUES (12,'Adimali',8);
INSERT INTO "Admin_tbl_place" VALUES (13,'Haripad',6);
INSERT INTO "Admin_tbl_place" VALUES (15,'West Fort',11);
INSERT INTO "Admin_tbl_place" VALUES (16,'East Fort',11);
INSERT INTO "Admin_tbl_place" VALUES (17,'Guruvayur',11);
INSERT INTO "Admin_tbl_place" VALUES (18,'Kazhakootam',12);
INSERT INTO "Admin_tbl_place" VALUES (19,'Poojapura',12);
INSERT INTO "Admin_tbl_place" VALUES (20,'Vattiyoorkavu',12);
INSERT INTO "Admin_tbl_place" VALUES (21,'Kowdiar',12);
INSERT INTO "Admin_tbl_place" VALUES (22,'Palayam',12);
INSERT INTO "Admin_tbl_place" VALUES (23,'Karyavattom',12);
INSERT INTO "Admin_tbl_place" VALUES (24,'Thampanoor (Central Station)',12);
INSERT INTO "Admin_tbl_place" VALUES (25,'Oachira',2);
INSERT INTO "Admin_tbl_place" VALUES (26,'Asramam',2);
INSERT INTO "Admin_tbl_place" VALUES (27,'Punalur',2);
INSERT INTO "Admin_tbl_place" VALUES (28,'Pathanapuram',2);
INSERT INTO "Admin_tbl_place" VALUES (29,'Kundara',2);
INSERT INTO "Admin_tbl_place" VALUES (30,'Ayoor',2);
INSERT INTO "Admin_tbl_place" VALUES (31,'Kottiyam',2);
INSERT INTO "Admin_tbl_place" VALUES (32,'Adoor',3);
INSERT INTO "Admin_tbl_place" VALUES (33,'Konni',3);
INSERT INTO "Admin_tbl_place" VALUES (34,'Kozhencherry',3);
INSERT INTO "Admin_tbl_place" VALUES (35,'Mallappally',3);
INSERT INTO "Admin_tbl_place" VALUES (36,'Ranni',3);
INSERT INTO "Admin_tbl_place" VALUES (37,'Parumala',3);
INSERT INTO "Admin_tbl_place" VALUES (38,'Pandalam',3);
INSERT INTO "Admin_tbl_place" VALUES (39,'Thiruvalla',3);
INSERT INTO "Admin_tbl_place" VALUES (40,'Ambalappuzha',6);
INSERT INTO "Admin_tbl_place" VALUES (41,'Cherthala',6);
INSERT INTO "Admin_tbl_place" VALUES (42,'Mannar',6);
INSERT INTO "Admin_tbl_place" VALUES (43,'Mavelikkara',6);
INSERT INTO "Admin_tbl_place" VALUES (44,'Kuttanad',6);
INSERT INTO "Admin_tbl_place" VALUES (45,'Changanassery',13);
INSERT INTO "Admin_tbl_place" VALUES (46,'Pala',13);
INSERT INTO "Admin_tbl_place" VALUES (47,'Ettumanoor',13);
INSERT INTO "Admin_tbl_place" VALUES (48,'Vagamon',13);
INSERT INTO "Admin_tbl_place" VALUES (49,'Mundakayam',13);
INSERT INTO "Admin_tbl_place" VALUES (50,'Meenachil',13);
INSERT INTO "Admin_tbl_place" VALUES (51,'Chingavanam',13);
INSERT INTO "Admin_tbl_place" VALUES (52,'Baker Junction',13);
INSERT INTO "Admin_tbl_place" VALUES (53,'Kattappana',8);
INSERT INTO "Admin_tbl_place" VALUES (54,'Kumily',8);
INSERT INTO "Admin_tbl_place" VALUES (55,'Devikulam',8);
INSERT INTO "Admin_tbl_place" VALUES (56,'Chinnakanal',8);
INSERT INTO "Admin_tbl_place" VALUES (57,'Nedumkandam',8);
INSERT INTO "Admin_tbl_place" VALUES (58,'Cheruthoni',8);
INSERT INTO "Admin_tbl_place" VALUES (59,'Idukki Dam',8);
INSERT INTO "Admin_tbl_place" VALUES (60,'Angamaly',1);
INSERT INTO "Admin_tbl_place" VALUES (61,'Perumbavoor',1);
INSERT INTO "Admin_tbl_place" VALUES (62,'Kakkanad',1);
INSERT INTO "Admin_tbl_place" VALUES (63,'Thrippunithura',1);
INSERT INTO "Admin_tbl_place" VALUES (64,'Kaloor',1);
INSERT INTO "Admin_tbl_place" VALUES (65,'Infopark',1);
INSERT INTO "Admin_tbl_place" VALUES (66,'Kalady',1);
INSERT INTO "Admin_tbl_place" VALUES (67,'Chalakudy',11);
INSERT INTO "Admin_tbl_place" VALUES (68,'Irinjalakuda',11);
INSERT INTO "Admin_tbl_place" VALUES (69,'Kodungallur',11);
INSERT INTO "Admin_tbl_place" VALUES (70,'Athirappilly',11);
INSERT INTO "Admin_tbl_place" VALUES (71,'Vazhachal',11);
INSERT INTO "Admin_tbl_place" VALUES (72,'Kunnamkulam',11);
INSERT INTO "Admin_tbl_propertytype" VALUES (1,'Land');
INSERT INTO "Admin_tbl_propertytype" VALUES (2,'Building');
INSERT INTO "Guest_tbl_renter" VALUES (1,'BMW','bmw@gmail.com','6166332366','Ernakulam,Muvattupuzha','Assets/User/A4_paper.jpg','Assets/User/A4_paper.jpg','bmw12',6,1);
INSERT INTO "Guest_tbl_renter" VALUES (2,'Ace','ace26@example.com','7800236110','Ace Creative 45 Innovation Drive, Suite 200 Tech Park District London, W1T 1AB UK','Assets/User/Portraits-Chicago-Giovanni-4.jpg.webp','Assets/User/classmate-a4-size-notebook_zkXhEYO.jpg','Ace12',9,2);
INSERT INTO "Guest_tbl_seller" VALUES (1,'Rino k','rino18@gmail.com','7718811118','Ernakulam,Muvattupuzha','Assets/User/A4_paper.jpg','Assets/User/1363137.png','1188',2,1);
INSERT INTO "Guest_tbl_seller" VALUES (2,'abc123','abc123@gmail.com','665554467','Ernakulam,Muvattupuzha','Assets/User/Classmate_3_Subject_Book_Spiral_240_Pages_Single_Piece.jpg','Assets/User/801.webp','abc123',2,2);
INSERT INTO "Guest_tbl_user" VALUES (1,'Shen Varghese Bobby','shenbobby8@gmail.com','7766885533','Ernakulam,Muvattupuzha','Assets/User/lamp02_Bmy0hs8.png','123',2,1);
INSERT INTO "Guest_tbl_user" VALUES (2,'Apple123','apple12@gmail.com','3212564431','United Kingdom','Assets/User/Apple.avif','apap',2,1);
INSERT INTO "Guest_tbl_user" VALUES (3,'Apple','apple1@gmail.com','3212564431','UK','Assets/User/Apple1.avif','3333',2,2);
INSERT INTO "Guest_tbl_user" VALUES (5,'CR7','cr7@gmail.com','7777777333','Suite Q, Athene House, 86 The Broadway, London','Assets/User/inosuke-hashibira-5120x2880-23650_EnONbsQ.jpg','Cr_777777',9,1);
INSERT INTO "Guest_tbl_user" VALUES (6,'Ajo','Ajo12@gmail.com','3216371110','abcdefch','Assets/User/Screenshot_2026-02-24_161913.png','AB@#_abc1234567',46,1);
INSERT INTO "Seller_tbl_gallery" VALUES (12,'Assets/Property/Gallery/zenitsu-agatsuma-5120x2880-22696_L9EXie6.png',8);
INSERT INTO "Seller_tbl_gallery" VALUES (18,'Assets/Property/Gallery/pen_xHO6Ev8.jpg',8);
INSERT INTO "Seller_tbl_gallery" VALUES (19,'Assets/Property/Gallery/Apple.avif',8);
INSERT INTO "Seller_tbl_gallery" VALUES (20,'Assets/Property/Gallery/360_F_1067525262_9xIrN9lVnWDQhq0x8vnPCxOrUogrHkjt_TFgoThu.jpg',16);
INSERT INTO "Seller_tbl_gallery" VALUES (21,'Assets/Property/Gallery/Classmate_3_Subject_Book_Spiral_240_Pages_Single_Piece.jpg',16);
INSERT INTO "Seller_tbl_gallery" VALUES (22,'Assets/Property/Gallery/zenitsu-agatsuma-5120x2880-23643.jpg',10);
INSERT INTO "Seller_tbl_gallery" VALUES (24,'Assets/Property/Gallery/zenitsu-agatsuma-5120x2880-17046_3WcOwyA.jpg',18);
INSERT INTO "Seller_tbl_gallery" VALUES (25,'Assets/Property/Gallery/801_5pI3OQd.webp',18);
INSERT INTO "Seller_tbl_gallery" VALUES (26,'Assets/Property/Gallery/Apple_Mp2uIw7.avif',10);
INSERT INTO "Seller_tbl_gallery" VALUES (27,'Assets/Property/Gallery/stock-photo-happy-funny-people-isolated-over-white-background-52877164.jpg',11);
INSERT INTO "Seller_tbl_gallery" VALUES (28,'Assets/Property/Gallery/olena-bohovyk-ElfJDs4LAQk-unsplash_oFoMNJp.jpg',11);
INSERT INTO "Seller_tbl_gallery" VALUES (29,'Assets/Property/Gallery/demon-slayer-5120x2880-23247.jpg',15);
INSERT INTO "Seller_tbl_gallery" VALUES (30,'Assets/Property/Gallery/801_pU9aQcU.webp',15);
INSERT INTO "Seller_tbl_gallery" VALUES (31,'Assets/Property/Gallery/article_hero_lab_retriever.avif',20);
INSERT INTO "Seller_tbl_gallery" VALUES (32,'Assets/Property/Gallery/puttu-and-curry-1_OL9hjZb.jpeg',20);
INSERT INTO "Seller_tbl_gallery" VALUES (33,'Assets/Property/Gallery/Apple_Ob68T7q.avif',20);
INSERT INTO "Seller_tbl_gallery" VALUES (34,'Assets/Property/Gallery/1.jpg',24);
INSERT INTO "Seller_tbl_gallery" VALUES (35,'Assets/Property/Gallery/1.2.jpg',24);
INSERT INTO "Seller_tbl_gallery" VALUES (36,'Assets/Property/Gallery/1.3.jpg',24);
INSERT INTO "Seller_tbl_gallery" VALUES (37,'Assets/Property/Gallery/1.4.jpg',24);
INSERT INTO "Seller_tbl_gallery" VALUES (38,'Assets/Property/Gallery/2.jpg',25);
INSERT INTO "Seller_tbl_gallery" VALUES (39,'Assets/Property/Gallery/2.2.jpg',25);
INSERT INTO "Seller_tbl_gallery" VALUES (40,'Assets/Property/Gallery/2.3.jpg',25);
INSERT INTO "Seller_tbl_gallery" VALUES (41,'Assets/Property/Gallery/2.4.jpg',25);
INSERT INTO "Seller_tbl_gallery" VALUES (42,'Assets/Property/Gallery/2.5.jpg',25);
INSERT INTO "Seller_tbl_gallery" VALUES (43,'Assets/Property/Gallery/2.6.jpg',25);
INSERT INTO "Seller_tbl_gallery" VALUES (44,'Assets/Property/Gallery/2.7.jpg',25);
INSERT INTO "Seller_tbl_gallery" VALUES (45,'Assets/Property/Gallery/2.8.jpg',25);
INSERT INTO "Seller_tbl_gallery" VALUES (46,'Assets/Property/Gallery/2.9.jpg',25);
INSERT INTO "Seller_tbl_gallery" VALUES (47,'Assets/Property/Gallery/2.10.jpg',25);
INSERT INTO "Seller_tbl_gallery" VALUES (48,'Assets/Property/Gallery/2.11.jpg',25);
INSERT INTO "Seller_tbl_gallery" VALUES (49,'Assets/Property/Gallery/2.12.jpg',25);
INSERT INTO "Seller_tbl_gallery" VALUES (50,'Assets/Property/Gallery/3.1.jpg',26);
INSERT INTO "Seller_tbl_gallery" VALUES (51,'Assets/Property/Gallery/3.2.jpg',26);
INSERT INTO "Seller_tbl_gallery" VALUES (52,'Assets/Property/Gallery/3.3.jpg',26);
INSERT INTO "Seller_tbl_gallery" VALUES (53,'Assets/Property/Gallery/3.4.jpg',26);
INSERT INTO "Seller_tbl_gallery" VALUES (54,'Assets/Property/Gallery/3.5.jpg',26);
INSERT INTO "Seller_tbl_gallery" VALUES (55,'Assets/Property/Gallery/3.6.jpg',26);
INSERT INTO "Seller_tbl_gallery" VALUES (56,'Assets/Property/Gallery/3.7.jpg',26);
INSERT INTO "Seller_tbl_gallery" VALUES (57,'Assets/Property/Gallery/3.8.jpg',26);
INSERT INTO "Seller_tbl_gallery" VALUES (58,'Assets/Property/Gallery/3.9.jpg',26);
INSERT INTO "Seller_tbl_gallery" VALUES (59,'Assets/Property/Gallery/3.10.jpg',26);
INSERT INTO "Seller_tbl_gallery" VALUES (60,'Assets/Property/Gallery/3.11.jpg',26);
INSERT INTO "Seller_tbl_property" VALUES (8,'Nokia','12345678910abcd','1000','Assets/Property/Photo/Apple_JYXc2S6.avif',1,6,1,NULL,'2025-12-17',0,1,1,NULL,NULL);
INSERT INTO "Seller_tbl_property" VALUES (10,'Ajo','abdcefg1234567','100000000','Assets/Property/Photo/inosuke-hashibira-5120x2880-23650.jpg',0,5,9,1,'2026-01-13',1,NULL,1,NULL,NULL);
INSERT INTO "Seller_tbl_property" VALUES (11,'Hari','mnbvzcxaszdgeidh','123456712','Assets/Property/Photo/lamp02.png',1,6,8,NULL,'2026-01-13',0,1,2,1,1);
INSERT INTO "Seller_tbl_property" VALUES (15,'2026','22220000022226666','7676456354000','Assets/Property/Photo/article_hero_lab_retriever.avif',0,5,12,2,'2026-01-14',1,NULL,2,4,2);
INSERT INTO "Seller_tbl_property" VALUES (16,'LMNO','1a2b3c4d5e6f','120000000','Assets/Property/Photo/zenitsu-agatsuma-5120x2880-17046.jpg',1,6,2,NULL,'2026-01-14',0,2,2,1,3);
INSERT INTO "Seller_tbl_property" VALUES (18,'Genesis','qwertyuiopplkmnbv','1000','Assets/Property/Photo/gluten-free-dosa-1-e1722870434177.webp',0,5,7,1,'2026-01-14',1,NULL,1,NULL,NULL);
INSERT INTO "Seller_tbl_property" VALUES (20,'Hilltop','"Hill Top"
AB & DE Smith
AUSTRALIA','1000','Assets/Property/Photo/zenitsu-agatsuma-5120x2880-20236_xzWfQ2B.jpg',0,6,5,NULL,'2026-01-16',0,1,1,NULL,NULL);
INSERT INTO "Seller_tbl_property" VALUES (21,'Blue Haven','2 BHK IndependentHome,
Near City Center, calm residential area','2500000','Assets/Property/Photo/eltCKVcVTeml3jerlfulsg_0f2528ec_Yth0HE7.jpg',0,5,9,1,'2026-02-02',1,NULL,2,4,3);
INSERT INTO "Seller_tbl_property" VALUES (22,'Happy Nest','3 BHK,Prime residential area with easy access to schools, hospitals, and shopping centers','12000','Assets/Property/Photo/360_F_1067525262_9xIrN9lVnWDQhq0x8vnPCxOrUogrHkjt_pig7Zk3.jpg',0,6,12,NULL,'2026-02-02',0,1,2,1,2);
INSERT INTO "Seller_tbl_property" VALUES (23,'ASUS','qwertyuiopasdfghjklasdfghjklzxcvbnm','23332','Assets/Property/Photo/puttu-and-curry-1.jpeg',0,5,17,1,'2026-02-07',1,NULL,2,4,1);
INSERT INTO "Seller_tbl_property" VALUES (24,'4 Bedroom House For Sale, 2500 sqft','A well-maintained 4 bedroom independent house situated in a peaceful residential area of Permbra, Calicut. 
Ideal for families looking for a spacious home with nearby amenities.


Property Details
• Land Area: 15 cents
• Built-up Area: Approx. 2500 sq. ft.
• Bathrooms: 3 (2 attached bathrooms)
• Type: Independent residential house
• Condition: Ready to occupy / well maintained','65K','Assets/Property/Photo/1.jpg',0,5,11,1,'2026-02-11',1,NULL,2,NULL,NULL);
INSERT INTO "Seller_tbl_property" VALUES (25,'3Bhk Independent House/Villa for Rent','This 3 bhk house for  sell in nettoor, is available now. This property is one of the most prominent housing societies ','50K','Assets/Property/Photo/2.jpg',0,5,9,1,'2026-02-11',1,NULL,2,NULL,NULL);
INSERT INTO "Seller_tbl_property" VALUES (26,'3Bedrooms 2Baths','3bhk independent house , just 200 meter from mg college and 500 meter from marivanious college.','20000','Assets/Property/Photo/3.1.jpg',0,6,18,NULL,'2026-02-11',0,1,2,NULL,NULL);
INSERT INTO "User_tbl_complaint" VALUES (4,'Renter','abcdefghi',1,'2026-01-20','hello',NULL,NULL,2);
INSERT INTO "User_tbl_complaint" VALUES (5,'Seller','money is to big',1,'2026-01-28','ok',NULL,NULL,2);
INSERT INTO "User_tbl_complaint" VALUES (7,'Renter','cacbcybcb',1,'2026-01-28','dncbcbee',NULL,NULL,2);
INSERT INTO "User_tbl_complaint" VALUES (10,'Seller','bewbvwebbc',1,'2026-01-28','cjbwcbww',NULL,1,NULL);
INSERT INTO "User_tbl_complaint" VALUES (12,'ncuien','mccwwecdwhece',1,'2026-01-28','hecuewucuqe',1,NULL,NULL);
INSERT INTO "User_tbl_complaint" VALUES (13,'Seller','rghfchgbjjkjhcg',0,'2026-02-05','',NULL,1,NULL);
INSERT INTO "User_tbl_complaint" VALUES (14,'Seller','hi',0,'2026-03-02','',NULL,1,NULL);
INSERT INTO "User_tbl_feedback" VALUES (1,'zrxdcfvgbhnj',NULL,NULL,2);
INSERT INTO "User_tbl_feedback" VALUES (2,'very good',NULL,1,NULL);
INSERT INTO "User_tbl_feedback" VALUES (3,'there is an error in addproperty page',1,NULL,NULL);
INSERT INTO "User_tbl_feedback" VALUES (4,'euhdeehuehcu',NULL,NULL,2);
INSERT INTO "User_tbl_feedback" VALUES (5,'cjnjecncniq',1,NULL,NULL);
INSERT INTO "User_tbl_feedback" VALUES (6,'cnniwiiiiiw',NULL,1,NULL);
INSERT INTO "User_tbl_feedback" VALUES (7,'chehvcev',NULL,1,NULL);
INSERT INTO "User_tbl_feedback" VALUES (8,'akkjkdgh',NULL,1,NULL);
INSERT INTO "User_tbl_feedback" VALUES (9,'hiiii',1,NULL,NULL);
INSERT INTO "User_tbl_propertybooking" VALUES (35,'2026-01-29','2026-01-29','123456712',1,11,2,'2026-02-28');
INSERT INTO "User_tbl_propertybooking" VALUES (41,'2026-02-10','2026-02-10','7132',1,20,2,'2026-09-12');
INSERT INTO "User_tbl_propertybookingpayment" VALUES (59,'2026-01-29','123456690',1,35);
INSERT INTO "User_tbl_propertybookingpayment" VALUES (68,'2026-02-10','1000',1,41);
INSERT INTO "User_tbl_propertybookingpayment" VALUES (69,'2026-02-10','1000',1,41);
INSERT INTO "User_tbl_propertybookingpayment" VALUES (70,'2026-02-10','1000',1,41);
INSERT INTO "User_tbl_propertybookingpayment" VALUES (71,'2026-02-10','1000',0,41);
INSERT INTO "User_tbl_propertybookingpayment" VALUES (72,'2026-02-10','1000',0,41);
INSERT INTO "User_tbl_propertybookingpayment" VALUES (73,'2026-02-10','1000',0,41);
INSERT INTO "User_tbl_propertybookingpayment" VALUES (74,'2026-02-10','1000',0,41);
INSERT INTO "User_tbl_propertybookingpayment" VALUES (75,'2026-02-10','132',0,41);
INSERT INTO "User_tbl_propertybuing" VALUES (16,'2026-01-20','100000000',1,10,2);
INSERT INTO "User_tbl_propertybuing" VALUES (18,'2026-01-29','1000',1,18,2);
INSERT INTO "User_tbl_propertybuing" VALUES (20,'2026-02-02','2500000',1,21,2);
INSERT INTO "User_tbl_propertybuing" VALUES (24,'2026-02-10','23332',1,23,2);
CREATE INDEX IF NOT EXISTS "Admin_tbl_bhk_propertytype_id_fde2dc60" ON "Admin_tbl_bhk" (
	"propertytype_id"
);
CREATE INDEX IF NOT EXISTS "Admin_tbl_furnish_propertytype_id_61c59e84" ON "Admin_tbl_furnish" (
	"propertytype_id"
);
CREATE INDEX IF NOT EXISTS "Admin_tbl_place_district_id_08f368dc" ON "Admin_tbl_place" (
	"district_id"
);
CREATE INDEX IF NOT EXISTS "Admin_tbl_subcategory_category_id_093bff13" ON "Admin_tbl_subcategory" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "Guest_tbl_renter_place_id_aca2ccb6" ON "Guest_tbl_renter" (
	"place_id"
);
CREATE INDEX IF NOT EXISTS "Guest_tbl_seller_place_id_c3ff8ae1" ON "Guest_tbl_seller" (
	"place_id"
);
CREATE INDEX IF NOT EXISTS "Guest_tbl_user_place_id_524b89bc" ON "Guest_tbl_user" (
	"place_id"
);
CREATE INDEX IF NOT EXISTS "Seller_tbl_gallery_property_id_5049b402" ON "Seller_tbl_gallery" (
	"property_id"
);
CREATE INDEX IF NOT EXISTS "Seller_tbl_property_bhk_id_id_a3f45b6c" ON "Seller_tbl_property" (
	"bhk_id_id"
);
CREATE INDEX IF NOT EXISTS "Seller_tbl_property_category_id_id_29310934" ON "Seller_tbl_property" (
	"category_id_id"
);
CREATE INDEX IF NOT EXISTS "Seller_tbl_property_furnish_id_id_221bea86" ON "Seller_tbl_property" (
	"furnish_id_id"
);
CREATE INDEX IF NOT EXISTS "Seller_tbl_property_place_id_id_ab05a8f9" ON "Seller_tbl_property" (
	"place_id_id"
);
CREATE INDEX IF NOT EXISTS "Seller_tbl_property_propertytype_id_id_322e2fdf" ON "Seller_tbl_property" (
	"propertytype_id_id"
);
CREATE INDEX IF NOT EXISTS "Seller_tbl_property_renter_id_id_cff368d9" ON "Seller_tbl_property" (
	"renter_id_id"
);
CREATE INDEX IF NOT EXISTS "Seller_tbl_property_seller_id_id_52e32be2" ON "Seller_tbl_property" (
	"seller_id_id"
);
CREATE INDEX IF NOT EXISTS "User_tbl_complaint_renter_id_id_efe8ba9f" ON "User_tbl_complaint" (
	"renter_id_id"
);
CREATE INDEX IF NOT EXISTS "User_tbl_complaint_seller_id_id_3a91c07d" ON "User_tbl_complaint" (
	"seller_id_id"
);
CREATE INDEX IF NOT EXISTS "User_tbl_complaint_user_id_id_f5e63799" ON "User_tbl_complaint" (
	"user_id_id"
);
CREATE INDEX IF NOT EXISTS "User_tbl_feedback_renter_id_id_cb7c15a7" ON "User_tbl_feedback" (
	"renter_id_id"
);
CREATE INDEX IF NOT EXISTS "User_tbl_feedback_seller_id_id_41b41584" ON "User_tbl_feedback" (
	"seller_id_id"
);
CREATE INDEX IF NOT EXISTS "User_tbl_feedback_user_id_id_d78aeb3a" ON "User_tbl_feedback" (
	"user_id_id"
);
CREATE INDEX IF NOT EXISTS "User_tbl_propertybooking_property_id_id_166eef10" ON "User_tbl_propertybooking" (
	"property_id_id"
);
CREATE INDEX IF NOT EXISTS "User_tbl_propertybooking_user_id_id_3af92d12" ON "User_tbl_propertybooking" (
	"user_id_id"
);
CREATE INDEX IF NOT EXISTS "User_tbl_propertybookingpayment_propertybooking_id_id_b455fc9e" ON "User_tbl_propertybookingpayment" (
	"propertybooking_id_id"
);
CREATE INDEX IF NOT EXISTS "User_tbl_propertybuing_property_id_id_5fd9e499" ON "User_tbl_propertybuing" (
	"property_id_id"
);
CREATE INDEX IF NOT EXISTS "User_tbl_propertybuing_user_id_id_46848b14" ON "User_tbl_propertybuing" (
	"user_id_id"
);
COMMIT;
