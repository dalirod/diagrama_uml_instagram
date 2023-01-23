import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    username=Column(String(50))
    name=Column(String(200),nullable=False)
    email=Column(String(200),nullable=False,unique=True)
    password=Column(String(10),nullable=False)
    comment= relationship('comment')
    post= relationship('post')
    reels=relationship('reels')
    
class Comment(Base):
    __tablename__='comment'
    id=Column(Integer,primary_key=True)
    comments_text=Column(String)
    user_id=Column(Integer,ForeignKey('user.id'))
    likes=relationship('likes')
    post_id= Column(Integer,ForeignKey('post.id'))
   
 
class Post(Base):
    __tablename__='post'   
    id=Column(Integer,primary_key=True)
    comment_text=Column(String)
    user_id=Column(Integer,ForeignKey('user.id'))
    likes=relationship('likes')
    comment=relationship('comment')
  

class Reels(Base):
    __tablename__='reels'   
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('user.id'))
    likes=relationship('likes')
 

class Likes(Base):
    __tablename__='likes'   
    id=Column(Integer,primary_key=True)
    comment_id=Column(Integer,ForeignKey('comment.id'))
    post_id=Column(Integer,ForeignKey('post'))
    reels_id=Column(Integer,ForeignKey('reels'))
  
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
