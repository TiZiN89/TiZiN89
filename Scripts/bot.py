create table teacher (
teacher_id int (4) AUTO_INCREMENT,
Name_FIO varchar (50) NOT NULL,
PRIMARY KEY (teacher_id)
);

create table room (
room_id int (4) AUTO_INCREMENT,
room_number int (4) NOT NULL,
PRIMARY KEY (room_id)
);

create table student_groop (
groop_id int (4) AUOT_INCREMENT,
groop_number int (4) NOT NULL,
PRIMARY KEY (groop_ID)
);

create table reservation (
time int (4) NOT NULL,
res_teacher varchar (50) NULL,
res_room int (4) NULL,
res_groop int (4) NULL,
PRIMARY KEY (time),
FOREIGN KEY (res_teacher) REFERENCES users (teacher_id),
FOREIGN KEY (res_room) REFERENCES users (room_id),
FOREIGN KEY (res_groop) REFERENCES users (groop_id)
);