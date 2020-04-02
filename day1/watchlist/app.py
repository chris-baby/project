import os,sys

from flask import Flask,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
import click

WIN = sys.platform.startswith('win')
if WIN:
    prefix = "sqlite:///"
else:
    prefix = "sqlite:////"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# models 数据层
class user(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))

class movie(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

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

#自定义命令
@app.cli.command()
@click.option("--drop",is_flag=True,help="先删除在创建")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化数据库完成")
