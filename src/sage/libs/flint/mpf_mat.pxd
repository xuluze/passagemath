# sage_setup: distribution = sagemath-flint
# distutils: libraries = flint
# distutils: depends = flint/mpf_mat.h

################################################################################
# This file is auto-generated by the script
#   SAGE_ROOT/src/sage_setup/autogen/flint_autogen.py.
# From the commit 3e2c3a3e091106a25ca9c6fba28e02f2cbcd654a
# Do not modify by hand! Fix and rerun the script instead.
################################################################################

from libc.stdio cimport FILE
from sage.libs.gmp.types cimport *
from sage.libs.mpfr.types cimport *
from sage.libs.flint.types cimport *

cdef extern from "flint_wrap.h":
    void mpf_mat_init(mpf_mat_t mat, slong rows, slong cols, flint_bitcnt_t prec) noexcept
    void mpf_mat_clear(mpf_mat_t mat) noexcept
    void mpf_mat_set(mpf_mat_t mat1, const mpf_mat_t mat2) noexcept
    void mpf_mat_swap(mpf_mat_t mat1, mpf_mat_t mat2) noexcept
    void mpf_mat_swap_entrywise(mpf_mat_t mat1, mpf_mat_t mat2) noexcept
    mpf * mpf_mat_entry(const mpf_mat_t mat, slong i, slong j) noexcept
    void mpf_mat_zero(mpf_mat_t mat) noexcept
    void mpf_mat_one(mpf_mat_t mat) noexcept
    void mpf_mat_set_fmpz_mat(mpf_mat_t B, const fmpz_mat_t A) noexcept
    void mpf_mat_randtest(mpf_mat_t mat, flint_rand_t state, flint_bitcnt_t bits) noexcept
    void mpf_mat_print(const mpf_mat_t mat) noexcept
    bint mpf_mat_equal(const mpf_mat_t mat1, const mpf_mat_t mat2) noexcept
    bint mpf_mat_approx_equal(const mpf_mat_t mat1, const mpf_mat_t mat2, flint_bitcnt_t bits) noexcept
    bint mpf_mat_is_zero(const mpf_mat_t mat) noexcept
    bint mpf_mat_is_empty(const mpf_mat_t mat) noexcept
    bint mpf_mat_is_square(const mpf_mat_t mat) noexcept
    void mpf_mat_mul(mpf_mat_t C, const mpf_mat_t A, const mpf_mat_t B) noexcept
    void mpf_mat_gso(mpf_mat_t B, const mpf_mat_t A) noexcept
    void mpf_mat_qr(mpf_mat_t Q, mpf_mat_t R, const mpf_mat_t A) noexcept
