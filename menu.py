import simple_colors
from travel import Travel
from music import Music
from food import Food
from animal import Animal
from sports import Sports
from holidays import Holidays

def menu():
	print(simple_colors.red('\n SUBJECTS:', ['bold', 'underlined']))
	print(simple_colors.red('\n  1. Travel'))
	print(simple_colors.red('  2. Music'))
	print(simple_colors.red('  3. Food'))
	print(simple_colors.red('  4. Animal'))
	print(simple_colors.red('  5. Sports'))
	print(simple_colors.red('  6. Holidays'))

	subject = int(input(simple_colors.red('\n CHOOSE A SUBJECT : ')))

	if subject == 1 :
		Travel()
	elif subject == 2 :
		Music()
	elif subject == 3 :
		Food()
	elif subject == 4 :
		Animal()
	elif subject == 5 :
		Sports()
	elif subject == 6 :
		Holidays()
	else :
		print('Your choice is not between subjects! choose again:)')
		menu()
  

