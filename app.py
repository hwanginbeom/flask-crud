from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= 'postgresql:///app' # 설정해놓은 데이터 베이스명 | ubuntu=# create database app with template=template0 encoding='utf8' ;
app.config["SQLALCHEMY_TRACK_MODIFICATION"]= False
db.init_app(app) # 여기서 쓰는 디비가 app 이라는 db라는 것을 명시 
migrate = Migrate(app,db) # flask에서 디비를 쉽게 쓰게 하기 위해 쓰는 것 

@app.route("/")
def index():
    posts=Post.query.all()
    #SELECT * FROM posts;
    return render_template("index.html", posts=posts)
    
@app.route("/posts/new")
def new():
    return render_template("new.html")

@app.route("/post", methods=["POST"])
def create():
    #if request.method("POST") 이런건 보통 합쳐 놓은거 
    #사용자로 부터 값을 가져와서 (form데이터를 받을 때는 form으로)
    title = request.form.get('title')
    content = request.form.get('content')
    #DB에 저장
    post=Post(title=title , content=content)#이 post 자체가 ORM이다 
    db.session.add(post)
    #insert into posts (title, content)
    #values ('1번글', '1번내용');
    db.session.commit()
    return render_template("create.html", post=post)