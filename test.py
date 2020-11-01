from flask import Flask,render_template

app=Flask(__name__)
@app.route("/jj")
def test():
    return "welcome"

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/gallery")
def gall():
    return render_template("gallery.html")

@app.route("/explore")
def expl():
    return render_template("explore.html")



if __name__== "__main__":
    app.run()

