import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["physics", "chemistry", "mathematics", "biology"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display=[]
for i in range(word_length):
    display+='_'
end_game = False
remaining_lives=6
while remaining_lives > 0 and not end_game:
    guess=input("guess the letter").lower()
    for i in range(word_length):
        if chosen_word[i]==guess:
            display[i]=guess
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        remaining_lives-=1
        print(stages[remaining_lives])
    if remaining_lives > 0 and '_' not in display:
        end_game = True
        print("You Won !!!")
    elif remaining_lives == 0 :
        end_game=True
        print("You Lose !!!")

