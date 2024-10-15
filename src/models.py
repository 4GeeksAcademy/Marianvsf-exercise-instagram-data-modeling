import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    firtsname = Column(String(50), nullable=False)
    lastname = Column(String(50))
    email = Column(String(150), unique=True, nullable=False)

class Post(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    caption = Column(String(3800))
    image = Column(String(250)) #Url de la imagen del post
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(1200))
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    Post = relationship(Post)
    User = relationship(User)
    

class Follow(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('users.id'), primary_key=False)
    user_to_id = Column(Integer, ForeignKey('users.id'), primary_key=False)


class MediaType(enum.Enum):
    red = 1
    green = 2
    blue = 3

class Media(Base):
    __tablename__ = 'medias'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaType), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'))
    user = relationship(User)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
