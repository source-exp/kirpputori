from flask import Flask
from flask import abort, render_template, request, session, redirect, make_response, flash
import sqlite3
import config
import db
import items
import re
import users
import messages
import secrets

app = Flask(__name__)
app.secret_key = config.secret_key
db.init_db()

def require_login():
    if "user_id" not in session:
        abort(403)

def check_csrf():
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

@app.route("/")
def index():
    all_items = items.get_items()
    return render_template("index.html", items=all_items)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    items = users.get_items(user_id)
    return render_template("show_user.html", user=user, items=items)

@app.route("/messages")
def list_chats():
    require_login()
    chats = messages.get_user_chats(session["user_id"])
    return render_template("chat_list.html", chats=chats)

@app.route("/messages/<int:item_id>/")
def view_chat_item(item_id):
    require_login()
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if session["user_id"] == item["user_id"]:
        return redirect("/messages")
    return redirect(f"/messages/{item_id}/{item["user_id"]}")

@app.route("/messages/<int:item_id>/<int:partner_id>")
def view_chat(item_id, partner_id):
    require_login()
    item = items.get_item(item_id)
    if not item:
        abort(404)
    chat_history = messages.get_chat_history(session["user_id"], item_id, partner_id)
    return render_template("chat_room.html", item=item, chat_history=chat_history, partner_id=partner_id)

@app.route("/send_message/<int:item_id>", methods=["POST"])
def send_message(item_id):
    require_login()
    check_csrf()
    item = items.get_item(item_id)
    content = request.form["content"]
    receiver_id = item["user_id"]
    if session["user_id"] == item["user_id"]:
        receiver_id = request.form.get("receiver_id")
    if not receiver_id:
        abort(400)
    messages.send_message(session["user_id"], receiver_id, item_id, content)
    return redirect(f"/messages/{item_id}/{receiver_id}")

@app.route("/new_item")
def new_item():
    require_login()
    classes = items.get_all_classes()
    return render_template("new_item.html", classes=classes)

@app.route("/item/<int:item_id>")
def show_item(item_id):
    item = items.get_item(item_id)
    if not item:
        abort(404)
    classes = items.get_classes(item_id)
    images = items.get_images(item_id)
    return render_template("show_item.html", item=item, classes=classes, images=images)

@app.route("/image/<int:image_id>")
def show_image(image_id):
    image = items.get_image(image_id)
    if not image:
        abort(404)
    response = make_response(bytes(image))
    response.headers.set("Content-Type", "image/png")
    return response

@app.route("/images/<int:item_id>")
def edit_images(item_id):
    require_login()
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    images = items.get_images(item_id)

    return render_template("images.html", item=item, images=images)

@app.route("/add_image", methods=["POST"])
def add_image():
    require_login()
    check_csrf()
    item_id = request.form["item_id"]
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    file = request.files["image"]
    if not file.filename.endswith(".png"):
        flash("VIRHE: väärä tiedostomuoto", "error")
        return redirect("/images/" + str(item_id))

    image = file.read()
    if len(image) > 100 * 1024:
        flash("VIRHE: liian suuri kuva", "error")
        return redirect("/images/" + str(item_id))

    items.add_image(item_id, image)
    return redirect("/images/" + str(item_id))

@app.route("/remove_images", methods=["POST"])
def remove_images():
    require_login()
    check_csrf()
    item_id = request.form["item_id"]
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    for image_id in request.form.getlist("image_id"):
        items.remove_image(item_id, image_id)

    return redirect("/images/" + str(item_id))

@app.route("/edit_item/<int:item_id>")
def edit_item(item_id):
    require_login()
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    all_classes = items.get_all_classes()
    classes = {}
    for my_class in all_classes:
        classes[my_class] = ""
    for entry in items.get_classes(item_id):
        classes[entry["title"]] = entry["value"]

    return render_template("edit_item.html", item=item, classes=classes, all_classes=all_classes)

@app.route("/update_item", methods=["POST"])
def update_item():
    require_login()
    check_csrf()
    item_id = request.form["item_id"]
    title = request.form["title"]
    description = request.form["description"]
    price = request.form["price"]
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)
    if not re.search("^[1-9][0-9]{0,9}$", price):
        abort(403)
    if not title or len(title) > 50:
        abort(403)
    if not description or len(description) > 1000:
        abort(403)

    all_classes = items.get_all_classes()
    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    items.update_item(item_id, title, price, description, classes)
    return redirect("/item/" + str(item_id))

@app.route("/remove_item/<int:item_id>", methods=["GET", "POST"])
def remove_item(item_id):
    require_login()
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_item.html", item=item)

    if request.method == "POST":
        check_csrf()
        if "remove" in request.form:
            items.remove_item(item_id)
            return redirect("/")
        else:
            return redirect("/item/" + str(item_id))

@app.route("/find_item")
def find_item():
    query = request.args.get("query")
    if query:
        found_items = items.find_items(query)
    else:
        query = ""
        found_items = []
    return render_template("find_item.html", query=query, items=found_items)

@app.route("/create_item", methods=["POST"])
def create_item():
    require_login()
    check_csrf()
    title = request.form["title"]
    if not title or len(title) > 50:
        abort(403)
    description = request.form["description"]
    if not description or len(description) > 1000:
        abort(403)
    price = request.form["price"]
    if not re.search("^[1-9][0-9]{0,9}$", price):
        abort(403)
    user_id = session["user_id"]

    all_classes = items.get_all_classes()
    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title,class_value))

    items.add_item(title, description, price, user_id, classes)    
    return redirect("/")

@app.route("/register")
def register():
    if "user_id" in session:
            return redirect("/")
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if not username or not password1 or not password2:
        flash("VIRHE: Tyhjä kenttä", "error")
        return render_template("register.html")

    if password1 != password2:
        flash("VIRHE: salasanat eivät ole samat", "error")
        return render_template("register.html")

    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        flash("VIRHE: tunnus on jo varattu", "error")
        return render_template("register.html")
    flash("Tunnus on luotu", "success")
    return redirect("/login")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        if "user_id" in session:
            return redirect("/")
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user_id = users.check_login(username,password)

        if user_id:        
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        flash("Väärä tunnus tai salasana", "error")    
        return render_template("login.html")

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
        del session["csrf_token"]
    return redirect("/")

