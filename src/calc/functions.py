"""
Math functions for the evaluator, built on the standard library.

Every function accepts an int, float, or complex number. Complex input gives a
complex result, and real input gives a real result when one exists. Neither
``math`` (real only) nor ``cmath`` (always complex) does that by itself, so
each function picks one based on its input.

These functions used to come from numpy, and they keep numpy's results in the
places where ``math`` or ``cmath`` would raise instead:

* ``sqrt``, the logarithms, ``arcsin``, ``arccos``, and ``arctanh`` came from
  ``numpy.lib.scimath``. Real input outside their real domain gives a complex
  result, e.g. ``sqrt(-4) == 2j``.
* The other inverse functions give nan for real input outside their real
  domain, e.g. ``arccosh(0.5)``.
* Poles and overflow give inf, e.g. ``ln(0) == -inf`` and
  ``exp(1000) == inf``. Grading depends on this: two formulas that both
  evaluate to inf compare as equal, but a formula that raises can't be graded.
"""

import cmath
import math

INF = float("inf")
NAN = float("nan")
LN2 = math.log(2)
LN10 = math.log(10)


def _is_complex(x):
    return isinstance(x, complex)


def _recip(value):
    """
    Return 1 / value, with inf at zero instead of ZeroDivisionError.
    """
    if value == 0:
        if _is_complex(value):
            return complex(INF, NAN)
        return math.copysign(INF, value)
    return 1 / value


def _overflowed(real_scale, imag_scale, y):
    """
    Return real_scale * cos(y) + i * imag_scale * sin(y) for infinite scales.

    exp, sinh, and cosh of x + iy all have this form, and this is their value
    when x is large enough to overflow. Where sin(y) is zero, the imaginary
    part is a signed zero rather than nan.
    """
    sin_y = math.sin(y)
    if sin_y:
        imag = imag_scale * sin_y
    else:
        imag = math.copysign(1.0, imag_scale) * y
    return complex(real_scale * math.cos(y), imag)


def _complex_log(z):
    """
    Natural log of a complex number, with -inf at zero instead of ValueError.
    """
    if z == 0:
        return complex(-INF, math.atan2(z.imag, z.real))
    return cmath.log(z)


def _complex_arctanh(z):
    """
    Inverse hyperbolic tangent of a complex number, with inf at +/-1.
    """
    if z in (1, -1):
        return complex(math.copysign(INF, z.real), z.imag)
    return cmath.atanh(z)


# Trigonometric functions

def sin(x):
    """
    Sine
    """
    if _is_complex(x):
        return cmath.sin(x)
    return NAN if math.isinf(x) else math.sin(x)


def cos(x):
    """
    Cosine
    """
    if _is_complex(x):
        return cmath.cos(x)
    return NAN if math.isinf(x) else math.cos(x)


def tan(x):
    """
    Tangent
    """
    if _is_complex(x):
        return cmath.tan(x)
    return NAN if math.isinf(x) else math.tan(x)


def sec(x):
    """
    Secant
    """
    return _recip(cos(x))


def csc(x):
    """
    Cosecant
    """
    return _recip(sin(x))


def cot(x):
    """
    Cotangent
    """
    return _recip(tan(x))


# Inverse trigonometric functions
# http://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Relationships_among_the_inverse_trigonometric_functions

def arcsin(x):
    """
    Inverse sine. Complex for real input outside [-1, 1].
    """
    if _is_complex(x) or abs(x) > 1:
        return cmath.asin(x)
    return math.asin(x)


def arccos(x):
    """
    Inverse cosine. Complex for real input outside [-1, 1].
    """
    if _is_complex(x) or abs(x) > 1:
        return cmath.acos(x)
    return math.acos(x)


def arctan(x):
    """
    Inverse tangent
    """
    if not _is_complex(x):
        return math.atan(x)
    if x in (1j, -1j):
        return complex(math.copysign(0.0, x.real), math.copysign(INF, x.imag))
    return cmath.atan(x)


def arcsec(val):
    """
    Inverse secant. nan for real input inside (-1, 1).
    """
    val = 1. / val
    if _is_complex(val):
        return cmath.acos(val)
    return math.acos(val) if abs(val) <= 1 else NAN


def arccsc(val):
    """
    Inverse cosecant. nan for real input inside (-1, 1).
    """
    val = 1. / val
    if _is_complex(val):
        return cmath.asin(val)
    return math.asin(val) if abs(val) <= 1 else NAN


def arccot(val):
    """
    Inverse cotangent
    """
    if val.real < 0:
        return -math.pi / 2 - arctan(val)
    return math.pi / 2 - arctan(val)


# Hyperbolic functions

def sinh(x):
    """
    Hyperbolic sine
    """
    if _is_complex(x):
        try:
            return cmath.sinh(x)
        except OverflowError:
            return _overflowed(math.copysign(INF, x.real), INF, x.imag)
    try:
        return math.sinh(x)
    except OverflowError:
        return INF if x > 0 else -INF


def cosh(x):
    """
    Hyperbolic cosine
    """
    if _is_complex(x):
        try:
            return cmath.cosh(x)
        except OverflowError:
            return _overflowed(INF, math.copysign(INF, x.real), x.imag)
    try:
        return math.cosh(x)
    except OverflowError:
        return INF


def tanh(x):
    """
    Hyperbolic tangent
    """
    if _is_complex(x):
        return cmath.tanh(x)
    return math.tanh(x)


def sech(x):
    """
    Hyperbolic secant
    """
    return _recip(cosh(x))


def csch(x):
    """
    Hyperbolic cosecant
    """
    return _recip(sinh(x))


def coth(x):
    """
    Hyperbolic cotangent
    """
    return _recip(tanh(x))


# Inverse hyperbolic functions

def arcsinh(x):
    """
    Inverse hyperbolic sine
    """
    if _is_complex(x):
        return cmath.asinh(x)
    return math.asinh(x)


def arccosh(x):
    """
    Inverse hyperbolic cosine. nan for real input below 1.
    """
    if _is_complex(x):
        return cmath.acosh(x)
    return math.acosh(x) if x >= 1 else NAN


def arctanh(x):
    """
    Inverse hyperbolic tangent. Complex for real input outside [-1, 1].
    """
    if _is_complex(x) or abs(x) > 1:
        return _complex_arctanh(x)
    if abs(x) == 1:
        return math.copysign(INF, x)
    return math.atanh(x)


def arcsech(val):
    """
    Inverse hyperbolic secant. nan for real input outside (0, 1].
    """
    return arccosh(1. / val)


def arccsch(val):
    """
    Inverse hyperbolic cosecant
    """
    return arcsinh(1. / val)


def arccoth(val):
    """
    Inverse hyperbolic cotangent. nan for real input inside (-1, 1).
    """
    val = 1. / val
    if _is_complex(val):
        return _complex_arctanh(val)
    if abs(val) == 1:
        return math.copysign(INF, val)
    return math.atanh(val) if abs(val) < 1 else NAN


# Exponential, logarithms, and square root

def exp(x):
    """
    Exponential
    """
    if _is_complex(x):
        try:
            return cmath.exp(x)
        except OverflowError:
            return _overflowed(INF, INF, x.imag)
    try:
        return math.exp(x)
    except OverflowError:
        # An int too big to convert to float overflows even when negative.
        return INF if x > 0 else 0.0


def ln(x):
    """
    Natural logarithm. Complex for negative real input.
    """
    if _is_complex(x) or x < 0:
        return _complex_log(x)
    return -INF if x == 0 else math.log(x)


def log10(x):
    """
    Base-10 logarithm. Complex for negative real input.
    """
    if _is_complex(x) or x < 0:
        if x == 0:
            natural = _complex_log(x)
            return complex(natural.real, natural.imag / LN10)
        return cmath.log10(x)
    return -INF if x == 0 else math.log10(x)


def log2(x):
    """
    Base-2 logarithm. Complex for negative real input.
    """
    if _is_complex(x) or x < 0:
        natural = _complex_log(x)
        return complex(natural.real / LN2, natural.imag / LN2)
    return -INF if x == 0 else math.log2(x)


def sqrt(x):
    """
    Square root. Complex for negative real input.
    """
    if _is_complex(x) or x < 0:
        return cmath.sqrt(x)
    return math.sqrt(x)
