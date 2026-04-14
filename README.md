# Kirpputori

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään sovellukseen ilmoituksia. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään ilmoituksia.
* Käyttäjä näkee sovellukseen lisätyt ilmoitukset. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät ilmoitukset.
* Käyttäjä pystyy etsimään ilmoituksia hakusanalla tai luokittelun perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä ilmoituksia.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä arvosteluja ja käyttäjän lisäämät ilmoitukset.
* Käyttäjä pystyy valitsemaan tietokohteelle yhden tai useamman luokittelun. Mahdolliset luokat ovat valmiiksi tehtyjä.
* Sovelluksessa pystyy lähettämään viestejä käyttäjälle, joka on jättänyt ilmoituksen.

## Sovelluksen asennus

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Tietokannan taulujen ja alkutietojen luonti tapahtuu automaattisesti sovelluksen käynnistyessä

Voit käynnistää sovelluksen näin:

```
$ flask run
```