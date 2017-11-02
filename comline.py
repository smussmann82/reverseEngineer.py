from __future__ import print_function

import argparse
import os.path

class ComLine():
	'Class for implementing command line options'
	

	def __init__(self, args):
		parser = argparse.ArgumentParser()
		parser._action_groups.pop()
		required = parser.add_argument_group('required arguments')
		optional = parser.add_argument_group('optional arguments')
		required.add_argument("-v", "--vcf",
							dest='vcf',
							required=True,
							help="Specify a vcf file for input."
		)
		required.add_argument("-u", "--usnps",
							dest='usnps',
							required=True,
							help="Specify unlinked SNPs input."
		)
		
		self.args = parser.parse_args()

		#check if files exist
		self.exists( self.args.vcf )

	def exists(self, filename):
		if( os.path.isfile(filename) != True ):
			print(filename, "does not exist")
			print("Exiting program...")
			print("")
			raise SystemExit
