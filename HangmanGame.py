import random
stages=['''
    ********
           |
        0  |
       /|\ |
       / \ |
           |
    ********
    ''','''
    ********
           |
        0  |
       /|\ |
       /   |
           |
    ********
    ''','''
    ********
           |
        0  |
       /|\ |
           |
           |
    ********''',
    '''
    ********
           |
        0  |
       /|  |
           |
           |
    ********''',
    '''
    ********
           |
        0  |
        |  |
           |
           |
    ********''',
    '''
    ********
           |
        0  |
           |
           |
           |
    ********''',
    '''
    ********
           |
           |
           |
           |
           |
    ********''']
word_list=['apple','banana','pear','mango','grapes','orange','pomegranate','papaya','kiwi','guava','cherry','pineapple','watermelon']
chosen_word=random.choice(word_list)
play_again=1
while(play_again):
    lives=6
    display=[]
    for i in range(len(chosen_word)):
        display+='_'
    print(display)
    game_over=False
    while not game_over:
        guessed_letter=input("Guess a letter:").lower()
        for position in range(len(chosen_word)):
            letter=chosen_word[position]
            if guessed_letter==letter:
                display[position]=guessed_letter
        print(display)
        if guessed_letter not in chosen_word:
            lives-=1
            if lives==0:
                game_over=True
                print("You Lose!")
        if '_' not in display:
            game_over=True
            print("You Win!")  
        print(stages[lives])
    print("If You want to play again enter 1 or else enter 0 :")
    play_again=int(input())