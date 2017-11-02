from __future__ import print_function

class VCF():
	'Class for working with VCF file'
	

	def __init__(self, infile):
		self.vcf_file = infile
		self.content = list()

	def readFile(self):
		with open(self.vcf_file) as f:
			self.content = f.readlines()
		self.content = [x.strip() for x in self.content]

	def printf(self):
		for x in self.content:
			print(x)
