from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def run_notebook():
    try:
        # Execute the Jupyter Notebook
        subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", "NET.ipynb"], check=True)
        return "Notebook executed successfully!"
    except Exception as e:
        return f"Error executing notebook: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
