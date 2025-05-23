# sage_setup: distribution = sagemath-repl
# sage.doctest: needs sage.graphs
"""
This file (./sol/graphtheory_doctest.sage) was *autogenerated* from ./sol/graphtheory.tex,
with sagetex.sty version 2011/05/27 v2.3.1.
It contains the contents of all the sageexample environments from this file.
You should be able to doctest this file with:
sage -t ./sol/graphtheory_doctest.sage
It is always safe to delete this file; it is not used in typesetting your
document.

Sage example in ./sol/graphtheory.tex, line 5::

  sage: def circulant(n, d):
  ....:    g = Graph(n)
  ....:    for u in range(n):
  ....:        for c in range(d):
  ....:            g.add_edge(u,(u+c)%n)
  ....:    return g

Sage example in ./sol/graphtheory.tex, line 19::

  sage: def kneser(n, k):
  ....:    g = Graph()
  ....:    g.add_vertices(Subsets(n,k))
  ....:    for u in g:
  ....:        for v in g:
  ....:            if not u & v:
  ....:                g.add_edge(u,v)
  ....:    return g

Sage example in ./sol/graphtheory.tex, line 33::

  sage: def kneser(n, k):
  ....:    g = Graph()
  ....:    sommets = Set(range(n))
  ....:    g.add_vertices(Subsets(sommets,k))
  ....:    for u in g:
  ....:        for v in Subsets(sommets - u,k):
  ....:            g.add_edge(u,v)
  ....:    return g

Sage example in ./sol/graphtheory.tex, line 59::

  sage: g = graphs.PetersenGraph()
  sage: def optimal_order(g):
  ....:    order = []
  ....:    for color_class in sorted(g.coloring()):
  ....:        for v in color_class:
  ....:            order.append(v)
  ....:    return order
  sage: optimal_order(g)
  [0, 2, 6, 1, 3, 5, 9, 4, 7, 8]
"""
