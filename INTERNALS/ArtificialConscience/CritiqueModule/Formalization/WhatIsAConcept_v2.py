### CITATIONS FROM ENGLISH TRANSLATION (1994) OF "WHAT IS PHILOSOPHY?" BY GILLES DELEUZE & FÉLIX GUATTARI (1991).
### Qu'est-ce que la philosophie? (c) 1991 by Les Editions de Minuit. Translation (c) 1994 Columbia University Press. First published by Verso 1994. (c) Verso 1994. All Rights Reserved.
### PYTHON CODE MINUS CONTENT (CITATION, FAIR USE) FROM "WHAT IS PHILOSOPHY?" by A.G. (c) 2016. All Rights Reserved.
### Thought Experiment: Can machine intelligence invent new philosophical concepts autonomously or through some process, maybe even a stochastic process?
### Title: WhatIsAConcept_v2.py
### MOTIVATING QUESTION: WHAT IS THE FUNDAMENTAL DIFFERENCE BETWEEN PYTHON SCRIPTS "WhatIsAConcept_v1.py" and "WhatIsAConcept_v2.py"?
### FIND ALL DIFFERENCES, IDENTIFY MOST FUNDAMENTAL, i.e. AS FAR INTO THE FOUNDATIONS OF EVERYTHING AS YOU CAN GO RELATIVE TO THE FOUNDATIONS OF EVERYTHING SAID BEFORE IN THIS PREFACE TO THE PRESENTATION OF THE CODE (THIS REPOSITORY, MOSTLY THE README.md FILE, AND THESE NOTES).

import random

WhatIsAConcept = ['There are no simple concepts.',
'Every concept has components and is defined by them.',
'It therefore has a combination (chiffre).',
'It is a multiplicity, although not every multiplicity is conceptual.',
'There is no concept with only one component.',
'Every concept is at least double or triple, etc.',
'Neither is there a concept possessing every component, since this would be chaos pure and simple.',
'Every concept has an irregular contour defined by the sum of its components, which is why, from Plato to Bergson, we find the idea of the concept being a matter of articulation, of cutting and cross cutting.',
'The concept is a whole because it totalizes its components, but it is a fragmentary whole.',
'Only on this condition can it escape the mental chaos constantly threatening it, stalking it, trying to reabsord it.',
'All concepts are connected to problems without which they would have no meaning and which can themselves only be isolated and understood as their solution emerges.',
'We are dealing here with a problem concerning the plurality of subjects, their relationship, and their reciprocal presentation.',
'We put to one side the question of the difference between scientific and philosophical problems.',
'However, even in philosophy, concepts are only created as a function of problems which are thought to be badly understood or badly posed (pedagogy of the concept).',
'In short, we say that every concept always has a history, even though this history zigzags, though it passes, if need be, through other problems and onto different planes.',
'In any concept there are usually bits or components that come from other concepts, which corresponded to other problems and presupposed other planes.',
'This is inevitable because each concept carries out a new cutting-out, takes on new contours, and must be reactivated or recut.',
'On the other hand, a concept also has a becoming that involves its relationship with concepts situated on the same plane.',
'Here concepts link up with each other, support one another, coordinate their contours, articulate their respective problems, and belong to the same philosophy, even if they have different histories.',
'In fact, having a finite number of components, every concept will branch off toward other concepts that are differently composed but that constitute other regions of the same plane, answer to problems that can be connected to each other, and participate in a co-creation.',
'A concept requires not only a problem through which it recasts or replaces earlier concepts but a junction of problems where it combines with other coexisting concepts.',
'It is in this way that, on a determinable plane, we go from one concept to another by a kind of bridge.',
'Readers may start from whatever example they like.',
'We believe that they will reach the same conclusion about the nature of the concept or the concept of concept.',
'First, every concept relates back to other concepts, not only in its history but in its becoming or its present connections.',
'Every concept has components that may, in turn, be grasped as concepts... Concepts, therefore, extend to infinity and, being created, are never created from nothing.',
'Second, what is distinctive about the concept is that it renders components inseparable within itself.',
'Components, or what defines the consistency of the concept, its endoconsistency, are distinct, heterogeneous, and yet not separable.',
'The point is that each partially overlaps, has a zone of neighborhood (zone de voisinage), or a threshold of indiscernibility, with another one.',
'These zones, thresholds, or becomings, this inseparability, define the internal consistency of the concept.',
'But the concept also has an exoconsistency with other concepts, when their respective creation implies the construction of a bridge on the same plane.',
'Zones and bridges are the joints of the concept.',
'Third, each concept will therefore be considered as the point of coincidence, condensation, or accumulation of its own components.',
'The conceptual point constantly traverses its components, rising and falling within them.',
'In this sense, each component is an intensive feature, an intensive ordinate (ordonnée intensive), which must be understood not as a general or particular but as a pure and simple singularity - "a" possible world, "a" face, "some" words - that is particularized or generalized depending upon whether it is given variable values or a constant function.',
'But, unlike the position in science, there is neither constant nor variable in the concept, and we no more pick out a variable species for a constant genus than we do a constant species for variable individuals.',
"In the concept there are only ordinate relationships, not relationships of comprehension or extension, and the concept's components are neither constants nor variables but pure and simple variations ordered according to their neighborhood.",
'They are processual, modular.',
'A concept is a heterogenesis - that is to say, an ordering of its components by zones of neighborhood.',
'It is ordinal, an intension present in all the features that make it up.',
'The concept is in a state of survey (survol) in relation to its components, endlessly traversing them according to an order without distance.',
'It is immediately co-present to all its components or variations, at no distance from them, passing back and forth through them: it is a refrain, an opus with its number (chiffre).',
'The concept is an incorporeal, even though it is incarnated or effectuated in bodies.',
'But, in fact, it is not mixed up with the state of affairs in which it is effectuated.',
'It does not have spatiotemporal coordinates, only intensive ordinates.',
'It has no energy, only intensities; it is anenergetic (energy is not intensity but rather the way in which the latter id deployed and nullified in an extensive state of affairs).',
'The concept speaks the event, not the essence or the thing - pure Event, a hecceity, an entity...',
'The concept is defined by the inseparability of a finite number of heterogeneous components traversed by a point of absolute survey at infinite speed.',
'Concepts are "absolute surfaces or volumes," forms whose only object is the inseparability of distinct variations.',
'The "survey" (survol) is the state of the concept or its specific infinity, although the infinities may be larger or smaller according to the number of components, thresholds and bridges.',
'In this sense the concept is act of thought, it is thought operating at infinite (although greater or lesser) speed.',
'The concept is therefore both absolute and relative: it is relative to its own components, to other concepts, to the plane on which it is defined, and to the problems it is supposed to resolve; but it is absolute through the condensation it carries out, the site it occupies on the plane, and the conditions it assigns to the problem.',
'As whole it is absolute, but insofar as it is fragmentary it is relative.',
'It is infinite through its survey or its speed but finite through its movement that traces the contour of its components.',
'Philosophers are always recasting and even changing their concepts: sometimes the development of a point of detail that produces a new condensation, that adds or withdraws components, is enough.',
'The relativity and absoluteness of the concept are like its pedagogy and its ontology, its creation and its self-positing, its ideality and its reality - the concept is real without being actual, ideal without being abstract.',
'The concept is defined by its consistency, its endoconsistency and exoconsistency, but it has no reference: it is self-referential; it posits itself and its object at the same time as it is created.',
'Constructivism unites the relative and the absolute.',
'Concepts, which have only consistency or intensive ordinates outside of any coordinates, freely enter into relationships of nondiscursive resonance - either because the components of one become concepts with other heterogeneous components or because there is no difference of scale between them at any level.',
'Concepts are centers of vibrations, each in itself and every one in relation to all the others.',
'This is why they all resonate rather than cohere or correspond with each other.',
'There is no reason why concepts should cohere.',
'As fragmentary totalities, concepts are not even the pieces of a puzzle, for their irregular contours do not correspond to each other.',
'They do form a wall, but it is a dry-stone wall, and everything holds together only along diverging lines.',
'Even bridges from one concept to another are still junctions, or detours, which do not define any discursive whole.',
'They are movable bridges.',
'From this point of view, philosophy can be seen as being in a perpetual state of digression or digressiveness.',
'Planes must be constructed and problems posed, just as concepts must be created.',
'Philosophers do the best they can, but they have too much work to do to know whether it is the best, or even to bother with this question.',
'Of course, new concepts must relate to our problems, to our history, and, above all, to our becomings.',
'But what does it mean for a concept to be of our time, or of any time?',
'Concepts are not eternal, but does this mean they are temporal?',
'What is the philosophical form of the problems of a particular time?',
'If one concept is "better" than an earlier one, it is because it makes us aware of new variations and unknown resonances, it carries out unforeseen cuttings-out, it brings forth an Event that surveys (survole) us.',
'But we only wanted to show that a concept always has components that can prevent the appearance of another concept or, on the contrary, that can themselves appear only at the cost of the disappearance of other concepts.',
'However, a concept is never valued by reference to what it prevents: it is valued for its incomparable position and its own creation.',
'Suppose a component is added to a concept: the concept will probably break up or undergo a complete change involving, perhaps, another plane - at any rate, other problems.',
'The history of philosophy means that we evaluate not only the historical novelty of the concepts created by a philosopher but also the power of their becoming when they pass into one another.',
'The same pedagogical status of the concept can be found everywhere: a multiplicity, an absolute surface or volume, self-referents, made up of a certain number of inseparable intensive variations according to an order of neighborhood, and traversed by a point in a state of survey. ',
'The concept is the contour, the configuration, the constellation of an event to come.',
'Concepts in this sense belong to philosophy by right, because it is philosophy that creates them and never stops creating them.',
'The concept is obviously knowledge - but knowledge of itself, and what it knows is the pure event, which must not be confused with the state of affairs in which it is embodied.',
'The task of philosophy when it creates concepts, entities, is always to extract an event from things and beings, to set up the new event from things and beings, always to give them a new event: space, time, matter, thought, the possible as events.',
'Every concept shapes and reshapes the event in its own way.',
'The greatness of a philosophy is measured by the nature of the events to which its concepts summon us or that it enables us to release in concepts.',
'So the unique, exclusive bond between concepts and philosophy as a creative discipline must be tested in its finest details.',
'The concept belongs to philosophy and only to philosophy.']

"""
>>> type(WhatIsAConcept)
<type 'list'>
>>> len(WhatIsAConcept)
87
>>> print WhatIsAConcept[random.randint(0,87)]
['We believe that they will reach the same conclusion about the nature of the concept or the concept of concept.']
>>> print WhatIsAConcept[random.randint(0,87)]
['It is infinite through its survey or its speed but finite through its movement that traces the contour of its components.']
>>> print WhatIsAConcept[random.randint(0,87)]
['However, a concept is never valued by reference to what it prevents: it is valued for its incomparable position and its own creation.']
>>> print WhatIsAConcept[random.randint(0,87)]
['Second, what is distinctive about the concept is that it renders components inseparable within itself.']
"""
