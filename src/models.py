import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250)) 
    email = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
   
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    type = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    author_id = Column(String, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    comment_content = Column(String(50))
    post = relationship('Post')
    user = relationship('User')

class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id")) 
    post = relationship("post")

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class Following(Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e