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
def hello():
    return "Hello World!"
    

