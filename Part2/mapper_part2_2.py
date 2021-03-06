#!/usr/bin/python
# Let Hadoop know we want to use Python to execute our file

from itertools import cycle
import csv
import sys
# This module provides access to some variables used or 
# maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
# https://docs.python.org/3/library/sys.html

class mvMapper(object):
# Turn our records into key value pairs
	def __init__(self, infile=sys.stdin, separator=',', beta=0.85):
    # Prepare three arguments, naming the object, what is our input file, and what is our seperator
		self.infile = infile # Rename infile to know what infile we are referencing
		self.separator = separator # Rename seperator to know what objects seperator we are referencing
		self.beta = beta # Beta is a chosen constant to allow for random teleportation
		self.vectorize = dict() # create a dictionary variable that is consistent with our other variable naming
		self.e = 1.0/875713
		#self.vectorize = {1: 9.0/24, 2: 5.0/24, 3: 5.0/24, 4:5.0/24}
		
		
		with open('part-00000') as vector:
	        	for v in vector:
	            		elements = v.split(self.separator)
	            		source = int(elements[0].strip())
	            		value = float(elements[1].strip())
	            		self.vectorize[source] = value
			

	def map(self): # Here we will actually output our Key, Value pair for the Reducer to take in
		reader = csv.reader(self.infile)		
		for row in reader: # Begin looping through the object line by line up to the end of the vector file, which we know is four lines long
			source = int(row[0]) # Set our Source pages to column 0
			dest = int(row[1]) # Set our Destination pages to column 1
			prob = float(row[2]) # Set our probability to column 2. We will need to find a way to create this in part 2.
			if source in self.vectorize:
				self.emit(dest, self.beta * prob * self.vectorize[source] + (1 - self.beta) * self.e) # Output our Key, Value Pair, (Destination Page, Weighted Vector = 1/rows*probability path)

	def emit(self, key, value): # Emmitting Formatting
		sys.stdout.write('{0}{1}{2}\n'.format(key, self.separator, value))

	"""
	def status(self, message): # Basic Troubleshooting we may call later
		sys.stderr.write("reporter:status:{0}\n".format(message))

	def read(self): # Remoce trailing whitespace function
		for line in self.infile:
			yield line.rstrip()
			
	def __iter__(self): # Set Object as the iterator going through line by line through self that doesn't minus trailing white space
		for line in self.read():
			yield line
	"""

if __name__ == '__main__': # Makes sure that all code is executed at the bottom and make sure that script being imported to make sure that the code is completely done before handing it over to Hadoop, this allows for better debugging.
	mvMapper().map()
