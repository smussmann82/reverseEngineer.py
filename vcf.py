from __future__ import print_function

import collections

class VCF():
	'Class for working with VCF file'
	

	def __init__(self, infile):
		self.vcf_file = infile
		self.content = list()
		self.loci = collections.defaultdict(list)
		#self.data = collections.defaultdict(dict)

	def readFile(self):
		with open(self.vcf_file) as f:
			self.content = f.readlines()
		self.content = [x.strip() for x in self.content]

	def printf(self):
		for x in self.content:
			print(x)

	def parseFile(self):
		del self.content[:11] # remove most header lines
		header = self.content.pop(0) # retrieve line with individual names
		print(header)

		for x in self.content:
			templist = x.split()
			self.loci[int(templist[0])].append(x)

		#print(self.loci)
		od = collections.OrderedDict(sorted(self.loci.items()))
		for k,dk in od.iteritems():
			print(k)
			for snp in dk:
				print(snp)
				temp = snp.split() #split line for this locus
				locusdict = self.makeLocusDict(temp[3],temp[4]) #create dictionary specific to locus
				print(locusdict)
				

	def makeLocusDict(self,ref,alt):
		locusdict = dict()
		locusdict['0'] = ref
		counter = 1
		for a in alt.split(","):
			locusdict[str(counter)] = a
			counter+=1

		return locusdict
