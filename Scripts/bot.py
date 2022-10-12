create table profile (
user_id number (4) AUTO_INCREMENT,
birthday number (6) NOT NULL,
F.I.O varchar (30) NOT NULL,
sex (1) NOT NULL
PRIMARY KEY (user_id)
);

create table attribute (
user_id number(4) NOT NULL,
attribute_id number (4) AUYO_INCREMENT,
autoCreate (1),										???
type number(2) NOT NULL,							???
description vrchar (50),
PRIMARY KEY (attribute_id),
unique (user_id, type),
FOREIGN KEY (user_id) PEFERENSES profile (user_id)
);

create teble attibute-view (
ancher number(4) NOT NULL,
attribute_id number (4) NOT NULL,
view_id number (4) AUTO_INCREMENT,
image number (2),									???
PRIMARY KEY (view_id),
unique (attribute_id, arher)
FORIGN KEY (attribute-id) REFERENSES attribute (attribute_id)
);

create table view (
view_id number (4) AUTO_INCREMENT,
PRIMARY KEY (view_id),
FOREIGN KEY (view_id) REFERENSES attribute-view ( view_id)
);

create table data (
user_id number (4) AUTO_INCREMENT,
attribute_id number (4) NOT NULL,
view_id number (4) NOT NULL,
date number (4) NOT NULL,
value verchar (50) NOT NULL,
PRIMARY KEY (date)
unique (user_id, view_id)
FOREIGN KEY (user_id) REFERENSES profile (user_id),
FOREIGN KEY (view_id) REFERENSES view ( view_id),
FOREIGN KEY (attribute_id) REFERENSES attribute (attribute_id)
);