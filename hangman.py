# ///////////////////////////////////////////////////////////
# Hangman Game (written in Python 3)
# By Marcus Harjani
# ///////////////////////////////////////////////////////////
# Ensure words.txt and hangman.py are in the same directory
# Change directory to that with the files
# Run 'python hangman.py'
# Enjoy!
# //////////////////////////////////////////////////////////


# The variable 'begingame' and 'beginround' are assigned a '0' or '1'.
# This number determines whether to start a game and rounds within that game.
begingame = 0
beginround = 0
win = 0
loss = 0

# Gallows is an array, an index wil be printed and then added to with each incorrect guess.
gallows = [""" 
   _____
   |   |
       |
       |
       |
       |
    -----
""", """ 
   _____
   |   |
   O   |
       |
       |
       |
    -----
""", """ 
   _____
   |   |
   O   |
   |   |
       |
       |
    -----
""", """ 
   _____
   |   |
   O   |
  /|   |
       |
       |
    -----
""", """ 
   _____
   |   |
   O   |
  /|\  |
       |
       |
    -----
""", """ 
   _____
   |   |
   O   |
 _/|\  |
       |
       |
    -----
""", """ 
   _____
   |   |
   O   |
 _/|\_ |
       |
       |
    -----
""", """ 
   _____
   |   |
   O   |
 _/|\_ |
  /    |
       |
    -----
""", """ 
   _____
   |   |
   O   |
 _/|\_ |
  / \  |
       |
    -----
""", """ 
   _____
   |   |
   O   |
 _/|\_ |
 _/ \  |
       |
    -----
""", """ 
   _____
   |   |
   O   |
 _/|\_ |
 _/ \_ |
       |
    -----
"""]

# Welcome prompt.
welcomeprompt = input("""
======================
='Welcome to Hangman!= 
=============================================
='Select \'r\' for RULES or \'b\' to BEGIN: =
=============================================
""")

if welcomeprompt == str('r'):
	print("""
-------------------------------------------------------------------
-For each round of the game a random word will be chosen.----------
-You have 10 attempts to guess a letter that might be in the word.-
-For every wrong guess, a body part goes on the gallows.-----------
--------------------------------------------------------Good Luck!-
-------------------------------------------------------------------""")
	rulesprompt = input('Press \'b\' to BEGIN or \'q\' to QUIT:  ')
	if rulesprompt == str('b'):
		begingame = begingame + 1
	elif rulesprompt == str('q'):
		raise SystemExit
	else:
		input('Please select \'b\' or \'q\':   ')
elif welcomeprompt == str('b'):
	begingame = begingame + 1
else:
	input('Please select \'b\' or \'q\':   ')

# Stats and new rounds.
while begingame == 1:
	if beginround == 0: 
		print('\n' '\n' 'Current Stats: ''\n' 'Wins: ' + str(win) + '\n' 'Losses: ' + str(loss))
		roundstatus = input('Press \'n\' to begin a NEW ROUND or \'q\' to QUIT:   ')
		if roundstatus == str('n'):
			beginround = beginround + 1
		elif roundstatus == str('q'):
			raise SystemExit
		else:
			input('Please select \'n\' or \'q\':   ')

# Each new round has a new word and 10 guesses.
	if beginround == 1:
# Import random module and open words.txt as object 'file'.
# Define variable 'words' as a list of lines in words.txt (file has one word per line).
# Define variable 'hiddenword' as 'words' randomly selected from, IE a randomly chosen word.
# Define variable 'blankword' as an array which is then assigned string '- ' once for each item in the length of 'hiddenword'.
# Rationale: It's not known to the player what word is chosen,
# or what the possible words might be without opening words.txt.
		import random
		with open("words.txt") as file:
				words = file.read().split()
				hiddenword = random.choice(words)
		blankword = []
		for letter in range(len(hiddenword)):
			blankword.append('- ')
# Define 'pastguess' as an empty array each guess will be added to and then printed to display prior attempts.
# Define variable 'place' at 0. The rationale is to use 'place' as the current index to print of the gallows,
# As the player guesses, 'place' is added to by 1 so that the next gallows image is printed starting from [place] (or [0]).
		pastguess = []
		place = 0
# Function analyze() brings in variables and arrays defined above and then analyzes each player guess.
# Variable 'wordcompare' creates an array of 'hiddenword' with each letter as an item in the array.
# Variable 'space' is defined as string '- ' and will be used when analyzing the player guess against each letter in 'hiddenword'.
# Function works by:
# First, printing the blank hidden word (joined 'blankword'),
# Second, passing player's guess into variable 'playerguess',
# Third, adding 'playerguess' to the array of past guesses,
# Fourth, verifying 'playerguess' is not a number or more than one letter,
# Fifth, if 'playerguess' is not contained in the array of 'hiddenword' lettters then 1 is added to 'place',
# Sixth, if 'playerguess' is in the array of 'hiddenword' letters then replace '- ' with player guess at the index
# of a correct guess, or replace with '- ' if it is an incorrect guess.
		def analyze():
			global blankword
			global gallows
			global place
			global pastguess
			wordcompare = list(hiddenword)
			space = '- '
			print('\n' + ''.join(blankword))
			playerguess = input('\n' '\n' 'Please guess a letter: ')
			pastguess.append(playerguess)
			if len(playerguess) > 1 or playerguess.isnumeric():
				print('\n' '\n''Guess one letter!')
			elif playerguess not in wordcompare:
				place += 1
				return place
			else:
				for (i, item) in enumerate(wordcompare):
					if item == playerguess:
						blankword[i] = playerguess
					elif playerguess not in wordcompare:
						blankword[i] = space
# While 'place' (index of 'gallows') is less than 10 the player continues to guess by invoking the analyze() function.
# With each run through 1 is subtracted from remaining guesses and the current state of 'blankword', 'gallows', and 'pastguess' is printed.
		print(gallows[0])
		while place < 10:
			analyze()
			print('\n' '\n' + ''.join(blankword) + '\n' '\n' 'Gallows: ' + gallows[place] + '\n' + 'Guessed Letters: ' + ''.join(pastguess))
# Also, whether the game has been won or lost.
# A game is won if the joined 'blankword' (being replaced with guesses) matches the 'hiddenword'.
# If won, 1 is added to 'win' variable and 1 substracted from 'beginround' which returns to the main screen.
# If gallows is full ('place' at 10) then player loses, 1 is addedd to variable 'loss' and 1 substracted from 'beginround' which returns to the main screen.
			if ''.join(blankword) == hiddenword:
				print("""
				   YOU WON!
				  __________
				  |         |
				  _\       /_
				 |(|      | )|
				  \|      |/
				    \    /
				      \ /
				      | |
				     =====""")
				win = win + 1
				beginround = beginround - 1
				break
			elif place == 10:
				print("""
					YOU LOSE!
					 
					   wWWwWwwwwww
					  /    '   '     
					{@   ( .)  (.)
					 |        b !
					            .
					   |_  ~~~  .
					       ___/
					            :
					            _______
					            """ + 'The secret word is \'' + str(hiddenword) + '\'')
				loss = loss + 1
				beginround = beginround - 1
				break




