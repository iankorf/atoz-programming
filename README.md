A to Z Programming
==================

WARNING: this is highly volatile at the moment

This is a collection of 26 exercises that will improve your programming skill.
These exercises were built for the UC Davis class "MCB185: Programming for
Biologists". For this reason, many of the exercises have a molecular biology
theme. The class introduces the Unix/Linux command line environment, so there
are a few areas where working in Unix/Linux is assumed. Some problems require
data files, which you will find in the `data` directory. MCB185 is taught in
Python, but solutions to these problems may be available in other langauges.
See the various language directories for more information.

- [acgt](#acgt)
- [beat_box](#beat_box)
- [celsius](#celsius)
- [dna_tm](#dna_tm)
- [euler](#euler)
- [fizzprime](#fizzprime)
- [gregory](#gregory)
- [hydropathy](#hydropathy)
- [information](#information)
- [jaccard](#jaccard)
- [kolormatch](#kolormatch)
- [low_entropy](#low_entropy)
- [molbio](#molbio)
- [n50](#n50)
- [orf_finder](#orf_finder)
- [prosite](#prosite)
- [quality_trim](#quality_trim)
- [ribosome](#ribosome)
- [sigpep](#sigpep)
- [transfac](#transfac)
- [unique_kmers](#unique_kmers)
- [viterbi](#viterbi)
- [water](#water)
- [xref](#xref)
- [y...](#y...)
- [z...](#z...)


## acgt ##

Write a program that randomly prints out a single letter of DNA. In most
eukarytotic genomes, you are more likely to see an A or T than C or G, so make
the program do that also. In the human genome, about 60% is A/T and 40% is C/G.

Example of command line and output:

```
$ python3 acgt.py
A
```

## beat_box ##

Write a game where the player must try to hit the enter/return button exactly 4
seconds apart. It works like this:

- Computer: "Get ready to hit the enter key exactly 4 seconds apart!"
- Computer: "Press enter when ready..."
- Computer: waits for key press
- Player: presses key
- Computer: starts timer
- Computer: "Press the enter key after exactly 4 seconds"
- Player: presses key a second time
- Computer: reports how much time has elapsed
- Computer: start the whole process again

Players may find it helpful to perform an 8-count in their heads while
imagining a song with a tempo of 120 beats per minute.

Example of command line and output:

```
$ python3 beat_box.py
Get ready to hit the enter key exactly 4 seconds apart
Press enter when ready...
Press the enter key after exactly 4 seconds!
Your time: 2.679888963699341 was off by 33.00 percent.
Get ready to hit the enter key exactly 4 seconds apart!
```

## celsius ##

Write a program that converts from Celsius to Farenheit and vice-versa. The
input should be in the form of "37C or "98.6F". If the input is "37C" the
output should be "98.6F". After providing an answer, the program should
continue accepting input until the user enters a blank line.

Example of command line and input/output:

```
$ python3 celsius.py
What temperature to convert (e.g. 37C or 98.6F): 37C
37.0C is 98.6F
What temperature to convert (e.g. 37C or 98.6F): 98.6F
98.6F is 37.0C
What temperature to convert (e.g. 37C or 98.6F):
```

## dna_tm ##

Write a program that allows users to compute the melting temperature (Tm) of an
oligonucleotide (short DNA sequence) by typing (or copy-paste). The program
should quit if the input is empty and terminate with an error message if the
sequence contains letters other than A, C, G, or T. There are 2 formulas for
Tm, which depend on the length of the sequence. Your code must define a
function `tm()` that takes a sequence as an argument and returns the Tm. Here
are the 2 equations:

- 13 nt or less: 2*A + 2*T + C*4 + G*4
- 14 nt or more: 64.9 + 41 * (C + G -16.4) / (A + C + G + T)

Example of command line and input/output

```
$ python3 dna_tm.py
Oligo sequence: TAATACGACTCACTATAGGG
The Tm of TAATACGACTCACTATAGGG is 47.680C
```

## euler ##

Write a program that estimates Euler's number, e (2.71828...). This is the sum
of 1/n! ad infinitum. Write your own factorial function rather than using
`math.factorial()`. Print the value of e with each iteration of the loop.
Terminate the loop when the value of e no longer changes (runs out of
precision).

Example command line and output:

```
$ python3 euler.py
1.0
2.0
2.5
2.6666666666666665
2.708333333333333
2.7166666666666663
2.7180555555555554
2.7182539682539684
2.71827876984127
2.7182815255731922
2.7182818011463845
2.718281826198493
2.7182818282861687
2.7182818284467594
2.71828182845823
2.718281828458995
2.718281828459043
2.7182818284590455
```

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

```
$ python3 fizzprime.py
1
2*
Fizz*
4
Buzz*
Fizz
7*
8
Fizz
Buzz
11*
Fizz
13*
14
FizzBuzz
16
17*
```

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

```
$ python3 gregory.py  | less
Gregory odd-even: 3.140592653839794
Gregory flip-flop: 3.140592653839794
Nilakantha definite: 3.141839618929402
Nilakantha indefinite: 3.1666666666666665
Nilakantha indefinite: 3.1333333333333333
Nilakantha indefinite: 3.145238095238095
Nilakantha indefinite: 3.1396825396825396
Nilakantha indefinite: 3.1427128427128426
Nilakantha indefinite: 3.1408813408813407
Nilakantha indefinite: 3.142071817071817
Nilakantha indefinite: 3.1412548236077646
Infinite: 2.6666666666666665
Infinite: 3.0
Infinite: 3.2
Infinite: 3.3333333333333335
Infinite: 3.4285714285714284
Infinite: 3.0
Infinite: 3.111111111111111
Infinite: 3.2
Infinite: 3.272727272727273
Infinite: 3.3333333333333335
```

## hydropathy ##

Write a program that calculates the hydropathy of a sequence given as a command
line argument. Use the Kyte-Doolittle hydropathy scale.

```
$ python/hydropathy.py  MVSLPTVLQRVILN
Average hydropathy: 1.129
```

https://en.wikipedia.org/wiki/Hydrophilicity_plot
https://en.wikipedia.org/wiki/Hydrophobicity_scales


## information ##

Write a program that calculates the information content (entropy) of a
frequency distribution whose values are given on the command line.

- The values from the command line must be converted to a list of floats
- The container must sum very close to 1.0 or produce an error message
- The program must define a function `entropy()` that accepts the container
- The program must return the result in log2

```
$ python3 information.py 0.4 0.3 0.2 0.1
1.8464393446710154
```


## jaccard ##

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

## kolormatch ##

Given a color in the form of RGB values (e.g. 255, 254, 7), determine the
official HTML color name that it is closest to (e.g. 255, 255, 0 is yellow).



Your distance function should take 2 arguments (force them to figure out how to
pass containers rather than individual values).



This is either a struct or tuple or list

Taxicab (DTC) distance or Euclidean distance (D2).

Work out these examples pedanticly as well.

Data is in the file...

Try solving this
problem with DKL as well as DTC and D2. Which do you think works best?

https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence
https://en.wikipedia.org/wiki/Taxicab_geometry
https://en.wikipedia.org/wiki/Euclidean_distance

-----

This program introduces:

- Structured data of some kind
- Passing structured data to functions

This program reinforces the idea that there may be more than one way to solve a
problem.

## low_entropy ##

Commmand line parameters for file, window size, threshold

-----

Introduces:

- Windowing algorithm
- FASTA file reading (single record only)
- Converting a string into a list (some languages)


Forward reference to rloop and shannon and argparse?

## mcb185 ##

Write a function library with a FASTA file reader that reads sequence records
one at a time. Write a program that imports the library and reports the name
and length of each sequence.

-----

This task introduces function libraries (modules, packages).

## n... ##

## orf ##

Find open reading frames using ATG..STOP.

## phred? ##

## quartiles? ##

Quality values? Quality Trimmer?

Many ways to calculate quartiles... interesting. Good place for stats in
general. Do some kind of analysis on the lengths of proteins in E. coli?

## rloop_finder ##

The faster windowing algorithm here. Also re-using G + C instead of
re-calculating everything.

## shannon_filter ##

Argparse and FASTA reader with faster windowing. Do this all the right way.

## translate ##

This is just more windowing, but it's also reverse-complement intro. It's the
dictionary lookup.

## unique_kmers ##

Which kmers occur just once in a genome? Which ones don't occur at all?

This could also be, "which kmers occur in one genome but not the other?"

This is adding dictionary items that you don't know exist or not.

## v... ##

validate
valine
variant
vector

## weight_matrix ##

This is complex data

## x... ##

xref - cross reference names from one list to another, this is one name to many names, so key -> array of key or key -> set or something

## y... ##

Y.pestis? Which kmers are in Y.pestis but not E.coli and vice-versa. Could also
do the Jaccard Index of the kmers. It could be an ortholog question too.

## z... ##



