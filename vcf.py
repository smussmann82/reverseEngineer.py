from __future__ import print_function

import collections

class VCF():
	'Class for working with VCF file'
	

	def __init__(self, infile, dictofdicts,out):
		self.vcf_file = infile
		self.outfile = out
		self.content = list()
		self.dictofdicts = dictofdicts
		self.loci = collections.defaultdict(list)

	def readFile(self):
		with open(self.vcf_file) as f:
			self.content = f.readlines()
		self.content = [x.strip() for x in self.content]

	def printf(self):
		for x in self.content:
			print(x)

	def writeHeader(self):
		fn = open(self.outfile, 'w')
		for i in range(0,12):
			fn.write(self.content[i])
			fn.write("\n")
		fn.close()

	def parseFile(self):
		self.writeHeader()
		del self.content[:11] # remove most header lines
		header = self.content.pop(0).split() # retrieve line with individual names

		for x in self.content:
			templist = x.split()
			self.loci[int(templist[0])].append(x)

		index = 1 #index counter for the unlinked_snps data

		od = collections.OrderedDict(sorted(self.loci.items()))
		for k,dk in od.iteritems():
			snpcounter = 0 #index counter for the snps at each locus
			locusdata = collections.defaultdict(dict)
			for snp in dk:
				temp = snp.split() #split line for this locus
				locusdict = self.makeLocusDict(temp[3],temp[4]) #create dictionary specific to locus
				for i in range(9, len(temp)):
					
					templocus = list() #initialize new list for this locus
					alleles = list()
					if(temp[i] == './.'):
						alleles = temp[i].split("/")
					else:
						alleles = temp[i].split("|") #split locus 

					for allele in alleles:
						templocus.append(locusdict[allele])#translate each allele to base
					loc = ''.join(sorted(templocus))
					if(loc == "GT"):
						loc = "TG"

					locusdata[snpcounter][header[i]] = loc

				snpcounter+=1

			if(self.compareDicts(locusdata,index,dk)) == True:
				index+=1
				

	def compareDicts(self,dict1,index,snps):
		for k, dk in dict1.iteritems():
			if(dk == self.dictofdicts[index]):
				fn = open(self.outfile, 'a')
				fn.write(snps[k])
				fn.write("\n")
				fn.close()
				return True
		return False

	def makeLocusDict(self,ref,alt):
		locusdict = dict()
		locusdict['.'] = "N"
		locusdict['0'] = ref
		counter = 1
		for a in alt.split(","):
			locusdict[str(counter)] = a
			counter+=1

		return locusdict
