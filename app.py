from flask import Flask
import subprocess
import threading

app = Flask(__name__)

def run_notebook():
   # subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", "NET.ipynb"], check=True)

@app.route("/")
def home():
    thread = threading.Thread(target=run_notebook)
    thread.start()
    return "Notebook execution started in the background."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

