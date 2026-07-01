import random
from pickle import GLOBAL
from random import randint

from flask import Flask
app = Flask(__name__)

RANDOM_NUMBER = randint(0,9)
COLOR_LIST = ["red", "blue", "green", "purple", "orange", "#FF5733", "#33FF57"]


@app.route("/")
def home_page():
    return """
        <h1>Guess a number between 0 and 9</h1>
        <img src = "/static/random.gif">
        """

@app.route("/<int:number>")
def guess(number):
    global RANDOM_NUMBER
    if number == RANDOM_NUMBER:
        RANDOM_NUMBER = randint(0, 9)
        return f"""
        <h1 style="color:{random.choice(COLOR_LIST)}">CORRECT GUESS!!</h1>
        <img src = "/static/{number}.gif">
        """
    elif number<RANDOM_NUMBER:
        return f"""
        <h1 style="color:{random.choice(COLOR_LIST)}">Try Again, Higher</h1>
        <img src = "/static/{number}.gif">
        """
    else:
        return f"""
                <h1 style="color:{random.choice(COLOR_LIST)}">Try Again, Lower</h1>
                <img src = "/static/{number}.gif">
                """

if __name__=="__main__":
    app.run(debug=True)

