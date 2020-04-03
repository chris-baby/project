import os,sys

from flask import Flask,url_for,render_template,request,flash,redirect
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
app.config['SECRET_KEY'] = '1903c_dev'

db = SQLAlchemy(app)

# models 数据层
class user(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))

class movie(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        #获取表单的数据
        title = request.form.get("title")
        year = request.form.get("year")
        if not title or not year or len(year)>4 or len(title)>60:
            flash('输入错误')
            return redirect(url_for('index'))
        #将数据保存到数据库
        movie1 = movie(title=title,year=year)#创建记录
        db.session.add(movie1)
        db.session.commit()
        flash('创建成功')
        return redirect(url_for('index'))

    movies = movie.query.all()
    return render_template("index.html",movies=movies)

#自定义命令
@app.cli.command()
@click.option("--drop",is_flag=True,help="先删除在创建")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化数据库完成")


@app.cli.command()
def forgr():
    name = "chris"
    movies = [
            {"title":"大赢家","year":"2020"},
            {"title":"囧妈","year":"2020"},
            {"title":"战狼","year":"2019"},
            {"title":"叶问2","year":"2016"},
            {"title":"疯狂外星人","year":"2019"}
        ]
    user1 = user(name=name)
    db.session.add(user1)
    for i in movies:
        movie1 =movie(title=i["title"],year=i["year"])
        db.session.add(movie1)
    db.session.commit()
    click.echo("导入数据库完成")

#错误处理函数
@app.errorhandler(404)
def pape_not_found(e):
    return render_template('404.html')


#模板上下文处理函数
@app.context_processor
def comon_user1():
    user1 = user.query.first()
    return dict(user1=user1)