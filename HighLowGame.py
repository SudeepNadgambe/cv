from art import logo,vs
from game_data import data
import random
from replit import clear


def versus():
  print(vs)
score = 0
end = False
dict1=data[random.randint(1,50)]
dict2=data[random.randint(1,50)]
while not end:
  print(logo)
  print(f"Compare A : {dict1['name']}, {dict1['description']}, from {dict1['country']}")
  versus()
  print(f"Against B : {dict2['name']}, {dict2['description']}, from {dict2['country']}")
  if score > 0:
    print("Your answer is right")
    print(f"Current score:{score}")
  answer = input("Who has more Followers\nType 'A' or 'B':").title()
  if dict1['follower_count'] > dict2['follower_count']:
    correct_answer = 'A'
  else:
    correct_answer = 'B'
  if answer == correct_answer:
    score+=1
    temp = dict2
    dict1 = temp
    dict2 = data[random.randint(1,50)]
    clear()
  else :
    print("Wrong Answer")
    end = True



