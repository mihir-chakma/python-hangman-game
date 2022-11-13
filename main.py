import random 

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# words bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar'
       'coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk'
       'lion lizard llama mole monkey moose mouse mule newt otter owl panda'
       'parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep'
       'skunk sloth snake spider stork swan tiger toad trout turkey turtle'
       'weasel whale wolf wombat zebra').split()

random_choice = random.choice(words)

blank = ['_' for i in range(len(random_choice))]
print(' '.join(blank))

end_game = False
lifes = 6 

stages = stages[::-1]

while not end_game:
    user_choice = input('\nEnter your choice : ')

    if user_choice in blank:
        print(f'\nYou already guessed {user_choice}')

    for i in range(len(random_choice)):
        if user_choice in random_choice[i]:
            blank[i] = user_choice

    print(f'\n{" ".join(blank)}\n')

    if user_choice not in random_choice:
        lifes = lifes - 1
        if lifes == 0:
            print('You lose.')
            print(f'Word is : {random_choice}')
            end_game = True
    
    print(stages[lifes])

    if '_' not in blank:
        end_game = True
        print('You win.')
