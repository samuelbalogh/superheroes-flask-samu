import random

import flask

from superheroes import DCSuperHero, Fight

# Create the application.
APP = flask.Flask(__name__)

# list our superheroes here
superman = DCSuperHero(
    "Superman",
    strength=93,
    powers=["x-ray vision", "flying", "super strength"],
    damagemin=3,
    damagemax=8,
)
batman = DCSuperHero(
    "Batman", strength=85, powers=["lots of money"], damagemin=4, damagemax=6
)
catwoman = DCSuperHero(
    "Catwoman", strength=88, powers=["speed", "agility"], damagemin=1, damagemax=8
)
robin = DCSuperHero("Robin", strength=75, powers=["agility"], damagemin=1, damagemax=2)

all_superheroes = [superman, batman, catwoman, robin]


# this is a "dictionary comprehension" - it's a one-liner of building a dictionary from another iterable
superheroes = {hero.name.lower(): hero for hero in all_superheroes}


@APP.route("/")
def index():
    heroes = random.sample(all_superheroes, k=2)

    fight = Fight(*heroes)
    fight.start()

    return flask.render_template("index.html", heroes=heroes)

# this is another form of routing:
# <name> is a variable and can be any superhero name
@APP.route("/<name>")
def superhero(name):
    hero = superheroes.get(name)
    return flask.render_template("hero.html", hero=hero)


if __name__ == "__main__":
    APP.debug = True
    APP.run()
