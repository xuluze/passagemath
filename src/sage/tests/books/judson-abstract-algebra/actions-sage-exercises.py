# sage_setup: distribution = sagemath-repl
# sage.doctest: needs sage.graphs sage.plot
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
## Exercises 14.8 Sage Exercises
##
r"""
~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: G = Graph([(1,2), (2,3), (3,1)])
    sage: G.plot()   # not tested

~~~~~~~~~~~~~~~~~~~~~~ ::

    sage: G = graphs.CycleGraph(8)
    sage: G.add_edges([(0,2),(1,3),(4,6),(5,7)])
    sage: G.plot()   # not tested
"""
