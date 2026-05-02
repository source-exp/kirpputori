# Pylint raportti
Pylint antaa seuraavan raportin sovelluksesta:
```txt
************* Module app
app.py:45:73: C0303: Trailing whitespace (trailing-whitespace)
app.py:63:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:77:55: C0303: Trailing whitespace (trailing-whitespace)
app.py:78:54: C0303: Trailing whitespace (trailing-whitespace)
app.py:272:44: C0303: Trailing whitespace (trailing-whitespace)
app.py:273:76: C0303: Trailing whitespace (trailing-whitespace)
app.py:274:77: C0303: Trailing whitespace (trailing-whitespace)
app.py:304:63: C0303: Trailing whitespace (trailing-whitespace)
app.py:305:41: C0303: Trailing whitespace (trailing-whitespace)
app.py:311:0: W0311: Bad indentation. Found 12 spaces, expected 8 (bad-indentation)
app.py:346:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:349:19: C0303: Trailing whitespace (trailing-whitespace)
app.py:354:51: C0303: Trailing whitespace (trailing-whitespace)
app.py:364:0: C0305: Trailing newlines (trailing-newlines)
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:34:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:49:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:55:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:67:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:82:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:96:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:102:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:111:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:120:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:131:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:161:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:178:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:198:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:234:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:248:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:234:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:255:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:278:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:309:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:315:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:337:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:337:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:358:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:3:0: C0411: standard import "sqlite3" should be placed before third party imports "flask.Flask", "flask.abort" (wrong-import-order)
app.py:7:0: C0411: standard import "re" should be placed before third party imports "flask.Flask", "flask.abort" and first party imports "config", "db", "items"  (wrong-import-order)
app.py:10:0: C0411: standard import "secrets" should be placed before third party imports "flask.Flask", "flask.abort" and first party imports "config", "db", "items", "users", "messages"  (wrong-import-order)
app.py:2:0: W0611: Unused url_for imported from flask (unused-import)
************* Module config
config.py:1:0: C0304: Final newline missing (missing-final-newline)
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:22:33: C0303: Trailing whitespace (trailing-whitespace)
db.py:33:27: C0303: Trailing whitespace (trailing-whitespace)
db.py:34:0: C0303: Trailing whitespace (trailing-whitespace)
db.py:39:0: C0304: Final newline missing (missing-final-newline)
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:11:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
db.py:13:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
db.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:25:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:35:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module items
items.py:59:29: C0303: Trailing whitespace (trailing-whitespace)
items.py:95:29: C0303: Trailing whitespace (trailing-whitespace)
items.py:117:0: C0303: Trailing whitespace (trailing-whitespace)
items.py:123:0: C0304: Final newline missing (missing-final-newline)
items.py:1:0: C0114: Missing module docstring (missing-module-docstring)
items.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:38:8: R1704: Redefining argument with the local name 'title' (redefined-argument-from-local)
items.py:41:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:58:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:69:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:80:8: R1704: Redefining argument with the local name 'title' (redefined-argument-from-local)
items.py:83:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:94:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module messages
messages.py:4:42: C0303: Trailing whitespace (trailing-whitespace)
messages.py:4:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
messages.py:15:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
messages.py:18:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
messages.py:26:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
messages.py:27:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
messages.py:28:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
messages.py:31:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
messages.py:32:0: C0304: Final newline missing (missing-final-newline)
messages.py:32:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
messages.py:1:0: C0114: Missing module docstring (missing-module-docstring)
messages.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
messages.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
messages.py:17:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
messages.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module seed
seed.py:14:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
seed.py:17:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
seed.py:18:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
seed.py:20:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
seed.py:21:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
seed.py:22:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
seed.py:24:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
seed.py:25:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
seed.py:26:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
seed.py:27:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
seed.py:28:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
seed.py:29:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
seed.py:30:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
seed.py:31:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
seed.py:32:0: C0303: Trailing whitespace (trailing-whitespace)
seed.py:33:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
seed.py:34:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
seed.py:35:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
seed.py:36:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
seed.py:37:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
seed.py:38:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
seed.py:39:0: W0311: Bad indentation. Found 4 spaces, expected 16 (bad-indentation)
seed.py:40:0: W0311: Bad indentation. Found 4 spaces, expected 16 (bad-indentation)
seed.py:41:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
seed.py:42:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
seed.py:45:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
seed.py:46:0: C0304: Final newline missing (missing-final-newline)
seed.py:46:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
seed.py:1:0: C0114: Missing module docstring (missing-module-docstring)
seed.py:9:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:10:0: C0103: Constant name "item_per_user" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:11:0: C0103: Constant name "messages_per_user" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
seed.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:5:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:6:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:7:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:10:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:20:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:23:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:24:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:25:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:28:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:29:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:30:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:31:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
users.py:32:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:33:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:34:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:36:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:37:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
users.py:38:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
users.py:39:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
users.py:44:0: C0304: Final newline missing (missing-final-newline)
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:27:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:36:1: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
users.py:41:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:2:0: C0411: third party import "werkzeug.security.check_password_hash" should be placed before first party import "db"  (wrong-import-order)
users.py:1:0: R0801: Similar lines in 2 files
==items:[45:51]
==users:[9:15]
	sql = """SELECT items.id,
                    items.title,
                    items.description,
                    items.price,
                    users.id user_id,
                    users.username (duplicate-code)

-----------------------------------
Your code has been rated at 6.55/10
```
Käydään läpi sisältö ja korjataan tarvittavat osat.

## Missing docstring
Ilmoitus:
```txt
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
```
Mikä tarkoittaa, että koodissa ei ole kommenteja, koska sovelluksen kehityksessä on tehty tietoisesti päätös, ettei käytetä docstring-kommentteja.

## Bad indentation ja Trailing whitespace
```txt
users.py:10:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
```
Näitä ilmoituksia oli eniten, koska en lähtökohtaisesti merkkinyt Sublime Text:issä tarvittavat asetukset tabeille. Jälkikäteet oli helppo korjata.

## Constant name
Raportissa ilmoitukset olivat:
```txt
seed.py:9:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
```
Ideana on että kaikki päämuuttujat merkitään isoilla kirjamilla. Tämän ohjelman kontekstissä päämuuttujat isoilla kirjamilla eivät sovi.

## Dangerous default value [] as argument
Tämä ilmoitus:
```txt
db.py:25:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```
Viittaa koodin osaan:
```python
def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()
```
Koska parametrin oletusarvo on lista, ongelmana olisi voinut olla tyhjä listaolio on jaettu kaikkien funktion kutsujen kesken, mutta koodi ei muuta listaoliota.

## Redefining argument with the local name 'title'
```txt
items.py:38:8: R1704: Redefining argument with the local name 'title' (redefined-argument-from-local)
```
Tämä ilmoitus viittaa koodin:
```python
def add_item(title, description, price, user_id, classes):
    sql = """INSERT INTO items (title, description, price, user_id)
             VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, description, price, user_id])
    item_id = db.last_insert_id()
    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?,?,?)"
    for title, value in classes:
        db.execute(sql,[item_id, title, value])
```
Jossa muuttujalla ja funktion paremetrilla oli sama nimi.
## Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
Ilmoitus vittaa:
```txt
app.py:234:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```
Jossa sijaitsee taulun poistamisen funktio, jolloin jos ehdot eivät täydy ei pylintin kannalta taphdu mitään, mutta koska ehdot ovat joko `GET tai `POST` niin aina jokin heistä täyttyy.
## Similar lines in 2 files
```txt
users.py:1:0: R0801: Similar lines in 2 files
==items:[45:51]
==users:[9:15]
    sql = """SELECT items.id,
                    items.title,
                    items.description,
                    items.price,
                    users.id user_id,
                    users.username (duplicate-code)
```
Kaksi eri funktiota, jotka heti hakevat tarvittavat tiedot, mutta käyttävät eri inputtia, jolloin ensimmäinen etsii user_id perustella ja toinen item_id, tällöin on käytetty enemmän tietokannan osat kuin pythonia.

## Unnecessary "else" after "return"
Ylimääräiset else returnin kohdilla, jolloin funktio olisi silti lopettanut toimintaa ja palauttanut arvoa:
```txt
app.py:248:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
```

### Korjausten jälkeen:
```txt
------------------------------------------------------------------
Your code has been rated at 8.23/10
```
