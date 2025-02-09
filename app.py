import os
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

# Load cleaned Netflix data
df = pd.read_csv("netflix_titles.csv")  # Update with your cleaned file

@app.route("/")
def home():
    return df.head().to_html()  # Display first 5 rows as an HTML table

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
