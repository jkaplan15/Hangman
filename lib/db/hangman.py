from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Player    
import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word, session, player):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please enter a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():    
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
        player.wins += 1
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
        player.losses += 1

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      🤠
                   |    👋👔👋
                   |      👖
                   |     👟👟
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      🤠
                   |    👋👔👋
                   |      👖
                   |     👟
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      🤠
                   |    👋👔👋
                   |      👖
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      🤠
                   |    👋👔
                   |      👖
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      🤠
                   |      👔
                   |      👖
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      🤠
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]



def main(session, player):
    word = get_word()
    play(word, session, player)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word, session, player)

if __name__ == "__main__": 
    engine = create_engine('sqlite:///hangman.db')
    Session = sessionmaker(bind=engine)
    session = Session()


    player_name = input("Enter your name: ")
    # print(player_name)

    player = session.query(Player).filter(Player.username == player_name).first()
    if not player:
        player = Player(username = player_name, wins = 0, losses = 0)
        session.add(player)
    main(session, player)

    session.commit()




