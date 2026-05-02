# Kirpputori

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään sovellukseen ilmoituksia. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään ilmoituksia.
* Käyttäjä näkee sovellukseen lisätyt ilmoitukset. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät ilmoitukset.
* Käyttäjä pystyy etsimään ilmoituksia hakusanalla tai luokittelun perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä ilmoituksia.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät käyttäjän lisäämät ilmoitukset.
* Käyttäjä pystyy valitsemaan tietokohteelle yhden tai useamman luokittelun. Mahdolliset luokat ovat valmiiksi tehtyjä.
* Sovelluksessa pystyy lähettämään viestejä käyttäjälle, joka on jättänyt ilmoituksen.

## Sovelluksen asennus

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Tietokannan taulujen ja alkutietojen luonti tapahtuu automaattisesti sovelluksen käynnistyessä tai voi manuaalisesti luoda tietokannan taulut ja lisätä alkutiedot:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```

## Sovelluksen testatus suurella tietomäärällä
`seed.py` tiedostolla voi kokeila miten ohjelma käyttäytyy suurien tietomäärien kanssa. Kaikki tarvittavat kirjastot ovat valmiiksi asennettuna `Sovelluksen asennus` kohdalta.
Koodi valmiiksi luo:
* 100 käyttäjää
* 25 ilmoitusta jokaiselle käyttäjälle
* 25 viestiä satunaisille käyttäjälle
Jokaisen käyttäjän salasanaksi on asetettu "0"
Luodaan tietokanta seuraavalla komenolla:
```
$ python3 seed.py
```

### Tulokset
Tietokannan luomisen jälkeen nopeus eri sivuilla on seuraava:

* `/`: `3 ms`
* `/?page=4`: `6 ms`
* `/user/98`: `20 ms` (satunnainen käyttäjä, jolla on 25 ilmoitusta)
* `/find_item?query=&classes=&classes=`: `5 ms`






