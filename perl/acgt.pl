# acgt.pl

use strict; use warnings;

my $r = rand();
if    ($r < 0.3) {
	print "A\n";
}
elsif ($r < 0.5) {
	print "C\n";
}
elsif ($r < 0.7) {
	print "G\n";
}
else {
	print "T\n";
}
