"""
Estimate Pi by the Monte Carlo method.
"""

import argparse
import estimate
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('iterations', metavar='iterations', type=int,
        help='number of iterations to run')
args = parser.parse_args()

if __name__ == '__main__':
    print(estimate.pi(args.iterations))
