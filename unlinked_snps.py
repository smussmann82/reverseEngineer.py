from __future__ import print_function

import collections

class UNSNPS():
	'Class for working with unlinked file'
	

	def __init__(self, infile):
		self.snps_file = infile
		self.content = list()
		self.data = collections.defaultdict(dict)
		self.codes = {
			'A':'AA',
			'C':'CC',
			'T':'TT',
			'G':'GG',
			'M':'AC',
			'R':'AG',
			'W':'AT',
			'S':'CG',
			'Y':'CT',
			'K':'TG',
			'N':'NN',
			'-':'NN'
		}

	def readFile(self):
		with open(self.snps_file) as f:
			self.content = f.readlines()
		self.content = [x.strip() for x in self.content]

	def printf(self):
		for x in self.content:
			print(x)

	def parseFile(self):
		self.content.pop(0) #remove phylip header
		for x in self.content:
			counter=0 #initialize locus counter
			templist = x.split()
			for y in templist[1]:
				counter+=1
				#print(y)
				self.data[counter][templist[0]] = self.codes[y] #add [locus][individual] = [genotype] to dictionary
		print(self.data)
		
