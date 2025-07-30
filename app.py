from flask import Flask, render_template, request,redirect, url_for


app = Flask(__name__)
submitted_name= []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        submitted_name.append(name)
        return redirect (url_for("names"))
        return f"<h1>Hello, {name}!</h1>"
    
    return '''
        <form method="POST">
            <input type="text" name="name" placeholder="Enter your name">
            <button type="submit">Submit</button>
        </form>
    '''
@app.route("/names")
def names():
    return render_template("names.html", names=submitted_name)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
