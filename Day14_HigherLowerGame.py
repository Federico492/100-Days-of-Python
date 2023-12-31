from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"
  
def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    if guess == "a":
      return True
    else:
      return False 
  else:
    if guess == "b":
      return True
    else:
      return False

print(logo)
score = 0
continue_game = True
account_b = random.choice(data)

while continue_game:
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Compare B: {format_data(account_b)}.")
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  clear()
  print(logo)
  
  if is_correct:
    score += 1
    print(f"You are right! Current score: {score}")
  else:
    continue_game = False
    print(f"Wrong! Score: {score}")
