# sage_setup: distribution = sagemath-repl
# sage.doctest: needs scipy sage.symbolic
"""
This file (./float_doctest.sage) was *autogenerated* from ./float.tex,
with sagetex.sty version 2011/05/27 v2.3.1.
It contains the contents of all the sageexample environments from this file.
You should be able to doctest this file with:
sage -t ./float_doctest.sage
It is always safe to delete this file; it is not used in typesetting your
document.

Sage example in ./float.tex, line 251::

  sage: xrdf = RDF(3.0)

Sage example in ./float.tex, line 276::

  sage: R100 = RealField(100) # precision: 100 bits.
  sage: x100 = R100(3/8); x100
  0.37500000000000000000000000000

Sage example in ./float.tex, line 300::

  sage: Rdefault = RealField()  # default precision of 53 bits
  sage: xdefault = Rdefault(2/3)

Sage example in ./float.tex, line 319::

  sage: xrdf.prec()
  53
  sage: x100.prec()
  100
  sage: xdefault.prec()
  53

Sage example in ./float.tex, line 347::

  sage: x = 1.0; type(x)
  <... 'sage.rings.real_mpfr.RealLiteral'>
  sage: x.prec()
  53

Sage example in ./float.tex, line 384::

  sage: x = 1.0         # x belongs to RealField()
  sage: x = 0.1e+1      # idem: x belongs to RealField()
  sage: x = 1           # x is an integer
  sage: x = RDF(1)      # x is a machine double-precision number
  sage: x = RDF(1.)     # idem: x is a machine double-precision number
  sage: x = RDF(0.1e+1) # idem
  sage: x = 4/3         # x is a rational number
  sage: R = RealField(20)
  sage: x = R(1)        # x is a 20-bit floating-point number

Sage example in ./float.tex, line 400::

  sage: RDF(8/3)
  2.6666666666666665
  sage: R100 = RealField(100); R100(8/3)
  2.6666666666666666666666666667

Sage example in ./float.tex, line 412::

  sage: x = R100(8/3)
  sage: R = RealField(); R(x)
  2.66666666666667
  sage: RDF(x)
  2.6666666666666665

Sage example in ./float.tex, line 431::

  sage: 1.0/0.0
  +infinity
  sage: RDF(1)/RDF(0)
  +infinity
  sage: RDF(-1.0)/RDF(0.)
  -infinity

Sage example in ./float.tex, line 441::

  sage: 0.0/0.0
  NaN
  sage: RDF(0.0)/RDF(0.0)
  NaN

Sage example in ./float.tex, line 496::

  sage: R2 = RealField(2)

Sage example in ./float.tex, line 545::

  sage: x2 = R2(1.); x2.ulp()
  0.50
  sage: xr = 1.; xr.ulp()
  2.22044604925031e-16

Sage example in ./float.tex, line 655::

  sage: a = 10000.0; b = 9999.5; c = 0.1; c
  0.100000000000000
  sage: a1 = a+c # add a small perturbation to a.
  sage: a1-b
  0.600000000000364

Sage example in ./float.tex, line 680::

  sage: a = 1.0; b = 10.0^4; c = 1.0
  sage: delta = b^2-4*a*c
  sage: x = (-b-sqrt(delta))/(2*a); y = (-b+sqrt(delta))/(2*a)
  sage: x, y
  (-9999.99990000000, -0.000100000001111766)

Sage example in ./float.tex, line 692::

  sage: x+y+b/a
  0.000000000000000
  sage: x*y-c/a
  1.11766307320238e-9

Sage example in ./float.tex, line 713::

  sage: y = (c/a)/x; y
  -0.000100000001000000
  sage: x+y+b/a
  0.000000000000000
  sage: x*y-c/a
  -1.11022302462516e-16

Sage example in ./float.tex, line 746::

  sage: x1 = R2(1/2); x2 = R2(4); x3 = R2(-4)
  sage: x1, x2, x3
  (0.50, 4.0, -4.0)
  sage: x1+(x2+x3)
  0.50
  sage: (x1+x2)+x3
  0.00

Sage example in ./float.tex, line 781::

  sage: x = RDF(1/3)
  sage: for i in range(1,100): x = 4*x-1; print(x)
  0.33333333333333326
  0.33333333333333304
  0.33333333333333215
  ...
  -1.0
  -5.0
  -21.0
  -85.0
  -341.0
  -1365.0
  -5461.0
  -21845.0
  ...

Sage example in ./float.tex, line 824::

  sage: x = RDF(1/2)
  sage: for i in range(1,100): x = 3*x-1; print(x)
  0.5
  0.5
  0.5
  ...
  0.5

Sage example in ./float.tex, line 863::

  sage: x = RDF(1/3)

Sage example in ./float.tex, line 867::

  sage: x = 1/3

Sage example in ./float.tex, line 990::

  sage: def sumharmo(p):
  ....:    RFP = RealField(p)
  ....:    y = RFP(1.); x = RFP(0.); n = 1
  ....:    while x != y:
  ....:        y = x; x += 1/n; n += 1
  ....:    return p, n, x

Sage example in ./float.tex, line 1003::

  sage: sumharmo(2)
  (2, 5, 2.0)
  sage: sumharmo(20)
  (20, 131073, 12.631)

Sage example in ./float.tex, line 1072::

  sage: def iter(y, delta, a, n):
  ....:     for i in range(0,n):
  ....:         y += delta
  ....:         delta *= a
  ....:     return y

Sage example in ./float.tex, line 1087::

  sage: def exact(y, delta, a, n):
  ....:     return y+delta*(1-a^n)/(1-a)

Sage example in ./float.tex, line 1106::

  sage: y0 = RDF(10^13); delta0 = RDF(1); a = RDF(1-10^(-8)); n = 100000
  sage: ii = iter(y0,delta0,a,n)
  sage: s = exact(10^13,1,1-10^(-8),n)
  sage: print("exact - classical summation: %.1f" % (s-ii))  # abs tol 0.1
  exact - classical summation: -45.6

Sage example in ./float.tex, line 1128::

  sage: def sumcomp(y, delta, e, n, a):
  ....:     for i in range(0,n):
  ....:         b = y
  ....:         e += delta
  ....:         y = b+e
  ....:         e += (b-y)
  ....:         delta = a*delta # new value of delta
  ....:     return y

Sage example in ./float.tex, line 1194::

  sage: c = sumcomp(y0,delta0,RDF(0.0),n,a)
  sage: print("exact - compensated summation: %.5f" \
  ....:       % RDF(s-RR(c).exact_rational()))
  exact - compensated summation: -0.00042

Sage example in ./float.tex, line 1242::

  sage: x = CDF(2,1.); x
  2.0 + 1.0*I
  sage: y = CDF(20,0); y
  20.0

Sage example in ./float.tex, line 1249::

  sage: z = ComplexDoubleElement(2.,1.); z
  2.0 + 1.0*I

Sage example in ./float.tex, line 1269::

  sage: C = ComplexField(); C(2,3)
  2.00000000000000 + 3.00000000000000*I
  sage: C100 = ComplexField(100); C100(2,3)
  2.0000000000000000000000000000 + 3.0000000000000000000000000000*I

Sage example in ./float.tex, line 1297::

  sage: R200 = RealField(200); R200.pi()
  3.1415926535897932384626433832795028841971693993751058209749
  sage: R200.euler_constant()
  0.57721566490153286060651209008240243104215933593992359880577

Sage example in ./float.tex, line 1314::

  sage: x = RDF.pi()/2; x.cos() # floating-point approximation of zero!
  6.123233995736757e-17
  sage: x.cos().arccos() - x
  0.0

Sage example in ./float.tex, line 1564::

  sage: r3 = RIF(sqrt(3)); r3
  1.732050807568877?
  sage: print(r3.str(style='brackets'))
  [1.7320508075688769 .. 1.7320508075688775]

Sage example in ./float.tex, line 1602::

  sage: sage.rings.real_mpfi.printing_style = 'brackets'

Sage example in ./float.tex, line 1616::

  sage: r2 = RIF(2); r2, r2.diameter()
  ([2.0000000000000000 .. 2.0000000000000000], 0.000000000000000)

Sage example in ./float.tex, line 1628::

  sage: rpi = RIF(sqrt(2),pi); rpi
  [1.4142135623730949 .. 3.1415926535897936]
  sage: RIF(0,+infinity)
  [0.0000000000000000 .. +infinity]

Sage example in ./float.tex, line 1649::

  sage: RBF(pi)
  [3.141592653589793 +/- ...e-16]
  sage: RealBallField(100)(pi)
  [3.14159265358979323846264338328 +/- ...e-30]

Sage example in ./float.tex, line 1662::

  sage: RBF(2).rad()
  0.00000000

Sage example in ./float.tex, line 1675::

  sage: si = sin(RIF(pi))
  sage: si.contains_zero()
  True
  sage: sb = sin(RBF(pi))
  sage: sb.contains_zero()
  True

Sage example in ./float.tex, line 1704::

  sage: a = RealIntervalField(30)(1, RR(1).nextabove())
  sage: a.bisection()
  ([1.0000000000 .. 1.0000000000], [1.0000000000 .. 1.0000000019])

Sage example in ./float.tex, line 1713::

  sage: b = RealIntervalField(2)(-1,6)
  sage: b.center(), b.diameter()
  (2.0, 8.0)

Sage example in ./float.tex, line 1725::

  sage: s = RIF(1,2)
  sage: b = RBF(s)
  sage: bpi = RBF(pi)
  sage: ipi = RIF(bpi)

Sage example in ./float.tex, line 1735::

  sage: RIF(RBF(RIF(1,2))) == RIF(1,2)
  False
  sage: RBF(RIF(RBF(pi))) == RBF(pi)
  False

Sage example in ./float.tex, line 1810::

  sage: E = RIF(-pi/4,pi)
  sage: sin(E)
  [-0.70710678118654769 .. 1.0000000000000000]
  sage: E = RIF(-1,2); exp(E)
  [0.36787944117144227 .. 7.3890560989306505]
  sage: E = RIF(0,1); log(E)
  [-infinity .. -0.0000000000000000]

Sage example in ./float.tex, line 1838::

  sage: E=RIF(-pi,pi)
  sage: f = lambda x: sin(x)/x
  sage: f(E)
  [-infinity .. +infinity]

Sage example in ./float.tex, line 1913::

  sage: x = RIF(-1,1)
  sage: 1-x^2
  [0.0000000000000000 .. 1.0000000000000000]
  sage: 1-x*x
  [0.0000000000000000 .. 2.0000000000000000]
  sage: (1-x)*(1+x)
  [0.0000000000000000 .. 4.0000000000000000]

Sage example in ./float.tex, line 1975::

  sage: def bisect(funct, x, tol, zeros):
  ....:     if 0 in funct(x):
  ....:         if x.diameter()>tol:
  ....:             x1,x2 = x.bisection()
  ....:             bisect(funct,x1,tol,zeros)
  ....:             bisect(funct,x2,tol,zeros)
  ....:         else:
  ....:             zeros.append(x)
  sage: sage.rings.real_mpfi.printing_style = 'question'
  sage: fs = lambda x: sin(1/x)
  sage: d = RealIntervalField(100)(1/64,1/32)
  sage: zeros = []
  sage: bisect(fs,d,10^(-25),zeros)
  sage: for s in zeros:
  ....:     s
  0.015915494309189533576888377?
  0.01675315190441003534409303?
  0.01768388256576614841876487?
  0.018724110951987686561045148?
  0.01989436788648691697111047?
  0.021220659078919378102517835?
  0.02273642044169933368126911?
  0.024485375860291590118289809?
  0.026525823848649222628147293?
  0.02893726238034460650343342?
  sage: dfs = lambda x: -cos(1/x)/x^2
  sage: not any(dfs(z).contains_zero() for z in zeros)
  True

Sage example in ./float.tex, line 2022::

  sage: def NearlySingularMatrix(R, n):
  ....:     M=matrix(R,n,n)
  ....:     for i in range(0,n):
  ....:         for j in range(0,n):
  ....:             M[i,j]= (1+log(R(1+i)))/((i+1)^2+(j+1)^2)
  ....:     return M

Sage example in ./float.tex, line 2044::

  sage: n=35
  sage: NearlySingularMatrix(RDF,n).det() == 0.0
  True

Sage example in ./float.tex, line 2053::

  sage: NearlySingularMatrix(RBF,n).det().contains_zero()
  True

Sage example in ./float.tex, line 2064::

  sage: def tryDet(R, n):
  ....:     p = 53
  ....:     z = True
  ....:     while z:
  ....:         p += 100
  ....:         MRF=NearlySingularMatrix(R(p),n)
  ....:         d = MRF.det()
  ....:         z = d.contains_zero()
  ....:     return p,d
  sage: tryDet(RealBallField,n)  # long time
  (1653, [9.552323592707808e-485 +/- 1.65e-501])

Sage example in ./float.tex, line 2095::

  sage: tryDet(RealIntervalField,n)  # long time
  (1653, 9.552323592707808?e-485)

Sage example in ./float.tex, line 2135::

  sage: CBF(sqrt(2),pi)
  [1.414213562373095...] + [3.141592653589793...]*I
  sage: CIF(sqrt(2),pi)
  1.414213562373095? + 3.141592653589794?*I
  sage: CIF(sqrt(2)+pi*I)
  1.414213562373095? + 3.141592653589794?*I
  sage: CBF(sqrt(2)+pi*I)
  [1.414213562373095...] + [3.141592653589793...]*I

Sage example in ./float.tex, line 2146::

  sage: sage.rings.real_mpfi.printing_style = 'brackets'

Sage example in ./float.tex, line 2149::

  sage: c = CIF(RIF(1,2),RIF(-3,3))
  sage: c.real()
  [1.0000000000000000 .. 2.0000000000000000]
  sage: c.imag()
  [-3.0000000000000000 .. 3.0000000000000000]
  sage: CBF(RIF(1,2),RIF(-3,3))
  [+/- 2.01] + [+/- 3.01]*I

Sage example in ./float.tex, line 2164::

  sage: sage.rings.real_mpfi.printing_style = 'question'

Sage example in ./float.tex, line 2167::

  sage: ComplexIntervalField(100)(1+I*pi).arg()
  1.26262725567891168344432208361?
  sage: ComplexBallField(100)(1+I*pi).arg()
  [1.26262725567891168344432208360 +/- ...e-30]
  sage: ComplexIntervalField(100)(1+I*pi).norm()
  10.8696044010893586188344909999?

Sage example in ./float.tex, line 2242::

  sage: sage.rings.real_mpfi.printing_style = 'question'

Sage example in ./float.tex, line 2245::

  sage: x=QQbar(sqrt(3)); x
  1.732050807568878?
  sage: x.interval(RealIntervalField(100))
  1.73205080756887729352744634151?
"""
