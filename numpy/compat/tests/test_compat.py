from os.path import join

from numpy.compat import isfileobj, getargspec, formatargspec
from numpy.testing import assert_, assert_equal
from numpy.testing import tempdir


def test_isfileobj():
    with tempdir(prefix="numpy_test_compat_") as folder:
        filename = join(folder, 'a.bin')

        with open(filename, 'wb') as f:
            assert_(isfileobj(f))

        with open(filename, 'ab') as f:
            assert_(isfileobj(f))

        with open(filename, 'rb') as f:
            assert_(isfileobj(f))


def test_getargspec():
    argspec_kwonly = (['a'], ['foo'], 'args', 'kwargs', None, (1,),)
    assert_equal(getargspec(lambda a, *args, foo=1, **kwargs: 0),
                 argspec_kwonly)


def test_formatargspec():
    format_kwonly = '(a, *args, foo=1, **kwargs)'
    assert_equal(
        formatargspec(*getargspec(lambda a, *args, foo=1, **kwargs: 0)),
        format_kwonly)
    format_kwonly2 = '(a, foo=1, *, bar=2)'
    assert_equal(
        formatargspec(*getargspec(lambda a, foo=1, *, bar=2: 0)),
        format_kwonly2
    )
