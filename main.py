import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template('About.html')  # Replace with `render_template("about.html")` if you create one


@app.route("/contact")
def contact():
    return render_template('Contact.html')


@app.route("/startup")
def startup():
    return render_template('Startup.html')

@app.route("/team")
def team():
    return render_template('Team.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # fallback to 5000 locally
    app.run(host="0.0.0.0", port=port, debug=True)
