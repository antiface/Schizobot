# First Concept of History. A.G. (c) 2017. All Rights Reserved.
# struct FirstConcept {
#    char title[50];
#    int concept_id;
#  }; concept;
# PROBLEM: WHAT IS THE TYPE OF TYPE "FIRST CONCEPT"?

#########################

>>> class Concept:
	def __init__(self, name, id):
		self.name = name
		self.id = id
		
>>> x = Concept('Concept', '0.0')
>>> x
<__main__.Concept instance at 0x0000000002E885C8>
>>> x.name
'Concept'
>>> x.id
'0.0'

#########################

>>> def GiveConcept():
	return WhatIsAConcept[random.randint(0,87)]

>>> GiveConcept()
['It is infinite through its survey or its speed but finite through its movement that traces the contour of its components.']
>>> FirstConcept = Concept(GiveConcept(), '0.00000')
>>> FirstConcept
<__main__.Concept instance at 0x0000000002E8E488>
>>> dir(FirstConcept)
['__doc__', '__init__', '__module__', 'id', 'name']
>>> FirstConcept.name
['Philosophers do the best they can, but they have too much work to do to know whether it is the best, or even to bother with this question.']
>>> FirstConcept.id
'0.00000'

#########################
