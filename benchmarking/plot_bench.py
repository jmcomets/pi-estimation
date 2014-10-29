import sys
import csv
import math
import argparse
from statistics import mean as avg
from collections import OrderedDict
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('bench_file', type=argparse.FileType('r'),
        default=sys.stdin, help='file to read the benchmark output from')

if __name__ == '__main__':
    args = parser.parse_args()

    # read data
    benchs = OrderedDict()
    reader = csv.reader(args.bench_file)
    next(reader) # ignore header
    for line in reader:
        try:
            nb_iters, time, estimation = line
            nb_iters, time, estimation = int(nb_iters), float(time), float(estimation)
            bench = benchs.setdefault(nb_iters, {
                'estimations': [],
                'times': []
                })
            bench['estimations'].append(estimation)
            bench['times'].append(time)
        except ValueError:
            print('ignored line %s, bad format' % line, file=sys.stderr)
    args.bench_file.close()

    # plot data
    m, n = 1, 1
    xs = list(benchs.keys())
    plt.xlabel('Number of iterations')

    # all estimations
    sp1 = plt.subplot(m, n, 1)
    sp1.set_xscale('log')
    for x, b in benchs.items():
        sp1.scatter([x] * len(b['estimations']), b['estimations'], c='r')
    sp1.set_ylabel('All estimations', color='r')

    # math.pi horizontal line
    sp1.axhline(y=math.pi, c='y')

    # average time
    sp2 = sp1.twinx()
    sp2.plot(xs, [avg(b['times']) for b in benchs.values()], c='b')
    sp2.set_ylabel('Average runtime (s)', color='b')

    plt.show()
