from flask import Flask 

app=Flask(__name__)


@app.route("/")
def liked():
    return("liked_movies")

@app.route("/")
def disliked():
    return("disliked_movies")


app.run()