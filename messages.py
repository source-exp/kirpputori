import db

def get_user_chats(user_id):
	sql = """SELECT i.id AS item_id, i.title, 
    CASE WHEN m.sender_id = ? THEN m.receiver_id 
    ELSE m.sender_id END AS partner_id,
    u.username AS partner_name, MAX(m.sent_at) AS last_time
    FROM items AS i
    JOIN messages AS m ON i.id = m.item_id
    JOIN users AS u ON u.id = CASE WHEN m.sender_id = ? THEN m.receiver_id 
    ELSE m.sender_id END
    WHERE m.sender_id = ? OR m.receiver_id = ?
    GROUP BY i.id, partner_id
    ORDER BY last_time DESC"""
	return db.query(sql, [user_id, user_id, user_id, user_id])

def get_chat_history(user_id, item_id, partner_id):
	sql = """SELECT m.*, u.username AS sender_name
	FROM messages AS m
	JOIN users AS u ON m.sender_id = u.id
	WHERE m.item_id = ? 
	AND ((m.sender_id = ? AND m.receiver_id = ?)
	OR (m.sender_id = ? AND m.receiver_id = ?))
	ORDER BY m.sent_at ASC"""
	return db.query(sql, [item_id, user_id, partner_id, partner_id, user_id])

def send_message(sender_id, receiver_id, item_id, content):
	sql = "INSERT INTO messages (sender_id, receiver_id, item_id, content) VALUES (?, ?, ?, ?)"
	db.execute(sql, [sender_id, receiver_id, item_id, content])