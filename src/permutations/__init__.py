"""
This module exports a generator for elements of a permutation group.

This is a Python implementation of the "Plain Changes" algorithm
presented as Algorithm P in volume 4A of Donald Knuth's 'The Art of
Computer Programming'.  The variable names agree with Knuth's, but we
use 0-based indexing, of course.

Since we use the python match statement, version 3.10 or higher is
required.  For older versions, rewrite the match with if and continue.
"""
__version__ = '0.0.0'

def permutations(size):
    """Generator for all permutations of [0, 1, ..., size - 1].

    Return values are tuples with entries in range(size).

    >>> for p in permutations(3):
    ...     print(p)
    ... 
    (0, 1, 2)
    (0, 2, 1)
    (2, 0, 1)
    (2, 1, 0)
    (1, 2, 0)
    (1, 0, 2)
    """
    # Initialization
    # Start at the identity permutation:
    a = list(range(size))
    # The largest element of a:
    z = size - 1
    # The index of z when z is being shifted:
    Iz = z
    # The number of elements of a which are less than i
    # and have index larger than the index of i is
    # recorded as c[i].
    c = size*[0]
    # At each iteration the element j is swapped with a neighbor.
    # The value of o[j] is 1 if the neighbor is on the left, -1 otherwise.
    o = size*[1]
    shift_z = True
    state = 1
    while True:
        match state:
            case 1:
                yield tuple(a)
                j = z
                s = 0
                state = 2
            case 2:
                if j == 0:
                    return
                q = c[j] + o[j]
                if q == j + 1:
                    state = 3
                elif q < 0:
                    state = 4
                elif shift_z:
                    # Just shift z; avoiding all of the rigamarole.
                    shift_z = False
                    if Iz == size - 1:  # Shift z left
                        while Iz > 0:
                            a[Iz] = a[Iz - 1]
                            a[Iz - 1] = z
                            Iz -= 1
                            yield tuple(a)
                        c[z] = z
                    elif Iz == 0:         # Shift z right
                        while Iz < size - 1:
                            a[Iz] = a[Iz + 1]
                            a[Iz + 1] = z
                            Iz += 1
                            yield tuple(a)
                        c[z] = 0
                else:
                    # Compose with the transposition given by the full algorithm.
                    M = j + s - c[j]
                    N = M - o[j]
                    a[M], a[N] = a[N], a[M]
                    c[j] = q
                    shift_z = True
                    state = 1
            case 3:
                s += 1
                state = 4
            case 4:
                o[j] = -o[j]
                j -= 1
                state = 2
