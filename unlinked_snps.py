from __future__ import print_function

class UNSNPS():
	'Class for working with unlinked file'
	

	def __init__(self, infile):
		self.snps_file = infile
		self.content = list()

	def readFile(self):
		with open(self.snps_file) as f:
			self.content = f.readlines()
		self.content = [x.strip() for x in self.content]

	def printf(self):
		for x in self.content:
			print(x)
