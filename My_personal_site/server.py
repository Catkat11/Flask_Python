from flask import Flask, render_template

app = Flask(__name__)


# Defines a route for the home page "/"
@app.route("/")
def home():
    # Renders the "index.html" template from the "templates" folder
    return render_template("index.html")


# Checks if the file is being run directly rather than imported
if __name__ == "__main__":
    # Runs the application in debug mode
    app.run(debug=True)
