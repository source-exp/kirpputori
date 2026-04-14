CREATE TABLE users (
	id INTEGER PRIMARY KEY,
	username TEXT UNIQUE NOT NULL, 
	password_hash TEXT NOT NULL
);

CREATE TABLE items (
	id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	description TEXT,
	price INTEGER NOT NULL,
	user_id INTEGER NOT NULL REFERENCES users
);

CREATE TABLE classes (
	id INTEGER PRIMARY KEY,
	title TEXT,
	value TEXT
);

CREATE TABLE item_classes(
	id INTEGER PRIMARY KEY,
	item_id INTEGER REFERENCES items,
	title TEXT,
	value TEXT
);