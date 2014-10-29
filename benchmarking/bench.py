"""
Benchmark a pi estimation method by running it a number of times with varying
input.
"""
import sys
import csv
import time
from numpy import logspace
import argparse
from functools import partial

# estimate module is in parent directory
sys.path.append('..')
import estimate

def check_range(arg, min, max):
    """Partial argparse range type (derived from int), use with
    functools.partial() to bind max/min.
    """
    try:
        value = int(arg)
    except ValueError as e:
       raise argparse.ArgumentTypeError('expected int, got %s' % arg) from e
    if value < min or value > max:
        message = 'Expected value in [%s, %s], got %s' % (min, max, value)
        raise argparse.ArgumentTypeError(message)
    return value

# estimation config
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('method', type=str,
        choices=estimate.methods, help='method of computation (optimization)')
parser.add_argument('--parallel', action='store_true', default=False,
        help='run using parallel computation (fast, but dangerous!)')
parser.add_argument('--tries', type=int, default=10,
        help='number of tries to run for each input')
parser.add_argument('--logmax', type=partial(check_range, min=1, max=7),
        default=5, help='maximum power of the logarithmic scale')
parser.add_argument('--precision', type=int, default=50,
        help=("precision of the benchmark, corresponding to the number of"
              "inputs generated along the benchmark's logarithmic scale"))
parser.add_argument('-o', '--output-file', type=argparse.FileType('w'),
        default=sys.stdout, help='file to write the benchmark output to')

if __name__ == '__main__':
    args = parser.parse_args()
    writer = csv.writer(args.output_file)
    writer.writerow(('nb_iters', 'time', 'estimation'))
    for nb_iters in map(int, logspace(1, args.logmax, args.precision)):
        for _ in range(args.tries):
            init_time = time.time()
            estimated_pi = estimate.pi(nb_iters, args.method, args.parallel)
            dt = time.time() - init_time
            writer.writerow((nb_iters, dt, estimated_pi))
            sys.stdout.flush()
    args.output_file.close()
