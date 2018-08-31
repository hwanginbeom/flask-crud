import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = "posts"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String)
    content=db.Column(db.Text)
    created_at=db.Column(db.DateTime)
    update_at = db.Column(db.DateTime)
    comments =db.relationship("Comment", backref='post')
    #댓글들은 복수라 s 이고               여기서 post가 단수인것은 게시글자체는 한개 이기 때문이다.
    # 관계를 가지고있다라는 뜻 
    
    def __init__(self,title,content):
        self.title = title
        self.content = content
        self.created_at=datetime.datetime.now()
        
# CREATE TABLE posts(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR ,
#     content TEXT,
#     created_at DATETIME
#     )

class Comment(db.Model):
    __tablename__ = "Comments"
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String)
    created_at=db.Column(db.DateTime)
    
    #Fk
    post_id=db.Column(db.Integer, db.ForeignKey('posts.id'),nullable=False)

    def __init__(self,content):
        self.content = content
        self.created_at=datetime.datetime.now()
