import random
import string
import db
import users
import items
import messages
from app import app

user_count = 100
item_per_user = 25
messages_per_user = 25

def random_text(length=10):
    return ''.join(random.choices(string.ascii_lowercase + " ", k=length)).strip()

def main():
    db.init_db()
    all_classes = items.get_all_classes()

    for i in range(user_count):
        username = f"kayttaja_{i}_{random_text(4)}"
        users.create_user(username, "0")

        for _ in range(item_per_user):
            title = f"Myydään {random_text(8)}"
            price = random.randint(1, 10000)
            description = random_text(100)
            class_osasto = random.choice(all_classes["Osasto"])
            class_kunto = random.choice(all_classes["Kunto"])
            classes = [("Osasto", class_osasto), ("Kunto", class_kunto)]
            items.add_item(title, description, price, i + 1, classes)
    
    for _ in range(messages_per_user):
        sender_id = random.randint(1, user_count)
        while True:
            item_id = random.randint(1, user_count * item_per_user)
            receiver_item = items.get_item(item_id)
            if receiver_item and receiver_item["user_id"] != sender_id:
                receiver_id = receiver_item["user_id"]
                break
        content = f"Hei, olen kiinnostunut tästä! {random_text(15)}?"
        messages.send_message(sender_id, receiver_id, item_id, content)

if __name__ == "__main__":
    with app.app_context():
        main()
