import random

def load_words():														
    inFile = open("words.txt", 'r')
    line = inFile.readline()
    wordlist = line.split()
    return wordlist

def read_tries ():														
	try:
		i = int(input ("How many attempts do you want to have: "))
	except ValueError:
		print ("Enter number from 1 to 100")
		i = read_tries ()
	if (i<1) | (i>100):
		print ("Enter number from 1 to 100")
		i = read_tries ()
	return i

def read_cont (): 														
	ans = input ()
	if ans == "+":
		return True
	elif ans == "-":
		return False
	else:
		print ("Enter + if you want to restart or - if you'd like exit")
		return(read_cont())
		
def read_letter ():
	letter = input ("Enter your letter: ")
	if (len(letter) == 1) & (((ord(letter[0])>64) & (ord(letter[0])<91)) | ((ord(letter[0])>96) & (ord(letter[0])<123))):
		return letter.lower()
	else:
		print ("Enter one letter of latin alphabet")
		return(read_letter())

def letter_check(word, letter):  										
	letter_pos = []
	for i in range(len(word)):
		if word[i] == letter:
			letter_pos.append(i)
	return letter_pos

def word_choose (wordlist):												
	return random.choice(wordlist)
	
def solve_form(solve_old, letter_pos, word):							
	solve_new = ""
	j = 0
	for i in letter_pos:
		while j != i:
			solve_new += solve_old[j]
			j += 1
		solve_new += word[j]
		j += 1
	while j < (len(word)):
		solve_new += solve_old[j]
		j += 1
	return solve_new
	

def game_cycle (word):													
	tries = read_tries()
	old_letters = []
	solve = str("*" * len(word))
	print ("Сomputer chose word " + solve)
	res = 1
	while (res == 1):
		if (old_letters != []):
			print ("You've entered: " + str(old_letters))
		print ()
		letter = read_letter()
		if (letter not in old_letters):
			old_letters.append(letter)
			letter_pos = letter_check (word, letter)
			if letter_pos != []:
				solve = solve_form(solve, letter_pos, word)
				print ("You guessed! " + solve)
			else:
				if (tries == 1):
					res = 0
				else:
					tries -= 1
					print ("You guessed wrong. " + str(tries) + " attempts remain")
			if (solve.find("*") == -1):
				res = 2
		else:
			print ("You have already entered this letter")
	if res == 0:
		print ("You lost. The word was " + word)
	if res == 2:
		print ("Congratulations! You won!")
		
def main ():                 											
	cycle_flag = True
	wordlist = load_words()
	while cycle_flag:
		game_cycle(word_choose(wordlist))
		print ("Would you like to restart? (+/-)")
		cycle_flag = read_cont()
		print ("-------------------------------------")

if __name__ == "__main__":
	main() 																	
