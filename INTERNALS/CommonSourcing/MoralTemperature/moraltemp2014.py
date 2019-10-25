import time
import os
import json

os.chdir('C:\\Refcards')

def mentalstatus():
	x = {'time': time.strftime('%Y%m%d%H%M'), 'context': raw_input("What is happening?: "),
	'emotion': raw_input("How does it make you feel?: "), 'difficulty': raw_input("What is most difficult in that?: "),
	'past experience': raw_input("Have you experienced such things before? "),
	'resources': raw_input("What resources did you use?: ")}
	with open('mentalstatus_2014.txt', 'a') as outfile:
		json.dump(x, outfile)
		outfile.write(','+'\n')

def moraltempcard():
	x = {"time": time.strftime('%Y%m%d%H%M'), "context": raw_input("What is the context?: "),
	'emotions': {'Mental Energy': input('Mental Energy: '), 'Stress': input('Stress: '),
	'Anxiety': input('Anxiety: '), 'Anger': input('Anger: '), 'Fear': input('Fear: '),
	'Joy': input('Joy: '), 'Depression': input('Depression: '), 'Optimism': input('Optimism: '),
	'Morale': input('Morale: '), 'Motivation': input('Motivation: '), 'Enthusiasm': input('Enthusiasm: ')}}
	with open('moraltemperature.txt', 'a') as outfile:
		json.dump(x, outfile)
		outfile.write(','+'\n')
		
def writeNote(x):
	with open(x, 'w') as outfile:
		outfile.write('Time: '+time.asctime())
		outfile.write('\n')
		outfile.write('\n')
		outfile.write('Context: '+raw_input('Context: '))
		outfile.write('\n')
		outfile.write('\n')
		outfile.write('Qualia: '+raw_input('Qualia: '))
		outfile.write('\n')
		outfile.write('\n')
		outfile.write('Note: '+raw_input('Write note: '))
		
def note():
	t = time.strftime('%Y%m%d%H%M')
	writeNote(t+'.txt')
	
lstGoals = []
statRep = {}
def statusReport2():
	statRep = {'statusReport':{'date': time.asctime(), 'context': raw_input("What is the current Context?: "), 'mood': input("Rate mood from 1 to 10: "), 'projects': raw_input("What are the current Projects?: "), 'projectRating': input("Rate progress of Projects in general from 1 to 10: ")}}
	def setGoals():
		lstGoals.append(raw_input("List a concrete goal: "))
		lstGoals.append(raw_input("List a second concrete goal: "))
		lstGoals.append(raw_input("List a third: "))
		return lstGoals
	def addGoals(statRep):
		x = setGoals()
		statRep.update({'goals': x})
	addGoals(statRep)
	with open('statRep_2014.txt', 'a') as outfile:
		json.dump(statRep, outfile)
		outfile.write(','+'\n')

def triplecolumn():
	x = {'time': time.strftime('%Y%m%d%H%M'), 'automatic': raw_input("Automatic thoughts: "),
	'hotness': raw_input("Hotness?: "), 'response': raw_input("Rational response?: ")}
	with open('triplecolumn_2014.txt', 'a') as outfile:
		json.dump(x, outfile)
		outfile.write(','+'\n')
	
def needs():
	x = {'time': time.strftime('%Y%m%d%H%M'), 'needs': [raw_input("Name 3 current needs. 1): "), raw_input("2): "), raw_input("3): ")]}
	with open('needs_2014.txt', 'a') as outfile:
		json.dump(x, outfile)
		outfile.write(','+'\n')

def values():
	x = {'time': time.strftime('%Y%m%d%H%M'), 'values': [raw_input("Name 3 current values. 1): "), raw_input("2): "), raw_input("3): ")]}
	with open('values_2014.txt', 'a') as outfile:
		json.dump(x, outfile)
		outfile.write(','+'\n')

def thoughts():
	x = {'time': time.strftime('%Y%m%d%H%M'), 'thoughts': raw_input("Write down a thought: "), 'tags': raw_input("Write tags, separated by comma: ")}
	with open('thoughts_2014.txt', 'a') as outfile:
		json.dump(x, outfile)
		outfile.write(','+'\n')

def refCard():
	x = {"time": time.asctime(), "context": raw_input("What is the context?: "),
	"temp": input("What is the moral temperature?: ")}
	with open('moraltempcard_2014.txt', 'a') as outfile:
		json.dump(x, outfile)
		outfile.write(','+'\n')

def datetime():
	return {'time': time.strftime('%Y%m%d%H%M')}
	
def context():
	return {'context': raw_input("What is the current context?: ")}
	
def mood():
	return {'mood': input("Rate mood from 1 to 10: ")}
	
def projects():
	return {'projects': raw_input("What are your current Projects?: "),
	'projectRating': input("Rate progress of Projects in general from 1 to 10: ")}
	
def goals():
	return {'goals': (raw_input("List a concrete goal: "),
		raw_input("List a second concrete goal: "),
		raw_input("List a third: "))}

def statusReport():
	with open('status_2014.txt', 'a') as outfile:
		json.dump((datetime(), context(), mood(), projects(), goals()), outfile)
		outfile.write(','+'\n')

listfuncs = dir()

listdir = os.listdir(os.getcwd())

"""
f = open('mentalstatus_2014.txt', 'r')
>>> f.readline()

"""
