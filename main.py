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
args = parser.parse_args()

if __name__ == '__main__':
    print(estimate.pi(args.iterations))
