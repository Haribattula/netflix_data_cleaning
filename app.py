from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"  # <-- This line must be indented

@app.route("/about")
def about():
    return "About Page"
