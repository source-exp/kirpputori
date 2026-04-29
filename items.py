import db

def get_images(item_id):
    sql = "SELECT id FROM images WHERE item_id = ?"
    return db.query(sql, [item_id])

def add_image(item_id, image):
    sql = "INSERT INTO images (item_id, image) VALUES (?, ?)"
    db.execute(sql, [item_id, image])

def get_image(image_id):
    sql = "SELECT image FROM images WHERE id = ?"
    result = db.query(sql, [image_id])
    return result[0][0] if result else None

def remove_image(item_id, image_id):
    sql = "DELETE FROM images WHERE id = ? AND item_id = ?"
    db.execute(sql, [image_id, item_id])

def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes

def add_item(title, description, price, user_id, classes):
    sql = """INSERT INTO items (title, description, price, user_id)
             VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, description, price, user_id])
    item_id = db.last_insert_id()
    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?,?,?)"
    for title, value in classes:
        db.execute(sql,[item_id, title, value])

def get_classes(item_id):
    sql = "SELECT title, value FROM item_classes WHERE item_id = ?"
    return db.query(sql, [item_id])

def get_item(item_id):
    sql = """SELECT items.id,
                    items.title,
                    items.description,
                    items.price,
                    users.id user_id,
                    users.username
             FROM items, users
             WHERE items.user_id = users.id AND
                   items.id = ?"""
    result = db.query(sql, [item_id])
    return result[0] if result else None

def get_items():
    sql = """SELECT items.id, 
                    items.title, 
                    items.price, 
                    users.id user_id, 
                    users.username 
    FROM items JOIN users ON items.user_id = users.id
    ORDER BY items.id DESC"""
    return db.query(sql)

def update_item(item_id, title, price, description, classes):
    sql = """UPDATE items SET title = ?,
                        description = ?,
                        price = ?
                        WHERE id = ?"""
    db.execute(sql, [title, description, price, item_id])

    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])

def remove_item(item_id):
    sql = "DELETE FROM messages WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM images WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])


def find_items(query, classes):
    sql = """SELECT items.id, 
                    items.title, 
                    items.price, 
                    users.id user_id, 
                    users.username 
             FROM items JOIN users ON items.user_id = users.id"""

    params = []
    where_query = []

    if query:
        where_query.append("(items.title LIKE ? OR items.description LIKE ?)")
        like = "%" + query + "%"
        params.extend([like, like])

    if classes:
        for c, class_value in enumerate(classes):
            title, value = class_value.split(":",1)
            alias = f"ic{c}"
            sql += f" JOIN item_classes {alias} ON items.id = {alias}.item_id"
            where_query.append(f"{alias}.title = ? AND {alias}.value = ?")
            params.extend([title, value])
    
    if where_query:
        sql += " WHERE " + " AND ".join(where_query)

    sql += " GROUP BY items.id ORDER BY items.id DESC"

    return db.query(sql, params)