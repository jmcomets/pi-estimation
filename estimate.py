"""
Estimate Pi by the Monte Carlo method.
"""
import random

def throw_darts(amount):
    # pure python dart throw
    hits = 0
    for _ in range(int(amount)):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        hits += x**2 + y**2 <= 1
    return hits

def estimate_pi(nb_iters):
    """Estimate pi by the monte carlo method, computing the number of darts
    thrown in the unit square that were in the unit circle, passing in the
    number of darts to throw.
    """
    hits = throw_darts(nb_iters)
    return hits * 4 / float(nb_iters)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('iterations', metavar='iterations', type=int, help='number of iterations to run')
    args = parser.parse_args()
    print(estimate_pi(args.iterations))
