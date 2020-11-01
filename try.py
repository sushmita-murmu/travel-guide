from flask import Flask

app=Flask(__name__)
@app.route("/Hie")
def test():
    return "welcome"

if __name__== "__main__":
    app.run()

