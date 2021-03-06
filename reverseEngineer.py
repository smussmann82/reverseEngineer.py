#!/usr/bin/env python

from comline import ComLine
from vcf import VCF
from unlinked_snps import UNSNPS

import sys

def main():
	input = ComLine(sys.argv[1:])
	snps_file = UNSNPS(input.args.usnps)
	out = input.args.usnps + ".vcf"
	vcf_file = VCF(input.args.vcf,snps_file.data,out)
	vcf_file.readFile()
	snps_file.readFile()
	snps_file.parseFile()
	vcf_file.parseFile()

main()

raise SystemExit
