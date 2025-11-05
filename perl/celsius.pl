# celsius.pl

use strict; use warnings;

while (1) {
	print "What temperature to convert (e.g. 37C or 98.6F): ";
	my $temp1 = <STDIN>;
	chomp $temp1;
	my $scale1 = substr($temp1, -1, 1);
	chop $temp1;
	
	my $temp2;
	my $scale2;
	if ($scale1 eq 'F') {
		$temp2 = ($temp1 -32) * 5 / 9;
		$scale2 = 'C';
	}
	else {
		$temp2 = $temp1 * 9 / 5 + 32;
		$scale2 = 'F';
	}
	
	print "$temp1$scale1 is $temp2$scale2\n";
}