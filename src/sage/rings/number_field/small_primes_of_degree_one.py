# sage_setup: distribution = sagemath-flint
# sage.doctest: needs sage.libs.pari
r"""
Small primes of degree one

Iterator for finding several primes of absolute degree one of a number field of
*small* prime norm.

ALGORITHM:

Let `P` denote the product of some set of prime numbers. (In practice, we
use the product of the first 10000 primes, because Pari computes this many by
default.)

Let `K` be a number field and let `f(x)` be a polynomial defining `K` over the
rational field.  Let `\alpha` be a root of `f` in `K`.

We know that `[ O_K : \ZZ[\alpha] ]^2 = | \Delta(f(x)) / \Delta(O_K) |`, where
`\Delta` denotes the discriminant (see, for example, Proposition 4.4.4, p165 of
[Coh1993]_).  Therefore, after discarding primes dividing `\Delta(f(x))` (this
includes all ramified primes), any integer `n` such that `\gcd(f(n), P) > 0`
yields a prime `p | P` such that `f(x)` has a root modulo `p`.  By the
condition on discriminants, this root is a single root.  As is well known (see,
for example Theorem 4.8.13, p199 of [Coh1993]_), the ideal generated by `(p, \alpha -
n)` is prime and of degree one.

.. WARNING::

    It is possible that there are no primes of `K` of absolute degree one of
    small prime norm, and it is possible that this algorithm will not find
    any primes of small norm.

.. TODO::

    There are situations when this will fail.  There are questions of finding
    primes of relative degree one.  There are questions of finding primes of exact
    degree larger than one.  In short, if you can contribute, please do!

EXAMPLES::

    sage: x = ZZ['x'].gen()
    sage: F.<a> = NumberField(x^2 - 2)
    sage: Ps = F.primes_of_degree_one_list(3)
    sage: Ps # random
    [Fractional ideal (2*a + 1), Fractional ideal (-3*a + 1), Fractional ideal (-a + 5)]
    sage: [ P.norm() for P in Ps ] # random
    [7, 17, 23]
    sage: all(ZZ(P.norm()).is_prime() for P in Ps)
    True
    sage: all(P.residue_class_degree() == 1 for P in Ps)
    True

The next two examples are for relative number fields.::

    sage: L.<b> = F.extension(x^3 - a)
    sage: Ps = L.primes_of_degree_one_list(3)
    sage: Ps # random
    [Fractional ideal (17, b - 5), Fractional ideal (23, b - 4), Fractional ideal (31, b - 2)]
    sage: [ P.absolute_norm() for P in Ps ] # random
    [17, 23, 31]
    sage: all(ZZ(P.absolute_norm()).is_prime() for P in Ps)
    True
    sage: all(P.residue_class_degree() == 1 for P in Ps)
    True
    sage: M.<c> = NumberField(x^2 - x*b^2 + b)
    sage: Ps = M.primes_of_degree_one_list(3)
    sage: Ps # random
    [Fractional ideal (17, c - 2), Fractional ideal (c - 1), Fractional ideal (41, c + 15)]
    sage: [ P.absolute_norm() for P in Ps ] # random
    [17, 31, 41]
    sage: all(ZZ(P.absolute_norm()).is_prime() for P in Ps)
    True
    sage: all(P.residue_class_degree() == 1 for P in Ps)
    True

AUTHORS:

- Nick Alexander (2008): initial version
- David Loeffler (2009): fixed a bug with relative fields
- Maarten Derickx (2017): fixed a bug with number fields not generated by an integral element
"""

#*****************************************************************************
#       Copyright (C) 2008 William Stein
#
#  Distributed under the terms of the GNU General Public License (GPL)
#
#    This code is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#  The full text of the GPL is available at:
#
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.rings.integer_ring import ZZ


class Small_primes_of_degree_one_iter:
    r"""
    Iterator that finds primes of a number field of absolute degree
    one and bounded small prime norm.

    INPUT:

    - ``field`` -- a :class:`NumberField`

    - ``num_integer_primes`` -- integer (default: 10000); we try to find
      primes of absolute norm no greater than the ``num_integer_primes``-th
      prime number. For example, if ``num_integer_primes`` is 2, the largest
      norm found will be 3, since the second prime is 3.

    - ``max_iterations`` -- integer (default: 100); we test ``max_iterations``
      integers to find small primes before raising :class:`StopIteration`

    AUTHOR:

    - Nick Alexander
    """
    def __init__(self, field, num_integer_primes=10000, max_iterations=100):
        r"""
        Construct a new iterator of small degree one primes.

        EXAMPLES::

            sage: x = QQ['x'].gen()
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K.primes_of_degree_one_list(3) # random
            [Fractional ideal (2*a + 1), Fractional ideal (-a + 4), Fractional ideal (3*a + 2)]
        """
        self._field = field
        self._poly = self._field.absolute_field('b').defining_polynomial()
        self._poly = ZZ['x'](self._poly.denominator() * self._poly()) # make integer polynomial
        self._lc = self._poly.leading_coefficient()

        # this uses that [ O_K : Z[a] ]^2 = | disc(f(x)) / disc(O_K) |
        from sage.libs.pari import pari
        self._prod_of_small_primes = ZZ(pari('TEMPn = %s; TEMPps = primes(TEMPn); prod(X = 1, TEMPn, TEMPps[X])' % num_integer_primes))
        self._prod_of_small_primes //= self._prod_of_small_primes.gcd(self._poly.discriminant() * self._lc)

        self._integer_iter = iter(ZZ)
        self._queue = []
        self._max_iterations = max_iterations

    def __iter__(self):
        r"""
        Return ``self`` as an iterator.

        EXAMPLES::

            sage: x = QQ['x'].gen()
            sage: K.<a> = NumberField(x^2 - 3)
            sage: it = K.primes_of_degree_one_iter()
            sage: iter(it) == it # indirect doctest
            True
        """
        return self

    def _lengthen_queue(self):
        r"""
        Try to find more primes of absolute degree one of small prime
        norm.

        Checks \code{self._max_iterations} integers before failing.

        WARNING:

            Internal function.  Not for external use!

        EXAMPLES::

            sage: x = QQ['x'].gen()
            sage: K.<a> = NumberField(x^2 - 3)
            sage: Ps = K.primes_of_degree_one_list(20, max_iterations=3) # indirect doctest
            sage: len(Ps) == 20
            True
        """
        count = 0
        while count < self._max_iterations:
            n = next(self._integer_iter)
            g = self._prod_of_small_primes.gcd(self._poly(n))
            self._prod_of_small_primes //= g
            self._queue = self._queue + [ (p, n) for p in g.prime_divisors() ]
            count += 1
        self._queue.sort() # sorts in ascending order

    def __next__(self):
        r"""
        Return a prime of absolute degree one of small prime norm.

        Raises ``StopIteration`` if such a prime cannot be easily found.

        EXAMPLES::

            sage: x = QQ['x'].gen()
            sage: K.<a> = NumberField(x^2 - 3)
            sage: it = K.primes_of_degree_one_iter()
            sage: [ next(it) for i in range(3) ] # random
            [Fractional ideal (2*a + 1), Fractional ideal (-a + 4), Fractional ideal (3*a + 2)]

        TESTS:

        We test that :issue:`6396` is fixed. Note that the doctest is
        flagged as random since the string representation of ideals is
        somewhat unpredictable::

            sage: N.<a,b> = NumberField([x^2 + 1, x^2 - 5])
            sage: ids = N.primes_of_degree_one_list(10); ids  # random
            [Fractional ideal ((-1/2*b + 1/2)*a + 2),
             Fractional ideal (-b*a + 1/2*b + 1/2),
             Fractional ideal ((1/2*b + 3/2)*a - b),
             Fractional ideal ((-1/2*b - 3/2)*a + b - 1),
             Fractional ideal (-b*a - b + 1),
             Fractional ideal (3*a + 1/2*b - 1/2),
             Fractional ideal ((-3/2*b + 1/2)*a + 1/2*b - 1/2),
             Fractional ideal ((-1/2*b - 5/2)*a - b + 1),
             Fractional ideal (2*a - 3/2*b - 1/2),
             Fractional ideal (3*a + 1/2*b + 5/2)]
             sage: [x.absolute_norm() for x in ids]
             [29, 41, 61, 89, 101, 109, 149, 181, 229, 241]
             sage: ids[9] == N.ideal(3*a + 1/2*b + 5/2)
             True

        We test that :issue:`23468` is fixed::

            sage: R.<z> = QQ[]
            sage: K.<y> = QQ.extension(25*z^2 + 26*z + 5)
            sage: for p in K.primes_of_degree_one_list(10):
            ....:     assert p.is_prime()
        """
        if not self._queue:
            self._lengthen_queue()
        if not self._queue:
            raise StopIteration

        p, n = self._queue.pop(0)
        x = self._field.absolute_generator()
        return self._field.ideal([p, (x - n) * self._lc])

    next = __next__
