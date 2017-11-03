#! /usr/bin/perl

use warnings;
use strict;
use Getopt::Std;
use Data::Dumper;

# kill program and print help if no command line arguments were given
if( scalar( @ARGV ) == 0 ){
  &help;
  die "Exiting program because no command line options were used.\n\n";
}

# take command line arguments
my %opts;
getopts( 'hl:o:r:', \%opts );

# if -h flag is used, or if no command line arguments were specified, kill program and print help
if( $opts{h} ){
  &help;
  die "Exiting program because help flag was used.\n\n";
}

# parse the command line
my( $loci, $out, $remove ) = &parsecom( \%opts );

# declare variables
my @lociLines;
my @removeLines;

&filetoarray( $loci, \@lociLines );
&filetoarray( $remove, \@removeLines );

exit;

#####################################################################################################
############################################ Subroutines ############################################
#####################################################################################################

# subroutine to print help
sub help{
  
  print "\nmatchLoci.pl is a perl script developed by Steven Michael Mussmann\n\n";
  print "To report bugs send an email to mussmann\@email.uark.edu\n";
  print "When submitting bugs please include all input files, options used for the program, and all error messages that were printed to the screen\n\n";
  print "Program Options:\n";
  print "\t\t[ -h | -l | -o | -r ]\n\n";
  print "\t-h:\tDisplay this help message.\n";
  print "\t\tThe program will die after the help message is displayed.\n\n";
  print "\t-l:\tSpecify your pyRAD .loci file (required).\n\n";
  print "\t-o:\tSpecify the output file name (optional).\n";
  print "\t\tIf no name is provided, the file extension \".unlinked_snps.loci\" will be appended to the input file name.\n\n";
  print "\t-r:\tUse this flag to specify the list of loci to be removed (required).\n";
  print "\t\tThe number of each locus to be removed should be listed on its own line.\n\n";
  
}

#####################################################################################################
# subroutine to parse the command line options

sub parsecom{ 
  
	my( $params ) =  @_;
	my %opts = %$params;
  
	# set default values for command line arguments
	my $loci = $opts{l} || die "No input file specified.\n\n"; #used to specify input file name.  This is the input .loci file produced by pyRAD
	my $out = $opts{o} || $loci; #used to specify output file name.  If no name is provided, the file extension ".unlinked_snps.loci" will be ultimately be appended to the input file name.

	my $remove = $opts{r} || die "List of loci to be removed not specified.\n\n"; #used to specify the list of loci to be removed

	return( $loci, $out, $remove );

}

#####################################################################################################
# subroutine to put file into an array

sub filetoarray{

  my( $infile, $array ) = @_;

  
  # open the input file
  open( FILE, $infile ) or die "Can't open $infile: $!\n\n";

  # loop through input file, pushing lines onto array
  while( my $line = <FILE> ){
    chomp( $line );
    next if($line =~ /^\s*$/);
    #print $line, "\n";
    push( @$array, $line );
  }

  #foreach my $thing( @$array ){
  #	print $thing, "\n";
  #}

  # close input file
  close FILE;

}

#####################################################################################################
