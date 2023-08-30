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
end_game= False
word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)

lives=6

print(f'pssst The random word is {chosen_word}')
display = []
word_length=(len(chosen_word))
for _ in range (word_length):
  display += "_"
while not end_game:
    guss=input("guess a letter :").lower()

    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guss:
            display[position]=letter
        
    if guss not in chosen_word:
        lives -=1
        if lives==0:
            end_game=True
            print("you lose the man hanged")



    print(display)
    if "_" not in display:
        end_game=True
        print("you win")   

    print(stages[lives])
