from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        return f"<h1>Hello, {name}!</h1>"
    return '''
        <form method="POST">
            <input type="text" name="name" placeholder="Enter your name">
            <button type="submit">Submit</button>
        </form>
    '''
@app.route("/about")
def about():
    return "This is the About page"


if __name__ == "__main__":
    app.run(debug=True)
