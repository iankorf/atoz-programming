A to Z Programming
==================

This is a collection of 26 programming problems that will help you improve your
programming skill. If you love biology, rejoice, because many of the problems
have a molecular biology theme. Some problems require data files, which you
will find in the `data` directory. Solutions and learning materials are
provided in the various language directories.

- [administrator](#administrator)
- [beat_box](#beat_box)
- [celsius](#celsius)
- [dna_tm](#dna_tm)
- [enquire](#enquire)
- [fizzprime](#fizzprime)
- [gregory_leibniz](#gregory_leibniz)
- [h...](#h...)
- [information](#information)
- [jaccard_index](#jaccard_index)
- [kullback_leibler](#kullback_leibler)
-

## administrator ##

Write a program that helps you make decisions. Each time you run it, the
program responds with "yes", "no", or "yes, but...". The probabilities of each
are up to you, but here are some suggested values.

- 50% yes
- 40% no
- 10% yes, but...

## beat_box ##

Write a game where the player must try to hit the enter/return button exactly 4
seconds apart. The game should loop endlessly (hitting ^C or ^D will terminate
the while loop). Players may find it helpful to perform an 8-count in their
heads while imagining a song at 120 bpm.

## celsius ##

Write a program that converts from Celsius to Farenheit and vice-versa. The
input should be in the form of "37C or "98.6F". If the input is "37C" the
output should be "98.6F".

## dna_tm ##

Write a program that allows users to compute the melting temperature (Tm) of an
oligonucleotide by typing or copy-pasting sequence. The program should quit if
the input is empty and report an error if the sequence contains letters other
than A, C, G, or T. There are 2 formulas for Tm, which depend on the length of
the sequence. Your code must define a function `tm()` that takes a sequence as
an argument and returns the Tm. Here are the 2 equations:

- 13 nt or less: 2*A + 2*T + C*4 + G*4
- 14 nt or more: 64.9 + 41 * (C + G -16.4) / (A + C + G + T)

## enquire ##

Write a program where computer tries to guess a number you have in mind. The
bounds are from 1 to 1000. The program should repeatedly ask: "is the number
greater than X?", where X varies with each question. The program should always
succeed within 10 questions.

## fizzprime ##

One of the classic programming interview questions is FizzBuzz.

- Write the numbers from 1 to 100
- If the number is evenly divisible by 3, print "Fizz" instead
- If the number is evenly divisible by 5, print "Buzz" instead
- If the number is evenly divisible by 3 and 5, print "FizzBuzz"

In this program, you must follow the same rules as FizzBuzz with one added
complexity: if the number is prime, follow the number with an asterisk. Your
program must define a function `is_prime()` that takes a number as input and
returns a Boolean.

## gregory_leibniz ##

Write a program that esimates Pi (3.1415...) using 3 different methods.

1. Gregory-Leibniz series
2. Nilakantha series
3. Simulation of throwing random darts

The Gregory-Leibniz series is a simple way to estimate Pi. It alternates adding
and subtracting numbers, eventually converging to Pi/4. Use a `for` loop that
terminates after some number of iterations (e.g. 1000).

Pi/4 = 1/1 - 1/3 + 1/5 - 1/7 + 1/9 ...

-----

The Nilakantha series converges faster and is only slightly more complex to
calculate. Terminate this loop when the estimate of Pi is within 1e-6 of the
actual value (you must pretend you don't know the value of Pi).

Pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) ...

-----

A particularly poor (but fun) way to calculate Pi is to simulate throwing darts
with random x, y values in the range from 0 to 1 (e.g. a dart might land at
x=0.35, y=0.84). The ratio of darts that lie inside the circle y = x**2
compared to the total darts eventually converges to Pi/4. It's up to you how
you want to terminate this one.

-----

https://en.wikipedia.org/wiki/Pi

## h... ##

## information ##

Write a program that calculates the entropy of a frequency distribution whose
values are given on the command line. Here is an example command line.

```
python3 information.py 0.4 0.3 0.2 0.1
```

- The values from the command line must be converted to a list of floats
- The list must sum very close to 1.0 or produce an error message
- The program must define a function `entropy()` that takes a list argument
- The program must return the result in log2


## jaccard_index ##

Given 2 files, each containing a list of animal names, determine the Jaccard
Index between the two. The Jaccard Index is defined as the intersection divided
by the union. For this problem, you must use lists (no sets or dictionaries).

https://en.wikipedia.org/wiki/Jaccard_index

## kullback_leibler ##

Given a color in the form of RGB values, (e.g. 255, 254, 7), determine the
official HTML color name that it is the closest to (255, 255, 0 is yellow). Use
Kullback-Leibler divergence to determine the similarity of colors. You will
have to convert values in the byte scale (0-255) to probabilities.

Kullback-Leibler (DKL) is but one of many ways to compare histograms. Others
include Taxicab (DTC) distance or Euclidean distance (D2). Try solving this
problem with DKL as well as DTC and D2. Which do you think works best?

https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence
https://en.wikipedia.org/wiki/Taxicab_geometry
https://en.wikipedia.org/wiki/Euclidean_distance

## l... ##

## m... ##

## n50? ##

## orf ##

## paradox? parser? ##

## quality values? ##

## rloop_finder ##

## shannon_filter ##

## translate ##

## u... ##

## v... ##

## weight_matrix ##

## x... ##

## y... ##

## z... ##

