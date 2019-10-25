# DATETIME: (date at top)

# PROJECT: (name of the given Project that this Note falls into)

# CONCEPTS/THEMES: (Concepts and Themes related to this Note)

# NOTES:  (Notes on the Status of said Project, etc.)


import os
import time
 
os.chdir('/home/diane/Refcards')
 
def writeNote(x):
	with open(x, 'w') as outfile:
		outfile.write('TIME: '+time.asctime())
		outfile.write('\n')
		outfile.write('\n')
		outfile.write('PROJECT: '+raw_input('Project: '))
		outfile.write('\n')
		outfile.write('\n')
		outfile.write('CONCEPTS/THEMES: '+raw_input('Concepts/Themes: '))
		outfile.write('\n')
		outfile.write('\n')
		outfile.write('NOTES: '+raw_input('Notes: '))
		
def note():
	t = time.strftime('%Y%m%d%H%M')
	writeNote(t+'.txt')
