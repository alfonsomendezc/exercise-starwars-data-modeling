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
    name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    email_address = Column(String(60), nullable=False)
    address = Column(String(250))
    phone_number = Column(String(30), nullable=False)
    creation_date = Column(String(65), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    location = Column(String(250), nullable=False)
    galaxy = Column(String(250), nullable=False)
    weight = Column(Integer, nullable=False)
    fauna = Column(String(250), nullable=False)
    race = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    group = Column(String(30), nullable=False)
    race = Column(String(60), nullable=False)
    job = Column(String(60), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("character.id"), nullable=False)
    user = relationship(User)
    planet = relationship(Planet)
    character = relationship(Character)

def to_dict(self):
    return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')