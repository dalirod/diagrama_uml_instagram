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
    name=Column(String(200),nullable=False)
    email=Column(String(200),nullable=False,unique=True)
    password=Column(String(10),nullable=False)
    age=Column(Integer)
    date_of_birth=Column(Integer)
    planets= relationship('Planets')



class Planets(Base):
    __tablename__='planets'
    id=Column(Integer,primary_key=True)
    name=Column(String(4),nullable=False)
    population=Column(Integer)
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship('user')

 
class Favorites(Base):
    __tablename__='favorites'   
    id=Column(Integer,primary_key=True)
    name=Column(String(100),nullable=False)  
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship('user')


class Characterest(Base):
    __tablename__='characterest'   
    id=Column(Integer,primary_key=True)
    name=Column(String(100),nullable=False)
    occupation=Column(String(100))
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship('user')


class Villain(Base):
    __tablename__='villain'   
    id=Column(Integer,primary_key=True)
    name=Column(String(100),nullable=False)
    characterest_id= Column(Integer,ForeignKey('characterest.id'))
    characterest= relationship('characterest')
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
