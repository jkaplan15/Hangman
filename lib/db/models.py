from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Hangman(Base):
    __tablename__ = 'hangmans'

    id = Column(Integer(), primary_key=True)
    letters = Column(String())

    def __repr__(self):
        return f'Hangman #{self.id}: {self.letters}'

