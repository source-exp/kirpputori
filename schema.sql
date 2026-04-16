CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY,
	username TEXT UNIQUE NOT NULL, 
	password_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS items (
	id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	description TEXT,
	price INTEGER NOT NULL,
	user_id INTEGER NOT NULL REFERENCES users
);

CREATE TABLE IF NOT EXISTS classes (
	id INTEGER PRIMARY KEY,
	title TEXT,
	value TEXT
);

CREATE TABLE IF NOT EXISTS item_classes(
	id INTEGER PRIMARY KEY,
	item_id INTEGER REFERENCES items,
	title TEXT,
	value TEXT
);

CREATE TABLE IF NOT EXISTS messages(
	id INTEGER PRIMARY KEY,
	sender_id INTEGER NOT NULL REFERENCES users(id),
	receiver_id INTEGER NOT NULL REFERENCES users(id),
	item_id INTEGER NOT NULL REFERENCES items(id),
	content TEXT NOT NULL,
	sent_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE images(
	id INTEGER PRIMARY KEY,
	item_id INTEGER REFERENCES items(id),
	image BLOB
);

CREATE INDEX IF NOT EXISTS idx_messages_sender ON messages(sender_id);
CREATE INDEX IF NOT EXISTS idx_messages_receiver ON messages(receiver_id);
CREATE INDEX IF NOT EXISTS idx_messages_item ON messages(item_id);
CREATE INDEX IF NOT EXISTS idx_messages_chat_history ON messages(item_id, sender_id, receiver_id);