from flask import Flask,url_for,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = "chris"
    movies = [
        {"title":"大赢家","year":"2020"},
        {"title":"囧妈","year":"2020"},
        {"title":"战狼","year":"2019"},
        {"title":"叶问2","year":"2016"},
        {"title":"疯狂外星人","year":"2019"}
    ]
    return render_template("index.html",name=name,movies=movies)