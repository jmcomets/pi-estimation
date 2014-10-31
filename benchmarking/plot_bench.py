import sys
import csv
import math
import argparse
import statistics
import collections
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('bench_file', type=argparse.FileType('r'),
        default=sys.stdin, help=('file to read the benchmark output from'))
parser.add_argument('-o', '--output-image', type=argparse.FileType('w'),
        help='file to save the benchmark plot to')

def read_benchmarks(bench_file):
    benchs = collections.OrderedDict()
    reader = csv.reader(bench_file)
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
    return benchs

def plot_benchmarks(benchs):
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
    sp2.set_yscale('log') # linear complexity problem
    sp2.plot(xs, [statistics.mean(b['times']) for b in benchs.values()], c='b')
    sp2.set_ylabel('Average runtime (s)', color='b')

    # hacks
    sp1.set_ylim((1, 5))
    sp2.set_ylim((0, 1))

if __name__ == '__main__':
    args = parser.parse_args()

    # plot benchmarks
    with args.bench_file as fp:
        benchs = read_benchmarks(fp)
    plot_benchmarks(benchs)

    # either show or save
    if args.output_image:
        plt.savefig(args.output_image)
    else:
        plt.show()
