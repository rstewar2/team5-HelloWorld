#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/python
# Let Hadoop know we want to use Python to execute our file

import sys # Lets us use infile iterations
from itertools import groupby # Allows us to use groupby
from operator import itemgetter # The itemgetter operator simply specifies by which value of each tuple being yielded that should be grouped on

class mvReducer(object): # After Shuffling and Sorting, reduce key value pairs
	def __init__(self, infile=sys.stdin, separator=','): # Prepare three arguments, naming the object, what is our input file, and what is our seperator
		self.infile = infile
		self.separator = separator

	def reducer(self):
		for dest, values in self: # iterate through the Key, Value pair through the object
			self.emit(dest, sum(float(prob[1]) for prob in values))  # emit the key with value. Value = sum of column 1 of the inputted group defined by __iter__

	def emit(self, key, value): # formatting emmiter settings
		sys.stdout.write('{0}{1}{2}\n'.format(key, self.separator, value))

	def read(self): # Again making sure we don't have trailing whitespace
		for line in self.infile:
			yield line.rstrip()

	def __iter__(self): # Iterate through by groups of groupby(key),  straight from bengfort
		generator = (line.split(self.separator, 1) for line in self.read()) 
		for item in groupby(generator, itemgetter(0)):
			yield item

if __name__ == '__main__':
	mvReducer().reducer()