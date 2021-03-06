from flask import Flask,render_template,request ,redirect
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
    #SELECT * FROM posts ORDER BY id DESC;
    posts=Post.query.order_by(Post.id.desc()).all()
    #SELECT * FROM posts;
    #asc <->desc
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
    
@app.route("/posts/<int:post_id>/comment", methods=["POST"])
def comment(post_id):
    #1. 시용자가 보낸 댓글 내용 가져오기
    content = request.form.get('content')
    comment =Comment(content=content)
    
    #2. 해당하는 댓글이 어디 게시물이랑 관계가 있는지!!
    #2-1. 해당 게시물 가져오기
    post =Post.query.get(post_id)
    #2-2 해당 게시물에 댓글 오브젝트 넣기
    post.comments.append(comment)
    #2-3 댓글저장하기
    db.session.add(comment)
    db.session.commit()
    return redirect("/posts/{}".format(post_id))
    
    
    
    
# @app.route("/comment", methods=["POST"])
# def comment():
#     post_id = request.form.get('post_id')
#     content = request.form.get('content')
#     #DB에 저장
#     comment=Comment(content=content ,post_id = post_id )#이 post 자체가 ORM이다 
#     db.session.add(comment)
#     #insert into posts (title, content)
#     #values ('1번글', '1번내용');
#     db.session.commit()
#     return render_template("create.html", comment=comment)
    
@app.route("/posts/<int:id>")
def read(id):
    #DB에서 특정한 게시글(id)을 가져와 !
    post = Post.query.get(id) # Post 클래스의 메소드라고 생각하는게 편하다
    #SELECT * FROM posts WHERE id = 1;
    return render_template("read.html",post=post )
    
@app.route("/posts/<int:id>/delete")
def delete(id):
    #DB에서 특정한 게시글(id)을 가져와 !
    post = Post.query.get(id) # Post 클래스의 메소드라고 생각하는게 편하다
    #SELECT * FROM posts WHERE id = 1;
    db.session.delete(post)
    db.session.commit()
    #DELETE FROM posts WHERE id=2
    return redirect('/')
    #return render_template('index.html') 이거랑 다른 이유는 이렇게하면 그저 index.html을 형태를 호출 할 뿐 url의 주소는 /posts/<int:id>/delete

    #return render_template("delete.html", post=post ) /이렇게 하면 ure

@app.route("/posts/<int:id>/edit")
def edit(id):
    post = Post.query.get(id) # Post 클래스의 메소드라고 생각하는게 편하다
    #SELECT * FROM posts WHERE id = 1;
    return render_template("edit.html",post=post )
   
@app.route("/posts/<int:id>/update" , methods=["POST"])
def update(id):
    #DB에서 특정한 게시글(id)을 가져와 !
    post = Post.query.get(id) # Post 클래스의 메소드라고 생각하는게 편하다
    #SELECT * FROM posts WHERE id = 1;
    post.title = request.form.get('title')
    post.content = request.form.get('content')
    db.session.commit()
    #UPDATAE posts SET title = "hihi"
    #WHERE id = 2;
    return redirect("/posts/{}".format(post.id))
   
   
#Post.query.filter_by(title="1").first(
#SELECT COUNT(*) FROM posts
#WHERE title = '1';    
   
#Post.query.filter_by(title="1").all()
#SELECT * FROM posts
#WHERE title = '1';



#Post.query.filter_by(title="1").first()
#SELECT * FROM posts
#WHERE title = '1';

#Post.query.filter(Post.title != "1").all()
#SELECT * FROM posts
#WHERE title != '1';

#Post.query.filter(Post.title.like("%1%")).all()
#SELECT * FROM posts;
#WHERE title LIKE '%1%';

#from sqlarchemy import and_ , or_
#Post.query.filter(and_(Post.title=='1' , Post.comtemt == '1')
#SELECT * FROM posts
#WHERE title ="1" AND content = "1"