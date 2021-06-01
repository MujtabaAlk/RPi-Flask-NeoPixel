DROP TABLE IF EXISTS user_type;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    type INTEGER DEFAULT 1,
    FOREIGN KEY (type) REFERENCES user_type (id)
);

INSERT INTO user_type
    (title)
VALUES
    ('USER'),
    ('ADMIN');
