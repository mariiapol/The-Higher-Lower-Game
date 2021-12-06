import random
from flask import Flask

n = random.randint(0, 9)

app = Flask(__name__)

@app.route('/')
def game():
    return '<h1> Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width =450>'

#guess
@app.route("/<int:number>")
def f(number):
    if number > n:
        return '<h1 style="color: red"> Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width =450>'
    elif number < n:
        return '<h1 style="color: red"> Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width =450>'
    else:
        return '<h1 style="color: green"> You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width =450>'

if __name__ == "__main__":
    app.run()
