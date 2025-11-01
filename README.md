A to Z Programming
==================

This is a collection of 26 programming problems that will improve your
programming skill. For pedagogical reasons, many of these programs have a
molecular biology theme and there is an assumption you are working in a
Unix/Linux environment. Some problems require data files, which you will find
in the `data` directory. Language-specific solutions and learning materials are
provided in the various language directories.

- [acgt](#acgt)
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

## acgt ##

Write a program that randomly prints out a single letter of DNA. Like most
eukarytotic genomes, you are more likely to see an A or T than C or G.

-----

This program introduces:

- Conditional statement (if...)
- Random number generator
- Program output (print...)

## beat_box ##

Write a game where the player must try to hit the enter/return button exactly 4
seconds apart. It works like this:

- Computer: "Get ready to hit the enter/return key exactly 4 seconds apart"
- Computer: waits for key press
- Player: presses key
- Computer: starts timer
- Player: presses key a second time
- Computer: reports how much time has elapsed
- Computer: start the whole process again

Players may find it helpful to perform an 8-count in their heads while
imagining a song with a tempo of 120 beats per minute.

-----

This program introduces:

- Input from the user via the keyboard
- Endless loop

The program does not include a way to stop. Entering Control-C or Control-D
will probably terminate the program.

## celsius ##

Write a program that converts from Celsius to Farenheit and vice-versa. The
input should be in the form of "37C or "98.6F". If the input is "37C" the
output should be "98.6F". After providing an answer, the program should
continue accepting input.

-----

This program introduces:

- String manipulation
- Converting strings to floating point values

This program also reinforces the use of the conditional statement and endless
loop.

## dna_tm ##

Write a program that allows users to compute the melting temperature (Tm) of an
oligonucleotide (short DNA sequence) by typing (or copy-paste). The program
should quit if the input is empty and report an error if the sequence contains
letters other than A, C, G, or T. There are 2 formulas for Tm, which depend on
the length of the sequence. Your code must define a function `tm()` that takes
a sequence as an argument and returns the Tm. Here are the 2 equations:

- 13 nt or less: 2*A + 2*T + C*4 + G*4
- 14 nt or more: 64.9 + 41 * (C + G -16.4) / (A + C + G + T)

-----

This program introduces:

- Functions

This program also reinforces an endless loop, user input, numeric conversion,
and string manipulation.

## enquire ##

Write a program where the computer tries to guess a number you have in mind.
The bounds are from 1 to 1000. The program should repeatedly ask: "is the
number greater than X?", where X varies with each question. For example:

- Computer: "Think of a number from 1 to 1000 and then hit the enter key"
- User: thinking... imagines the number 789
- User: hits the enter key
- Computer: "Is the number greater than or equal to 500?"
- User: "yes"
- Computer: "Is the number greater than or equal to 750?"
- User: "yes"
- Computer: "Is the number greater than or equal to 875?"
- User: "no"
- etc until
- Computer: "The number you were thinking of is 789"

-----

This program introduces:

- binary search

Binary search is a common algorithmic pattern. It is a very efficient way of
searching for something if the answers are previously sorted (for example, the
numbers from 1 to 1000 are in order).

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

-----

This program reinforces several previous concepts: loops, conditionals, and
functions.

## gregory_leibniz ##

Write a program that esimates Pi (3.1415...) using 3 different methods.

1. Gregory-Leibniz series
2. Nilakantha series
3. Simulation by throwing random darts

The Gregory-Leibniz series is a simple way to estimate Pi. It alternates adding
and subtracting numbers, eventually converging to Pi/4. Use a loop that
terminates after some number of iterations (e.g. 1000).

Pi/4 = 1/1 - 1/3 + 1/5 - 1/7 + 1/9 ...

The Nilakantha series converges faster and is only slightly more complex to
calculate. Terminate this loop when the estimate of Pi is within 1e-6 of the
actual value (you must pretend you don't know the value of Pi).

Pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) ...

A particularly poor (but fun) way to calculate Pi is to simulate throwing darts
with random x, y values in the range from 0 to 1 (e.g. a dart might land at
x=0.35, y=0.84). The ratio of darts that lie inside the circle y = x**2
compared to the total darts eventually converges to Pi/4. It's up to you how
you want to terminate this part.

https://en.wikipedia.org/wiki/Pi

-----

This program introduces:

- Simulation as an algorithmic solution

This program reinforces the use of conditionals and loops. The Nilakantha
termination is related to binary search because each iteration gets closer and
closer to the answer. Developers often have a choice about how they implement
programs, so the random darts question is not specifically defined.

## h... ##

## information ##

Write a program that calculates the information content (entropy) of a
frequency distribution whose values are given on the command line. Here is an
example command line in Python.

```
python3 information.py 0.4 0.3 0.2 0.1
```

- The values from the command line must be converted to a container of floats
- The container must sum very close to 1.0 or produce an error message
- The program must define a function `entropy()` that accepts the container
- The program must return the result in log2

-----

This program introduces:

- Input from the command line
- The list (array, vector) type of container
- Error messages

This program reinforces the use of loops, conditionals, and functions.


## jaccard_index ##

Given 2 files, each containing a list of gene names, determine the Jaccard
Index between the two. The Jaccard Index is defined as the intersection divided
by the union. For this problem, you must use lists (arrays, vectors) not
organized data structures (sets, hashes, maps, dictionaries, trees).

You will find files of gene names ...

https://en.wikipedia.org/wiki/Jaccard_index

-----

This program introduces:

- File input
- Searching a list

This program reinforces the use lists in general and searching for specific
elements in particular. Most built-in search mechanisms are linear, however,
the more advanced progammers may choose to sort their list and then use binary
search. Of course, there are more efficient ways to solve the problem using
more organized data structures, but these are not introduced until...

## kullback_leibler ##

Given a color in the form of RGB values (e.g. 255, 254, 7), determine the
official HTML color name that it is closest to (e.g. 255, 255, 0 is yellow).
Use Kullback-Leibler divergence to determine the similarity of two colors. You
will have to convert RGB values from their usual byte scale (0-255) to
probabilities (0.0 to 1.0).

Need to explain DKL better and include a simple example with easy base 2
values.


Your DKL function should take 2 arguments (force them to figure out how to pass
containers rather than individual values).

dkl(a, b) not dkl(r1, g1, b1, r2, g2, b2)

This is either a struct or tuple or list

Kullback-Leibler (DKL) is but one of many ways to compare histograms. Others
include Taxicab (DTC) distance or Euclidean distance (D2).

Work out these examples pedanticly as well.



Try solving this
problem with DKL as well as DTC and D2. Which do you think works best?

https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence
https://en.wikipedia.org/wiki/Taxicab_geometry
https://en.wikipedia.org/wiki/Euclidean_distance

-----

This program introduces:

- Passing structured data to functions

This program reinforces the idea that there may be more than one way to solve a
problem.

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

