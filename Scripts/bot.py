ccreate table teacher (
Name_FIO varchar (50) NOT NULL,
PRIMARY KEY (Name_FIO)
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
res_room int (4),
res_groop int (4),
PRIMARY KEY (res_id),
FOREIGN KEY (res_teacher) REFERENCES teacher (teacher_id),
FOREIGN KEY (res_room) REFERENCES room (room_id),
FOREIGN KEY (res_group) REFERENCES student_group (groop_id)
);