import sys
import numpy
import random

def throw_darts_numpy_random(amount):
    # dart throw: numpy random uniform
    hits = 0
    for i in range(int(amount)):
        x = numpy.random.uniform(0, 1)
        y = numpy.random.uniform(0, 1)
        hits += x**2 + y**2 <= 1
    return hits

def throw_darts_numpy_random_sample(amount):
    # dart throw: numpy random uniform array
    hits = 0
    xs = numpy.random.random(amount)
    ys = numpy.random.random(amount)
    for i in range(int(amount)):
        hits += xs[i]**2 + ys[i]**2 <= 1
    return hits

def throw_darts_pure_python(amount):
    # dart throw: pure python
    hits = 0
    for _ in range(int(amount)):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        hits += x**2 + y**2 <= 1
    return hits

methods = (
        'numpy_random',
        'numpy_random_sample',
        'pure_python',
        )

def throw_darts(amount, method):
    func = getattr(sys.modules[__name__], 'throw_darts_%s' % method)
    return func(amount)

def pi(nb_iters, method=methods[0]):
    """Estimate pi by the monte carlo method, computing the number of darts
    thrown in the unit square that were in the unit circle, passing in the
    number of darts to throw.
    """
    hits = throw_darts(nb_iters, method)
    return hits * 4 / float(nb_iters)
