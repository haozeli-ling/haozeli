from flask import Flask, render_template

app = Flask(__name__)

# Define the home route
@app.route("/")
def home():
    return render_template("index.html")

# Define an about page route
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("teaching.html")

@app.route("/misc")
def misc():
    return render_template("misc.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

