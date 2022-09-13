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

create table student_group (
group_id int (4) AUOT_INCREMENT,
group_number int (4) NOT NULL,
PRIMARY KEY (group_ID)
);

create table reservation (
time int (4) NOT NULL,
res_teacher varchar (50),
res_room int (4),
res_groop int (4),
PRIMARY KEY (time, res_room),
FOREIGN KEY (res_teacher) REFERENCES teacher (teacher_id),
FOREIGN KEY (res_room) REFERENCES room (room_id),
FOREIGN KEY (res_group) REFERENCES student_group (groop_id)
);