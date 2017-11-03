#!/bin/bash

if [ $# -eq 0 ]
then
	echo "This script will find all monomorphic loci in the .loci file from pyRAD"
	echo "Usage: getMonomorphic.sh <FILE>"
	exit 1
fi

grep "//" $1 | grep -v [*-] | sed 's/[\/| ]//g' > ${1}.remove_loci.txt

exit
