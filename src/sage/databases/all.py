"""
This file gathers together all the tables in Sage.

    * ConwayPolynomials() -- database of selected Conway polynomials.

    * CremonaDatabase() - Cremona's tables of elliptic curves and related data.

    * findstat -- The FindStat database (https://www.findstat.org/).

    * JonesDatabase() -- returns the John Jones table of number fields
      with bounded ramification and degree <= 6.

    * oeis -- The On-Line Encyclopedia of Integer Sequences (https://oeis.org/).

    * SloaneEncyclopedia -- Local copy of Sloane On-Line Encyclopedia of
      Integer Sequences.

    * SteinWatkinsAllData() and SteinWatkinsPrimeData() - The
      Stein-Watkins tables of elliptic curves and related data.

    * SymbolicData() -- many benchmark and testing ideals

EXAMPLES::

    sage: ConwayPolynomials()
    Frank Lübeck's database of Conway polynomials

    sage: CremonaDatabase()
    Cremona's database of elliptic curves with conductor...

    sage: JonesDatabase()
    John Jones's table of number fields with bounded ramification and degree <= 6

    sage: oeis
    The On-Line Encyclopedia of Integer Sequences (https://oeis.org/)

    sage: SymbolicData()
    SymbolicData with ... ideals
"""

# ****************************************************************************
#       Copyright (C) 2005 William Stein <wstein@gmail.com>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

from sage.databases.all__sagemath_combinat import *
from sage.databases.all__sagemath_graphs import *
from sage.databases.all__sagemath_pari import *
from sage.databases.all__sagemath_schemes import *

from sage.misc.lazy_import import lazy_import

lazy_import('sage.databases.jones', 'JonesDatabase')

lazy_import('sage.databases.symbolic_data', 'SymbolicData')

lazy_import('sage.databases.odlyzko', 'zeta_zeros')

from sage.databases.db_class_polynomials import \
    HilbertClassPolynomialDatabase

lazy_import('sage.databases.cunningham_tables', 'cunningham_prime_factors')

del lazy_import
