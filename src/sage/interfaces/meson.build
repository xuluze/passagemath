py.install_sources(
  '__init__.py',
  'abc.py',
  'all.py',
  'all__sagemath_polyhedra.py',
  'axiom.py',
  'ecm.py',
  'expect.py',
  'four_ti_2.py',
  'fricas.py',
  'frobby.py',
  'gap.py',
  'gap3.py',
  'gap_workspace.py',
  'genus2reduction.py',
  'gfan.py',
  'giac.py',
  'gnuplot.py',
  'gp.py',
  'interface.py',
  'jmoldata.py',
  'kash.py',
  'kenzo.py',
  'latte.py',
  'lie.py',
  'lisp.py',
  'macaulay2.py',
  'magma.py',
  'magma_free.py',
  'maple.py',
  'mathematica.py',
  'mathics.py',
  'matlab.py',
  'maxima.py',
  'maxima_abstract.py',
  'maxima_lib.py',
  'mupad.py',
  'mwrank.py',
  'octave.py',
  'phc.py',
  'polymake.py',
  'povray.py',
  'process.pxd',
  'psage.py',
  'qepcad.py',
  'qsieve.py',
  'quit.py',
  'r.py',
  'read_data.py',
  'rubik.py',
  'sage-maxima.lisp',
  'sage0.py',
  'scilab.py',
  'singular.py',
  'sympy.py',
  'sympy_wrapper.py',
  'tab_completion.py',
  'tachyon.py',
  'tests.py',
  'tides.py',
  subdir: 'sage/interfaces',
)

extension_data = {
  'process' : files('process.pyx'),
  'sagespawn' : files('sagespawn.pyx'),
}

foreach name, pyx : extension_data
  if is_windows
    # Uses posix API
    continue
  endif

  py.extension_module(
    name,
    sources: pyx,
    subdir: 'sage/interfaces',
    install: true,
    include_directories: [inc_cpython],
    dependencies: [py_dep, gmp],
  )
endforeach

