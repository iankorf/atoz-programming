# beat_box.pl

use strict; use warnings;
use Time::HiRes;

my $target = 4;
while (1) {
	print "Get ready to hit the enter key exactly {target} seconds apart!\n";
	print "Press enter when ready...\n";
	<STDIN>;
	print "Press the enter key after exactly $target seconds! ";
	my $t0 = Time::HiRes::time();
	<STDIN>;
	my $t1 = Time::HiRes::time();
	my $elapsed = $t1 - $t0;
	my $off = abs($target - $elapsed);
	printf "Your time %.2f was off by %.2f percent.\n",
		$elapsed, 100 * $off / $target;
}

