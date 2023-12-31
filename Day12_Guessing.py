from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high!")
    return turns - 1
  elif guess < answer:
    print("Too low!")
    return turns - 1
  else:
    print(f"You won, you got the right number! The number was {answer}")

def set_difficulty():
  level = input("Set the difficult, 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print("Welcome to the guessing game!")
  print("I'm thinking of a number from 1 to 100")
  answer = randint(1,100)
  print(answer)
  
  turns = set_difficulty()
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a Guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You lose!")
      return
    elif guess != answer:
      print("Guess again!")
game()
