'''
This program is EX2 from the Introduction to programming assignment 2
Hangman game
Ben Higgs 03-12-2014
'''

from random import randint

def initgame(word,lives): #initialises the game and creates dict
    curguess=['*']*len(word)
    
    word=word.upper()
    hangman={'Word':word,'Curguess':curguess,'Lives':lives}
    return hangman

def wordguessed(hangman): #checks if words match returns bool
    curg=''
    check=False
    for i in range(len(hangman['Curguess'])): curg+=hangman['Curguess'][i]
    if hangman['Word']==curg: check=True
    return check

def checklives(hangman): #checks the remaining lives avail to user
    lives=hangman['Lives']
    return lives

def getword(hangman): #gets the word from the dict
    secretword=hangman['Word']
    return secretword

def printstatus(hangman): #print the game status
    curg=''
    for i in range(len(hangman['Curguess'])): curg+=hangman['Curguess'][i]
    checkstr='\nWORD: {0}; you have {1} lives left'.format(curg,hangman['Lives'])
    return checkstr

def updategame(hangman,guess): #updates the game and checks guessed letter and increments count and lives available
    guess=guess.upper()
    c=0
    for i in range(len(hangman['Curguess'])):
        if guess==hangman['Word'][i]:
            c+=1
            if guess not in hangman['Curguess']:
                hangman['Curguess'][i]=guess
    if c==0:
        hangman['Lives']-=1
    return hangman,c


def playgame(word,lives): #main function, uses above funtions to play a game of hangman by using the string and lives given, outputs all error messages and stuff
    hangman=initgame(word,lives)
    
    while checklives(hangman)>0 and not wordguessed(hangman):
        print(printstatus(hangman))
        
        check=False
        while check==False:
            letter=str(input('Guess a letter: '))
            if len(letter)>1:
                print('Must be a single letter. guess again, this did not count as a guess')
            else:
                letter=letter.upper()
                check=True
                
        hangman,occ=updategame(hangman,letter)
        if occ>0:
            print('There were {} occurences of the letter {}'.format(occ,letter))
        else: print('There were no occurences of the letter {} in the word. You lost a life'.format(letter))

    if wordguessed(hangman)==True:
        print('Well done – you have guessed the word correctly')
        print('The word was {}'.format(getword(hangman)))
    elif checklives(hangman)==0:
        print('You have no lives left – you have been hung!')
        print('The word was {}'.format(getword(hangman)))
        
            

#main loop of the program.
#takes file and loads lines into a list to be used and randomly referenced and then removed to ensure no word is used twice
#asks if user wants to repeat the game and keep playing, if not loop is exited.
#user inputs difficulty and file path or name. all inputs are checked and errors are given if not correct.
repeat=False
while repeat==False:
    print('''
Welcome to the Hangman game.
Please select a difficulty to play the game with and supply an appropriate text file to load words from.
    ''')
    Filename = input("Specify input text file: ")
    if Filename[-4:]!='.txt':
        Filename=Filename+'.txt'
    try :
        filein = open(Filename)
    except IOError as e :
        filein = None
        print("Failed to open", Filename, "- program aborted")
        break

    difcheck=False
    while difcheck==False:
        difficulty=int(input('''
Please pick a difficulty choice:
1 - Easy    10 lives allocated
2 - Medium   7 lives allocated
3 - Hard     5 lives allocated

Please make your choice: '''))
        if difficulty in (1,2,3):
            if difficulty==1:difficulty=10
            elif difficulty==2: difficulty=7
            elif difficulty==3:difficulty=5
            difcheck=True            
        else: print(' Please make a valid choice from the list, it will be shown again for reference')        
    if filein != None:
        listofwords=[]
        for line in filein:
            line=line.replace('\n', '').replace('\r', '')
            listofwords.append(line)
        while listofwords!=[]:
            if len(listofwords)>1:
                ranpos=randint(0,len(listofwords)-1)
                word=listofwords[ranpos]
                listofwords.remove(word)


                playgame(word,difficulty)
                rep=str(input('Would you like to play again? Y/N'))
                if rep in ('N','n'):
                    repeat=True
                    break
                if rep in ('Y','y'):
                    repeat=False
                else: print(' Please input a single character for yes or no, e.g. Y/N or y/n')    
            else: playgame(listofwords[0],difficulty);repeat=True;break
            

    

