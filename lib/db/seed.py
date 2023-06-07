from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Hangman

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///hangman.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    hangman1 = Hangman(letters="a")
    hangman2 = Hangman(letters="b")
    hangman3 = Hangman(letters="c")

    session.add_all([hangman1, hangman2, hangman3])
    session.commit()

    print("all done seeding")