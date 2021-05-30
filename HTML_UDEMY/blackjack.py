import random
from art import logo
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start=input("Do you want to paly blackjack.\nType y to play and n to stop").lower()
if start == 'y':
  end = False
elif start == 'n':
  end = True
  clear()
else:
  print("Invalid input !!!")  

while not end:
  user=[]
  computer=[]
  for i in range(2):
    user.append(random.choice(cards))
    computer.append(random.choice(cards))
  sum1=sum(user)
  sum2=sum(computer)
  print(f"Your cards are {user} which totals : {sum1}\nComputer one card is {computer[random.randint(0,1)]}")
  draw_card = False 
  while not draw_card:
    choice=input("Do you want to draw another card").lower()
    if choice == 'y':
      another_card = random.choice(cards)
      if another_card == 11:
        x=sum1 + another_card
        if x > 21:
          another_card = 1
        else:
          another_card = 11
      user.append(another_card)
      sum1_2 = sum(user)
      sum1 = sum1_2
      print(f"Another card is {another_card} which totals to : {sum1}")
    else:
      draw_card = True
  if sum1 > sum2 and sum1 <= 21 :
    print(f"Computer cards are {computer} which totals to {sum2}")
    print("You win")
  elif sum1 > 21 or sum1 < sum2:
    print(f"Computer cards are {computer} which totals to {sum2}")
    print("You loose")
  start_again=input("Do you want to play again\nType 'y' for yes and 'n' for no").lower()
  if start_again == 'y':
    clear()
  else:
    end = True