from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    wins = Column(Integer())
    losses = Column(Integer())

    # def __repr__(self):
    #     return f'Hangman #{self.id}: {self.username}'

