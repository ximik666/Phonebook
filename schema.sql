drop table if exists fio;
    create table fio (
    id integer primary key autoincrement,
    fio text not null,
    is_deleted boolean not null default false ,
    time_added time
);
drop table if exists number;
    create table number (
    id integer primary key autoincrement,
    number text,
    fio_id integer not null,
    type_number_id integer,
    is_deleted boolean not null default false ,
    time_added time,
    FOREIGN KEY(fio_id) REFERENCES fio(id),
    FOREIGN KEY(type_number_id) REFERENCES type_number(id)
);
drop table if exists skype_address;
    create table skype_address (
    id integer primary key autoincrement,
    skype_address text,
    fio_id integer not null,
    is_deleted boolean not null default false ,
    time_added time,
    FOREIGN KEY(fio_id) REFERENCES fio(id)
);
drop table if exists type_number;
    create table type_number (
    id integer primary key autoincrement,
    type_number text

);