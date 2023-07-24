Carillon
========

This project implements a generator for all permutations of a given
size.  The algorithm used by the generator appears in section 7.2.1.2
of Donald Knuth's "The Art of Computer Programming, Volume 4A" where
it is called "Algorithm P".  It is known to have been used by `secular
bell ringing societies
<https://www.historytoday.com/archive/months-past/ringing-changes>`_
in 17th century England.  They called it *the method of plain changes*.
It appears in a 1653 manuscript by Peter Mundy.  A description of the
method occupies the first 60 pages of "Tintinnalogia" which was written
by Richard Duckman and Fabian Stedman and published in 1668.

The algorithm is easy to describe recursively.  Given a list L of all
permutations of {0, 1, 2, ..., n -1}, written as n-tuples, one obtains
a list of all permutations of {0, 1, ..., n} by inserting n into each
position of each n-tuple in L.  Reorganizing the algorithm to avoid
storing previous permutations requires some fairly elaborate
bookkeeping, which Knuth describes in the book.

It is easy to observe that most of the steps of the algorithm involve
shifting the element n to the left or the right, which requires almost
no bookkeeping.  Knuth poses, as Exercise 16, the problem of how
to use this observation to speed up the algortithm.

The book includes answers to all exercises and, not surprisingly, the
pseudocode given as the solution of Exercise 16 is somehwat ambiguous.
It is not clear how to resolve the ambiguities to obtain an algorithm
which works.  Presumably this is a pedagogical technique, intended to
encourage a student to actually do the exercise. This project can be
viewed as a solution of Exercise 16, based on the same ideas as the
solution in the book but implemented differently.


