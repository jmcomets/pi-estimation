"""
Estimate Pi by the Monte Carlo method.
"""

import argparse
import estimate
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('iterations', metavar='iterations', type=int,
        help='number of iterations to run')
parser.add_argument('-m', '--method', type=str,
        choices=estimate.methods, default=estimate.methods[0],
        help='method of computation (optimization)')
parser.add_argument('--parallel', action='store_true', default=False,
        help='run using parallel computation')

if __name__ == '__main__':
    args = parser.parse_args()
    print(estimate.pi(args.iterations, args.method, args.parallel))
