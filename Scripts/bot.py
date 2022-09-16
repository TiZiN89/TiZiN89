create table teacher (
teacher_id int (4) AUTO INCREMENT,
Name_FIO varchar (50) NOT NULL,
PRIMARY KEY (teacher_id)
);

create table room (
room_number int (4) NOT NULL,
PRIMARY KEY (room_number)
);

create table student_group (
group_number int (4) NOT NULL,
PRIMARY KEY (group_number)
);

create table reservation (
res_id int (4) AUTO INCREMENT,
time int (4) NOT NULL,
res_teacher varchar (50),
res_room int (4) NOT NULL,
res_groop int (4) NOT NULL,
PRIMARY KEY (res_id),
ALTERNATE KEYS (time, res_room)
FOREIGN KEY (res_teacher) REFERENCES teacher (teacher_id),
FOREIGN KEY (res_room) REFERENCES room (room_id),
FOREIGN KEY (res_group) REFERENCES student_group (groop_id)
);