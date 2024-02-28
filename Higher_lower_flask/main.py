from flask import Flask
import random

# Generate a random number between 0 and 9
random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return "<h1> Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

# Route for guessing the number
@app.route("/<int:guess_number>")
def guess(guess_number):
    if guess_number > random_number:
        return "<h1 style='color: blue'>Too high! Try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif guess_number < random_number:
        return "<h1 style='color: red'>Too low! Try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color:green'>You win!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
