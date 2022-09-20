CREATE DATABASE db;
\c db;

CREATE TABLE message (
    id SERIAL NOT NULL,
    username VARCHAR(100) NOT NULL,
    content VARCHAR(140) NOT NULL,
    likes int not null default 0,
    time_posted timestamp default now(),
    PRIMARY KEY (id)
);
