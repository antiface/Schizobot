# A.G. (c) 2017. All Rights Reserved.
# What is History?
# History begins with an Event, an Event Type, a Record of that event, and a Record Type as well as Record ID.

>>> class History:
	def __init__(self,event_name,event_type,record_type,record_id):
		self.event_name = event_name
		self.event_type = event_type
		self.record_type = record_type
		self.record_id = record_id

		
>>> Hx1 = History('Holocaust', 'Tragedy', 'Song', '00000')
>>> Hx1.event_name
'Holocaust'
>>> Hx1.event_type
'Tragedy'
>>> Hx1.record_type
'Song'
>>> Hx1.record_id
'00000'

>>> class History:
	def __init__(self,event_name,event_type,record_type, record,record_id):
		self.event_name = event_name
		self.event_type = event_type
		self.record_type = record_type
		self.record = record
		self.record_id = record_id
		
Hx2 = History('A.G. Birthday', 'Birthday', 'Identity Record', 'It was a rainy October day...', '0.00000')
>>> Hx2.event_name, Hx2.event_type, Hx2.record_type, Hx2.record, Hx2.record_id
('A.G. Birthday', 'Birthday', 'Identity Record', 'It was a rainy October day...', '0.00000')
