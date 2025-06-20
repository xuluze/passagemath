# sage_setup: distribution = sagemath-combinat
# sage.doctest: needs sage.combinat sage.modules
r"""
Weyl Lie Conformal Algebra

Given a commutative ring `R`, a free `R`-module `M` and a
non-degenerate, skew-symmetric, bilinear pairing
`\langle \cdot,\cdot\rangle: M \otimes_R M \rightarrow R`. The *Weyl*
Lie conformal algebra associated to this datum is the free
`R[T]`-module generated by `M` plus a central vector `K`. The
non-vanishing `\lambda`-brackets are given by:

.. MATH::

    [v_\lambda w] = \langle v, w\rangle K.

This is not an H-graded Lie conformal algebra. The choice of a
Lagrangian decomposition `M = L \oplus L^*` determines an H-graded
structure. For this H-graded Lie conformal algebra see the
:mod:`Bosonic Ghosts Lie conformal algebra<sage.algebras.\
lie_conformal_algebras.bosonic_ghosts_lie_conformal_algebra>`

AUTHORS:

- Reimundo Heluani (2019-08-09): Initial implementation.
"""

# *****************************************************************************
#       Copyright (C) 2019 Reimundo Heluani <heluani@potuz.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

from .lie_conformal_algebra_with_structure_coefs import \
    LieConformalAlgebraWithStructureCoefficients
from sage.matrix.special import identity_matrix
from sage.structure.indexed_generators import standardize_names_index_set


class WeylLieConformalAlgebra(LieConformalAlgebraWithStructureCoefficients):
    r"""
    The Weyl Lie conformal algebra.

    INPUT:

    - ``R`` -- a commutative ring; the base ring of this Lie
      conformal algebra
    - ``ngens`` -- an even positive Integer (default: `2`); the number
      of non-central generators of this Lie conformal algebra
    - ``gram_matrix`` -- a matrix (default: ``None``); a non-singular
      skew-symmetric square matrix with coefficients in `R`
    - ``names`` -- list or tuple of strings; alternative names
      for the generators
    - ``index_set`` -- an enumerated set; alternative indexing set
      for the generators

    OUTPUT:

    The Weyl Lie conformal algebra with generators
     `\alpha_i`, `i=1,...,ngens` and `\lambda`-brackets

     .. MATH::

        [{\alpha_i}_{\lambda} \alpha_j] = M_{ij} K,

    where `M` is the ``gram_matrix`` above.

    .. NOTE::

        The returned Lie conformal algebra is not `H`-graded. For
        a related `H`-graded Lie conformal algebra see
        :class:`BosonicGhostsLieConformalAlgebra<sage.algebras.\
        lie_conformal_algebras.bosonic_ghosts_lie_conformal_algebra\
        .BosonicGhostsLieConformalAlgebra>`.

    EXAMPLES::

        sage: lie_conformal_algebras.Weyl(QQ)
        The Weyl Lie conformal algebra with generators (alpha0, alpha1, K) over Rational Field
        sage: R = lie_conformal_algebras.Weyl(QQbar, gram_matrix=Matrix(QQ,[[0,1],[-1,0]]), names = ('a','b'))
        sage: R.inject_variables()
        Defining a, b, K
        sage: a.bracket(b)
        {0: K}
        sage: b.bracket(a)
        {0: -K}

        sage: R = lie_conformal_algebras.Weyl(QQbar, ngens=4)
        sage: R.gram_matrix()
        [ 0  0| 1  0]
        [ 0  0| 0  1]
        [-----+-----]
        [-1  0| 0  0]
        [ 0 -1| 0  0]
        sage: R.inject_variables()
        Defining alpha0, alpha1, alpha2, alpha3, K
        sage: alpha0.bracket(alpha2)
        {0: K}

        sage: R = lie_conformal_algebras.Weyl(QQ); R.category()
        Category of finitely generated Lie conformal algebras with basis over Rational Field
        sage: R in LieConformalAlgebras(QQ).Graded()
        False
        sage: R.inject_variables()
        Defining alpha0, alpha1, K
        sage: alpha0.degree()
        Traceback (most recent call last):
        ...
        AttributeError: 'WeylLieConformalAlgebra_with_category.element_class' object has no attribute 'degree'...

    TESTS::

        sage: lie_conformal_algebras.Weyl(ZZ, gram_matrix=identity_matrix(ZZ,3))
        Traceback (most recent call last):
        ...
        ValueError: the Gram_matrix should be a non degenerate skew-symmetric 3 x 3 matrix, got [1 0 0]
        [0 1 0]
        [0 0 1]
    """
    def __init__(self, R, ngens=None, gram_matrix=None, names=None,
                 index_set=None):
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.Weyl(QQ)
            sage: TestSuite(V).run()
        """
        from sage.matrix.matrix_space import MatrixSpace
        if ngens:
            from sage.rings.integer_ring import ZZ
            if not (ngens in ZZ and not ngens % 2):
                raise ValueError("ngens needs to be an even positive Integer, "
                                 f"got {ngens}")
        if gram_matrix is not None:
            if ngens is None:
                ngens = gram_matrix.dimensions()[0]
            try:
                assert (gram_matrix in MatrixSpace(R, ngens, ngens))
            except AssertionError:
                raise ValueError("the Gram_matrix should be a skew-symmetric "
                    "{0} x {0} matrix, got {1}".format(ngens, gram_matrix))
            if (not gram_matrix.is_skew_symmetric() or
                    gram_matrix.is_singular()):
                raise ValueError("the Gram_matrix should be a non degenerate "
                                 "skew-symmetric {0} x {0} matrix, got {1}"
                                 .format(ngens, gram_matrix))
        elif gram_matrix is None:
            if ngens is None:
                ngens = 2
            A = identity_matrix(R, ngens // 2)
            from sage.matrix.special import block_matrix
            gram_matrix = block_matrix([[R.zero(), A], [-A, R.zero()]])

        latex_names = None
        if (names is None) and (index_set is None):
            names = 'alpha'
            latex_names = tuple(r'\alpha_{%d}' % i
                                for i in range(ngens)) + ('K',)
        names, index_set = standardize_names_index_set(names=names,
                                                      index_set=index_set,
                                                      ngens=ngens)
        weyldict = {(i, j): {0: {('K', 0): gram_matrix[index_set.rank(i),
                                                       index_set.rank(j)]}}
                    for i in index_set for j in index_set}

        super().__init__(R, weyldict, names=names,
                         latex_names=latex_names,
                         index_set=index_set,
                         central_elements=('K',))
        self._gram_matrix = gram_matrix

    def _repr_(self):
        """
        The name of this Lie conformal algebra.

        EXAMPLES::

            sage: R = lie_conformal_algebras.Weyl(ZZ); R
            The Weyl Lie conformal algebra with generators (alpha0, alpha1, K) over Integer Ring
        """
        return "The Weyl Lie conformal algebra with generators {} over {}"\
            .format(self.gens(), self.base_ring())

    def gram_matrix(self):
        r"""
        The Gram matrix that specifies the `\lambda`-brackets of the
        generators.

        EXAMPLES::

            sage: R = lie_conformal_algebras.Weyl(QQbar, ngens=4)
            sage: R.gram_matrix()
            [ 0  0| 1  0]
            [ 0  0| 0  1]
            [-----+-----]
            [-1  0| 0  0]
            [ 0 -1| 0  0]
        """
        return self._gram_matrix
