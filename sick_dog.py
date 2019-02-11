class Dog(object):
	"""docstring for Dog"""
	def __init__(self, name):
		self.name = name
		self.sick = False
		self.sickness = ''

	def is_sick(self):
		return self.sick

	def diagnose(self, sickness):
		self.sick = True
		self.sickness = sickness

	def cured(self):
		self.sick = False
		self.sickness = ''

cases = {
	0: 'headache',
	1: 'rabies',
	2: 'worms',
	3: 'vaccination',
	4: 'stomachache',
	5: 'running nose'
}

switcher = {
	0: 'Prescribe Ibuprofen',
	1: 'Refer to the lab for injection',
	2: 'Refer to a chemist in town',
	3: 'Request immunization card',
	4: '',
	5: 'A dog with a running nose? Lol'
}

def diagnose(dog):
	if dog.is_sick():
		return switcher.get(dog.sickness, 'Case not seen before')
	return dog.name + ' is not sick.'


#  TESTS

dog = Dog('Tommy')
print(diagnose(dog))	# dog is feeling well
dog.diagnose(0)
print(diagnose(dog))	# the dog has a headache
dog.cured()
dog.diagnose(5)
print(diagnose(dog))	# random stuff 
