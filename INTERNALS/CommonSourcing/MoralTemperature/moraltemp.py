import time
 
def f(): return time.asctime()
def g(): return raw_input('Context: ')
def h(): return raw_input('Qualia: ')
def i(): return [f(), g(), h()]
 
"""
>>> x = i()
Context: Sitting at home.
Qualia: Happy, snappy, chappy.
>>> x
['Thu Jun 26 08:09:37 2014', 'Sitting at home.', 'Happy, snappy, chappy.']
"""
