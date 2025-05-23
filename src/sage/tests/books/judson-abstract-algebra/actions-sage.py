# sage_setup: distribution = sagemath-repl
# sage.doctest: needs sage.graphs sage.groups
##          Sage Doctest File         ##
#**************************************#
#*    Generated from PreTeXt source   *#
#*    on 2017-08-24T11:43:34-07:00    *#
#*                                    *#
#*   http://mathbook.pugetsound.edu   *#
#*                                    *#
#**************************************#
##
"""
Please contact Rob Beezer (beezer@ups.edu) with
any test failures here that need to be changed
as a result of changes accepted into Sage.  You
may edit/change this file in any sensible way, so
that development work may procede.  Your changes
may later be replaced by the authors of "Abstract
Algebra: Theory and Applications" when the text is
updated, and a replacement of this file is proposed
for review.
"""
##
## To execute doctests in these files, run
##   $ $SAGE_ROOT/sage -t <directory-of-these-files>
## or
##   $ $SAGE_ROOT/sage -t <a-single-file>
##
## Replace -t by "-tp n" for parallel testing,
##   "-tp 0" will use a sensible number of threads
##
## See: http://www.sagemath.org/doc/developer/doctesting.html
##   or run  $ $SAGE_ROOT/sage --advanced  for brief help
##
## Generated at 2017-08-24T11:43:34-07:00
## From "Abstract Algebra"
## At commit 26d3cac0b4047f4b8d6f737542be455606e2c4b4
##
## Section 14.7 Sage
##
r"""
~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: D = DihedralGroup(8)
    sage: C = D.center(); C
    Subgroup generated by [(1,5)(2,6)(3,7)(4,8)]
    of (Dihedral group of order 16 as a permutation group)

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: C.list()
    [(), (1,5)(2,6)(3,7)(4,8)]

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: a = D("(1,2)(3,8)(4,7)(5,6)")
    sage: C1 = D.centralizer(a); C1.list()
    [(), (1,2)(3,8)(4,7)(5,6), (1,5)(2,6)(3,7)(4,8), (1,6)(2,5)(3,4)(7,8)]

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: b = D("(1,2,3,4,5,6,7,8)")
    sage: C2 = D.centralizer(b); C2.order()
    8

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: CCR = D.conjugacy_classes_representatives(); CCR
    [(), (2,8)(3,7)(4,6), (1,2)(3,8)(4,7)(5,6), (1,2,3,4,5,6,7,8),
     (1,3,5,7)(2,4,6,8), (1,4,7,2,5,8,3,6), (1,5)(2,6)(3,7)(4,8)]

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: r = CCR[2]; r
    (1,2)(3,8)(4,7)(5,6)

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: conj = []
    sage: x = [conj.append(g^-1*r*g) for g in D if not g^-1*r*g in conj]
    sage: conj
    [(1,2)(3,8)(4,7)(5,6),
     (1,6)(2,5)(3,4)(7,8),
     (1,8)(2,7)(3,6)(4,5),
     (1,4)(2,3)(5,8)(6,7)]

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: sizes = [D.order()/D.centralizer(g).order()
    ....:              for g in D.conjugacy_classes_representatives()]
    sage: sizes
    [1, 4, 4, 2, 2, 2, 1]

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: D.order() == sum(sizes)
    True

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: Q = graphs.CubeGraph(3)
    sage: Q.plot(layout='spring')   # not tested

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: A = Q.automorphism_group()
    sage: A.order()
    48

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: a = A("('000','001')('010','011')('110','111')('100','101')")
    sage: a in A
    True

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: A.orbits()        # random
    [['000', '001', '010', '100', '011', '101', '110', '111']]

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: A.is_transitive()
    True

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: S = A.stabilizer('000')
    sage: S.list()          # random
    [(),
     ('001','100','010')('011','101','110'),
     ('010','100')('011','101'),
     ('001','010','100')('011','110','101'),
     ('001','100')('011','110'),
     ('001','010')('101','110')]

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: P = graphs.PathGraph(11)
    sage: P.plot()   # not tested

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: A = P.automorphism_group()
    sage: A.list()
    [(), (0,10)(1,9)(2,8)(3,7)(4,6)]

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: A.is_transitive()
    False

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: A.orbits()
    ((0, 10), (1, 9), (2, 8), (3, 7), (4, 6), (5,))

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: A.stabilizer(2).list()
    [()]

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: A.stabilizer(5).list()
    [(), (0,10)(1,9)(2,8)(3,7)(4,6)]

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: G = SymmetricGroup(4)
    sage: S = G.stabilizer(4)
    sage: S.orbits()
    ((1, 2, 3), (4,))
"""
